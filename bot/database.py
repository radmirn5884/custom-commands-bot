from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.chat import Base, Chat
from models.command import CustomCommand

engine = create_engine('sqlite:///bot_chats.db')
SessionLocal = sessionmaker(bind=engine)

def init_db():
    """Инициализация базы данных"""
    Base.metadata.create_all(engine)

def get_db():
    """Получение сессии базы данных"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
