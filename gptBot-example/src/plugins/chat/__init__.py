
import json
from nonebot import on_command, on_message
from nonebot.rule import to_me
from nonebot.adapters import Message
from nonebot.adapters import Event
import requests
import re

pattern = re.compile(r"^chatGPT\s*(.*)$")  # 匹配以 chatGPT 开头的字符串，并获取后面的内容

chatgpt = on_command("", rule=to_me(), aliases={
                     "gpt", "chatgpt"}, priority=10, block=True)


@chatgpt.handle()
async def handle_function(event: Event):
    message = event.get_plaintext()
    
    if message:
        match = pattern.match(message.strip())
        if not match:
            # 如果匹配失败则结束命令处理
            await chatgpt.finish("命令格式错误，请输入 chatGPT + 需要查询的内容")
            return
        query = match.group(1)  # 获取正则匹配结果中第一个括号中的内容
        text = requestApi(query)
        print(text)
        await chatgpt.finish(text)
    else:
        await chatgpt.finish("请输入内容")


def requestApi(msg):
    msg_body = {
        "msg": msg
    }
    response = requests.get('http://127.0.0.1:8000/chat-api/?msg='+msg)
    result = json.loads(response.text)
    text = result['text']['message']['content']
    return text
