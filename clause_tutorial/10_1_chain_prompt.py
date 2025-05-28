#! /usr/bin/env python3

import os
import openai
import argparse
import logging
import anthropic

logging.basicConfig(level=logging.DEBUG)

def get_completion(messages, system_prompt=""):
    openai.api_base = "https://llm-gateway.momenta.works"
    openai.api_key = "sk-C_cHvXw-KB1QUxV2qy9qlw"

    response = openai.ChatCompletion.create(
        model="gemini/gemini-2.5-pro-preview-03-25",
        # model="gemini-2.5-flash-preview-04-17",
        # model="deepseek/deepseek-chat",
        messages=messages,
        presence_penalty=0,
        temperature=0,
        max_tokens=65535,
    )
    response_content = response.choices[0].message.content
    return response_content

def main():
    """
    
    first_user = "请列出十个汉字，要求偏旁部首必须带有：金，木，水，火，土"
    messages = [
        {
            "role": "user",
            "content": first_user
        }
    ]

    # first_response = get_completion(messages)
    first_response = "钱，错，被，杯，波，涛，灾，焰，怀，坏"
    print(first_response)

    second_user = "在刚才的汉字中，请找出偏旁部首不是金，木，水，火，土的汉字。如果没找到，请回答：没找到"

    messages = [
        {
            "role": "user",
            "content": first_user
        },
        {
            "role": "assistant",
            "content": first_response
        },
        {
            "role": "user",
            "content": second_user
        }
    ]

    second_response = get_completion(messages)
    print(second_response)
    """
    
    """
    first_user = "请帮我给一位喜欢跑步的女孩写三个短故事，每个故事不超过100字。"
    messages = [
        {
            "role": "user",
            "content": first_user
        }
    ]

    first_response = get_completion(messages)
    print(first_response)

    second_user = "请修改上述的三个故事，让故事更曲折，情节更精彩，能吸引男生阅读。"
    messages = [
        {
            "role": "user",
            "content": first_user
        },
        {
            "role": "assistant",
            "content": first_response
        },
        {
            "role": "user",
            "content": second_user
        }
    ]

    second_response = get_completion(messages)
    print(second_response)
    """

    first_user = """请从《水浒传》中选出十个最精彩的花名，并解释好在哪里"""
    prefill = "<name>"
    messages = [
        {
            "role": "user",
            "content": first_user
        },
        {
            "role": "assistant",
            "content": prefill
        }
    ]

    first_response = get_completion(messages)
    print(first_response)

    second_user = "请给上述的水浒传花名，按照精彩程度进行排序，并给出理由。"
    messages = [
        {
            "role": "user",
            "content": first_user
        },
        {
            "role": "assistant",
            "content": prefill + "\n" + first_response
        },
        {
            "role": "user",
            "content": second_user
        }
    ]

    second_response = get_completion(messages)
    print(second_response)

if __name__ == "__main__":
    main()