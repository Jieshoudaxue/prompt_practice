#! /usr/bin/env python3


import openai
import os
import subprocess
import json
from typing import Dict, List, Any, Optional, Tuple, Union



bash_tool = {
    "name": "bash",
    "description": "Execute bash commands and return the output",
    "input_schema": {
        "type": "object",
        "properties": {
            "command": {
                "type": "string",
                "description": "The bash command to execute"
            }
        },
        "required": ["command"]
    }
}


class LLM:
    def __init__(self):
        self.system_prompt = """You are a helpful AI assistant with access to bash commands.
        You can help the user by executing commands and interpreting the results.
        Be careful with destructive commands and always explain what you're doing.
        You have access to the bash tool which allows you to run shell commands."""
        self.messages = [
            {"role": "system", "content": self.system_prompt},
        ]
        self.tools = [bash_tool]

    def __call__(self, content):
        
        self.messages.append({"role": "user", "content": content})

        openai.api_base = "https://llm-gateway.momenta.works"
        openai.api_key = "sk-C_cHvXw-KB1QUxV2qy9qlw"
        response = openai.ChatCompletion.create(
            # model="gemini/gemini-2.5-pro-preview-03-25",
            model="gemini-2.5-flash-preview-04-17",
            messages=self.messages,
            tools=self.tools,
            tool_choice="auto"
        )
        response_content = response.choices[0].message
        assistant_response = {"role": "assistant", "content": []}
        tool_calls = []
        # 处理tool_calls
        if response_content.tool_calls:
            # 如果有工具调用，需要包含tool_calls字段
            assistant_response["tool_calls"] = []
            for tool_call in response_content.tool_calls:
                assistant_response["tool_calls"].append({
                    "id": tool_call.id,
                    "type": "function",
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments
                    }
                })
                tool_calls.append({
                    "id": tool_call.id,
                    "name": tool_call.function.name,
                    "input": json.loads(tool_call.function.arguments)
                })
        self.messages.append(assistant_response)
        return assistant_response, tool_calls

# Function to execute bash commands
def execute_bash(command):
    """Execute a bash command and return a formatted string with the results."""
    # If we have a timeout exception, we'll return an error message instead
    try:
        result = subprocess.run(
            ["bash", "-c", command],
            capture_output=True,
            text=True,
            timeout=10
        )
        return f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}\nEXIT CODE: {result.returncode}"
    except Exception as e:
        return f"Error executing command: {str(e)}"


def handle_tool_call(tool_call):
    if tool_call["name"] != "bash":
        raise Exception(f"Unsupported tool: {tool_call['name']}")

    command = tool_call["input"]["command"]
    print(f"Executing bash command: {command}")
    output_text = execute_bash(command)
    print(f"Bash output:\n{output_text}")
    
    # 返回符合OpenAI API格式的工具结果
    return {
        "role": "tool",
        "tool_call_id": tool_call["id"],
        "content": output_text
    }


def user_input():
    x = input("You: ")
    if x.lower() in ["exit", "quit"]:
        print("\nExiting agent loop. Goodbye!")
        raise SystemExit(0)
    return x


def loop(llm):
    msg = ""    
    while True:
        msg = user_input()
        output, tool_calls = llm(msg)
        print("Agent: ", output)
        for tc in tool_calls:
            handle_tool_call(tc)


def main():
    try:
        print("\n=== LLM Agent Loop with Claude and Bash Tool ===\n")
        print("Type 'exit' to end the conversation.\n")
        loop(LLM())
    except KeyboardInterrupt:
        print("\n\nExiting. Goodbye!")
    except Exception as e:
        print(f"\n\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()