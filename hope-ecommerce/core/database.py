from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from core.configs import ConfigSetting

engine: AsyncEngine = create_async_engine(ConfigSetting.DATABASE_URL)  # Corrigido para DATABASE_URL
Session: AsyncSession = sessionmaker(bind=engine,
                                     class_=AsyncSession,
                                     expire_on_commit=False,
                                     autoflush=False)