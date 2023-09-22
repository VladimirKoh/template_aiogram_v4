import aiomysql
from data import config


async def create_conn():
    conn = await aiomysql.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASS,
        db=config.DB_NAME,
        charset='utf8mb4',
        cursorclass=aiomysql.cursors.DictCursor
    )
    return conn


async def close_conn(conn):
    conn.close()


async def add_user(user_id):
    conn = await create_conn()
    async with conn.cursor() as cursor:
        query = "INSERT INTO `users` (`user_id`) VALUES(%s)"
        await cursor.execute(query, user_id)
        await conn.commit()
    await close_conn(conn)
