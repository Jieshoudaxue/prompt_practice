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

    # prompt = "请问我圣诞节会收到礼物吗？"

    # prompt = """下面是一组对话，请以 A 的身份继续完成对话：
    # Q: 为什么圣诞老人会在圣诞节前夜给孩子们送礼物呀？
    # A: 因为圣诞老人喜欢你们，他希望所有的孩子们都能过一个快乐的圣诞节。
    # Q: 那我圣诞节会收到礼物吗？
    # """

    # prompt = """当今中国汽车行业，有几大风云人物，他们分别是：
    # <individuals>
    # 1. 雷军 [小米]
    # 2. 王传福 [比亚迪]
    # 3. 余承东 [华为]
    # 4. 李斌 [蔚来]
    # </individuals>
    # 请问在美国，有哪些类似的人物？
    # """
    # prefill = "<individuals>"

    email = "我不会游泳，怎么把我弄这来了，我妈呢"
    prompt = f"""这有一封邮件: <email>{email}</email>. 请根据邮件内容，将邮件按以下类别分类：
    <category>
    1. 售前问题
    2. 损害或有缺陷的商品
    3. 账单问题
    4. 其他（请说明具体原因）
    </category>
    请以如下格式回复：答案是：类别序号
    """

    print(get_completion(prompt, system_prompt, prefill))



if __name__ == "__main__":
    main()