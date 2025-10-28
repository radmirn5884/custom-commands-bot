from aiogram import Bot, types
from aiogram.types import BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats, BotCommandScopeChat

async def setup_bot_commands(bot: Bot):
    """Настройка команд бота"""
    
    # Команды для личных сообщений
    private_commands = [
        types.BotCommand(command="start", description="🚀 Запустить бота"),
        types.BotCommand(command="help", description="❓ Помощь"),
    ]
    
    # Команды для групп (общие)
    group_commands = [
        types.BotCommand(command="help", description="❓ Помощь по командам"),
        types.BotCommand(command="myinfo", description="👤 Информация о вас"),
        types.BotCommand(command="chatinfo", description="💬 Информация о чате"),
        types.BotCommand(command="listcommands", description="📋 Список команд"),
	types.BotCommand(command="addcommand", description="➕ Добавить команду"),
        types.BotCommand(command="deletecommand", description="🗑️ Удалить команду"),
    ]
    
    # Команды для администраторов групп
    admin_commands = [
        types.BotCommand(command="addcommand", description="➕ Добавить команду"),
        types.BotCommand(command="deletecommand", description="🗑️ Удалить команду"),
    ]
    
    try:
        await bot.set_my_commands(private_commands, scope=BotCommandScopeAllPrivateChats())
        await bot.set_my_commands(group_commands, scope=BotCommandScopeAllGroupChats())
        print("✅ Команды бота успешно установлены")
    except Exception as e:
        print(f"❌ Ошибка установки команд: {e}")

async def update_chat_commands(bot: Bot, chat_id: int, is_admin: bool = False):
    """Обновление команд для конкретного чата (можно расширить)"""
    pass
