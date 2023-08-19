<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>

# NoneBot-Plugin-Send-Message
_✨ 一个可以群昵称显示现在时间的插件 ✨_
    <br></br>
</div>

## 如何安装？如何下载？
你可以使用 python中的pip
```bash
   pip install nonebot-plugin-send-message
```

   或者nonebot里的
```bash
  nb plugin install nonebot-plugin-send-message
```
---
## 如何使用？

先打开你的`.env.dev`或者`.env.prod`文件 添加如下内容

```bash
send_message=["10001"] # 输入你的qq号记得带双引号
welcome = "欢迎你添加我为好友\n我是一个传话机器人\n直接把你需要传递的信息发给我" # 欢迎添加好友的信息 发送图片表情请手动cq码
SUPERUSERS=["123123123"] # nonebot超级管理员配置
```

`send_message`是发送给传话的主人 就是对方发送消息传达的对象

`welcome`为欢迎语

### 这是主人发送对话用的

`/传话 [QQ] [内容]` `#传话给指定的用户`

注意此命令使用nonebot超级管理员才可以触发 如果你配置文件有`SUPERUSERS`直接添加你的qq号就行，没有的可以抄上面，有就忽略吧

---
## 有bug？ 无法使用？
请发issues给我

---

## 效果

![](https://s1.ax1x.com/2023/08/12/pPuDEPH.png)

![](https://s1.ax1x.com/2023/08/12/pPuDVGd.png)
