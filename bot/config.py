import os
from dataclasses import dataclass
from decouple import config

@dataclass
class BotConfig:
    token: str = config('BOT_TOKEN')
    
bot_config = BotConfig()
