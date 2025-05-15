#! /usr/bin/env python3

import os
import openai
import argparse
import logging
import anthropic

logging.basicConfig(level=logging.DEBUG)

def get_completion(prompt: str, system_prompt = "", prefill = ""):
    openai.api_base = "https://llm-gateway.momenta.works"
    openai.api_key = "sk-C_cHvXw-KB1QUxV2qy9qlw"

    response = openai.ChatCompletion.create(
        # model="gemini/gemini-2.5-pro-preview-03-25",
        model="gemini-2.5-flash-preview-04-17",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": prefill}
        ],
        presence_penalty=0,
        temperature=0,
        max_tokens=65535,
    )
    response_content = response.choices[0].message.content
    return response_content

def main():
    system_prompt = ""
    prefill = ""
    # prompt = """下面这句电影评论是积极的还是消极的？
    
    # 这部电影以其新颖和原创让我大开眼界。说件不相关的事，今天的米线一般，但是就餐体验还不错"""


    # system_prompt = "你是一个精明的电影评论读者"
    
    # prompt = """下面这句电影评论是积极的还是消极的？在回答之前，请使用<positive-argument> and <negative-argument> XML 标签，标出电影评论中的积极和消极的论点。
    
    # 这部电影以其新颖和原创让我大开眼界。说件不相关的事，今天的米线一般，但是就餐体验还不错"""


    # prompt = "请说出由一位 1956 年出生的著名的电影演员主演的电影名称"
    # prompt = "请说出由一位 1956 年出生的著名的电影演员主演的电影名称。在回答之前，先使用<brainstorm> xml 标签，列出一些 1956 年出生的著名的电影演员，然后再给出答案"

    # email = "你好，我的联想笔记本电脑在运行时发生奇怪的声音，还散发着塑料烧焦的味道，我需要更换一台新的设备"
    # email = "你好，我能用我的苹果手机砸核桃吗，还是说他只能打电话"
    # email = "狗日的移动，几个月前我都已经把那个彩铃服务关了，怎么一直在扣费，你们咋回事，诈骗吗"
    email = "我不会游泳，怎么把我弄这来了，我妈呢"
    prompt = f"""这有一封邮件: <email>{email}</email>. 请根据邮件内容，将邮件按以下类别分类：
    <category>
    1. 售前问题
    2. 损害或有缺陷的商品
    3. 账单问题
    4. 其他（请说明具体原因）
    </category>
    请以如下格式回复：<answer>类别序号</answer>
    """

    print(get_completion(prompt, system_prompt, prefill))



if __name__ == "__main__":
    main()