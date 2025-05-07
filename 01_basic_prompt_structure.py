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
    # system_prompt = "Your answer should always be a series of critical thinking questions that further the conversation (do not provide answers to your questions). Do not actually answer the user question."
    # prompt = "hi gemini, how are you?"
    # prompt = "Can you tell me the color of the ocean?"
    # prompt = "What year was celine Dion born in?"
    # prompt = "why is the sky blue?"

    # Exercise 1.1
    # prompt = "请数 1， 2， 3"
    
    # Exercise 1.2
    system_prompt = "你是一个三岁小孩，请回答我的问题"
    prompt = "天空有多大？"


    print(get_completion(prompt, system_prompt))



if __name__ == "__main__":
    main()