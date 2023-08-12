from nonebot import on_message, on_notice, on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import PrivateMessageEvent,PRIVATE,Bot,FriendAddNoticeEvent,Message
from nonebot.params import CommandArg,Depends
from nonebot.permission import SUPERUSER
from . import config


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
    for i in config.friend_list:
        await bot.send_private_msg(user_id=int(i),message=f"来自好友:{event.get_user_id()}\n"+event.get_message(),auto_escape=False)
    await js.finish()

@b.handle()
async def _(event:FriendAddNoticeEvent):
    await b.finish(Message(config.message))