from nonebot import get_driver
from nonebot.log import logger

class Config():
    message:str = get_driver().config.dict().get("welcome","你好呀")
    friend_list:list = get_driver().config.dict().get("send_message",[])
