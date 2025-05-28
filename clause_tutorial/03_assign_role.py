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

    # prompt = "请用一句话评论滑板爱好者"

    # system_prompt = "你是一只猫"
    # prompt = "请用一句话评论滑板爱好者"

    # system_prompt = "你是一只猫，正在跟一群滑板爱好者聊天"
    # prompt = "请用一句话评论滑板爱好者"

    # prompt = "张三正看着李四；李四正看着王五；张三结婚了，王五没有结婚，我们并不知道李四是否结婚了；请问是否有一个已经结婚的人在看着另一个没有结婚的人？"

    # system_prompt = "你是一名机器人，专门用来回答复杂的逻辑问题。"
    # prompt = "张三正看着李四；李四正看着王五；张三结婚了，王五没有结婚，我们并不知道李四是否结婚了；请问是否有一个已经结婚的人在看着另一个没有结婚的人？"

    system_prompt = "你是一名机器人，专门用来解答复杂的数学问题。"
    prompt = "下面的算术运算是否正确：" \
    "2x - 3 = 9" \
    "2x = 6" \
    "x = 3"

    print(get_completion(prompt, system_prompt))


if __name__ == "__main__":
    main()