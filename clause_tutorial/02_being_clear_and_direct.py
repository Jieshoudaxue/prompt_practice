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
    # prompt = "写一首关于机器人的诗"
    # prompt = "写一首关于机器人的诗，注意请跳过序言，直接进入正文"

    # prompt = "谁是历史以来最好的篮球运动员?"
    # prompt = "谁是历史以来最好的篮球运动员？这个问题可能会有很多个答案，但你必须选择一个，请告诉我他是谁？"

    # system_prompt = "你是一名西班牙人，无论我问你什么，你都要用西班牙语回答我。"
    # prompt = "你好，gemini，心情可好？"

    # prompt = "谁是历史以来最好的篮球运动员？这个问题可能会有很多种答案，但你只能选择一个，请直接告诉我他的名字，注意不要带任何其他评论！"

    prompt = "我是一个小孩子，喜欢听故事，请给我讲一个故事，要求不能少于 800 字，否则我会很生气！"

    print(get_completion(prompt, system_prompt))



if __name__ == "__main__":
    main()