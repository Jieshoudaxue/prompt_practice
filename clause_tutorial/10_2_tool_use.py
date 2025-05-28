#! /usr/bin/env python3

import os
import openai
import argparse
import logging
import anthropic

logging.basicConfig(level=logging.DEBUG)

def get_completion(messages, system_prompt="", prefill="", stop_sequences=None):
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
        stop_sequences=stop_sequences
    )
    response_content = response.choices[0].message.content
    return response_content

def main():
    
    

if __name__ == "__main__":
    main()