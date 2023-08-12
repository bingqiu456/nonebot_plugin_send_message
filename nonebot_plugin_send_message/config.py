from nonebot import get_driver
from nonebot.log import logger

friend_list = get_driver().config.dict().get("send_message",[])
if not friend_list:
    logger.warning("警告:未配置接受对象")

message = get_driver().config.dict().get("welcome","你好呀")
