import orm
import asyncio
from models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(user='root', password='', db='awesome', loop=loop)
    u = User(name='test_user_1', email='test_user_1@example.com', password='123456', image='about:blank')
    await u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
