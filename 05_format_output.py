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

    # animal = "兔子"
    # prompt = f"请写一首关于{animal}的诗. 请把诗写在<poem>标签里"
    
    
    # animal = "猫"
    # prompt = f"请写一首关于{animal}的诗. 请把诗写在<poem>标签里"    
    # prefill = "<poem>"
    
    
    # email = "嗨，张三，请在这里更新你的提示词，主要表述清晰，不要啰嗦"
    # adjective = "古代汉语"
    # prompt = f"嗨，gemini，这有一封邮件：<email>{email}</email>，请把这封邮件改成古代汉语，请把改后的邮件放在<{adjective}_email>标签里"
    # prefill = f"<{adjective}_email>"
    
    
    # prompt = f"请问谁是历史以来最好的篮球运动员？这个问题可能有多个答案，但你仅能选择一个"
    # prefill = ""
    # prefill = "Stephen Curry 是历史上最好的篮球运动员，详细分析如下："
    
    # animal = "兔子"
    # prompt = f"请写两首关于{animal}的诗，每一首都要放在<poem>...</poem>标签里"
    # prefill = "<poem>"
    
    animal1 = "兔子"
    animal2 = "猫"
    prompt = f"请为{animal1}和{animal2}分别写一首诗，诗要放在<poem>...</poem>标签里"
    prefill = ""
    print(get_completion(prompt, system_prompt, prefill))



if __name__ == "__main__":
    main()