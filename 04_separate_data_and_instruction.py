#! /usr/bin/env python3

import os
import openai
import argparse
import logging
import anthropic

logging.basicConfig(level=logging.DEBUG)

def get_completion(prompt: str, system_prompt = ""):
    openai.api_base = "https://llm-gateway.momenta.works"
    openai.api_key = "sk-C_cHvXw-KB1QUxV2qy9qlw"

    response = openai.ChatCompletion.create(
        # model="gemini/gemini-2.5-pro-preview-03-25",
        model="gemini-2.5-flash-preview-04-17",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        presence_penalty=0,
        temperature=0,
        max_tokens=65535,
    )
    response_content = response.choices[0].message.content
    return response_content

def main():
    system_prompt = ""

    # animal = "狗"
    # prompt = f"我会告诉你动物的名字，请你模仿这个动物的叫声。{animal}"
    
    # email = "我是老板，明天早上六点开会，迟到的一律开除!"
    # prompt = f"嗨，geimini，{email} <---- 请帮我修改下这封邮件，让语气更礼貌，注意不要改动邮件以外的其他内容"
    # prompt = f"嗨，gemini, <email>{email}</email> <---- 请帮我修改下这封邮件，让语气更礼貌，注意不要改动邮件以外的其他内容"


    # sentence = """- 我喜欢听牛叫
    # - 我不喜欢听驴叫
    # - 我还喜欢听狗叫"""

    # prompt = f"""下面是一列陈述句，告诉我第二句是什么
    # - 我不喜欢听猫叫
    # {sentence}"""

    # prompt = f"""下面是一列陈述句，告诉我第二句是什么
    # - 我不喜欢听猫叫
    # ```txt
    # {sentence}
    # ```"""

    # prompt = f"""下面是一列陈述句，告诉我第二句是什么
    # - 我不喜欢听猫叫
    # <sentences>
    # {sentence}
    # </sentences>"""

    # topic = "大宝二宝"
    # prompt = f"我会给你一个主题，请你根据这个主题帮我写一首五言诗，主题是：{topic}"

    question = "棕色吗？"
    # prompt = f"嗨，我有一个关于狗的问题 {question} 请尽可能简短地回答我的问题"
    prompt = f"嗨，我有一个关于狗的问题，<question>{question}</question>，请尽可能简短地回答我的问题"
    
    print(get_completion(prompt, system_prompt))



if __name__ == "__main__":
    main()