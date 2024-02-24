from core.configs import ConfigSetting
from core.database import engine


async def create_table() -> None:
    import models.__all__models
    
    async with engine.begin() as conn:
        await conn.run_sync(ConfigSetting.DBBaseModel.metadata.drop_all)
        await conn.run_sync(ConfigSetting.DBBaseModel.metadata.create_all)
        await conn.commit()
        print("Tabelas criadas com sucesso!")


if __name__ == "__main__":
    import asyncio
    asyncio.run(create_table())