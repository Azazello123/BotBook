from dataclasses import dataclass
from typing import List
from typing import Union


from environs import Env


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: List[int]  # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot


# Создаем функцию, которая будет читать файл .env и возвращать
# экземпляр класса Config с заполненными полями token и admin_ids
def load_config(path: Union[str, None] = None):
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS')))
        )
    )