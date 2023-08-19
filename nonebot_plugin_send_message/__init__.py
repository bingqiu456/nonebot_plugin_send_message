from asyncio.log import logger
from nonebot import on_message, on_notice, on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import PrivateMessageEvent,PRIVATE,Bot,FriendAddNoticeEvent,Message
from nonebot.params import CommandArg,Depends
from nonebot.permission import SUPERUSER
from .config import Config
from nonebot.plugin import PluginMetadata


if not Config.friend_list:
    logger.warning("未配置名单！")

__plugin_meta__ = PluginMetadata(
    name="双向聊天插件",
    description="一个支持双向聊天的传话插件，可用于临时聊天而不想加好友场景",
    usage="没什么用",
    type="application",
    config=Config,
    homepage="https://github.com/bingqiu456/nonebot_plugin_send_message",
    supported_adapters="onebot v11"
)

async def dependency():
    Matcher.skip()

js = on_message(priority=5,permission=PRIVATE)
b = on_notice(priority=4)
fs = on_command("传话",priority=1,permission=SUPERUSER)

@fs.handle()
async def _(bot:Bot,matcher: Matcher,event:PrivateMessageEvent,c:Message = CommandArg()):
    matcher.stop_propagation()
    d = str(c).split(" ",maxsplit=1)
    if len(d) != 2:
        await fs.finish()
    await bot.send_private_msg(user_id=int(d[0]),message=d[1],auto_escape=False)
    await fs.finish("已发送！")

@js.handle()
async def _(bot:Bot, event: PrivateMessageEvent,check=Depends(dependency)):
    for i in Config.friend_list:
        await bot.send_private_msg(user_id=int(i),message=f"来自好友:{event.get_user_id()}\n"+event.get_message(),auto_escape=False)
    await js.finish()

@b.handle()
async def _(event:FriendAddNoticeEvent):
    await b.finish(Message(Config.message))