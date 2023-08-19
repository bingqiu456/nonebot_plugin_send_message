 # -*- coding: utf-8 -*-
import setuptools
setuptools.setup(
    name = "nonebot_plugin_send_message",
    version = "3.0",
    packages = setuptools.find_packages(),
    author="bingyue",
    author_email="hello-yiqiu@qq.com",
    description="""一个支持双向聊天的传话插件，可用于临时聊天而不想加好友场景""",
    url="https://github.com/bingqiu456/nonebot_plugin_send_message",
    install_requires=[
        "nonebot2>=2.0.0rc3",
        "nonebot-adapter-onebot>=2.2.1",
    ],
    keywords=["nonebot_plugin_send_message","nonebot","nonebot_plugin"],
)