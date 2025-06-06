import os
import json
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import tiktoken

_ = load_dotenv(find_dotenv())

API_KEY = os.environ["API_KEY"]
SYSTEM_MESSAGE = os.environ["SYSTEM_MESSAGE"]
BASE_URL = "https://api.together.xyz"
DEFAULT_MODEL = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"
FILENAME = "message_history.json"
INPUT_TOKEN_LIMIT = 2048

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def chat_completion(messages, model=DEFAULT_MODEL, temperature=0.1, **kwargs):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        stream=False,
        **kwargs,
    )
    return response.choices[0].message.content

def chat_completion_stream(messages, model=DEFAULT_MODEL, temperature=0.1, **kwargs):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        stream=True,
        **kwargs,
    )

    response_content = ""

    for chunk in response:
        chunk_content = chunk.choices[0].delta.content
        if chunk_content is not None:
            print(chunk_content, end="")
            response_content += chunk_content

    print()
    return response_content

def count_tokens(text, model):
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)
    return len(tokens)

def count_total_tokens(messages, model):
    total = 0
    for message in messages:
        total += count_tokens(message["content"], model)
    return total

def enforce_token_limit(messages, token_limit, model=DEFAULT_MODEL):
    while count_total_tokens(messages, model) > token_limit:
        if len(messages) > 1:
            messages.pop(1)
        else:
            break

def save_to_json_file(obj, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(obj, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"{filename} 파일에 내용을 저장하는 중에 오류가 발생했습니다:\n{e}")

def load_from_json_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"{filename} 파일 내용을 읽어오는 중에 오류가 발생했습니다:\n{e}")
        return None

def chatbot():
    messages = load_from_json_file(FILENAME)
    if not messages:
        messages = [
            {"role": "system", "content": SYSTEM_MESSAGE},
        ]

    print("Chatbot: 안녕하세요! 무엇을 도와드릴까요? (종료하려면 'quit' 또는 'exit'을 입력하세요.)\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            break

        messages.append({"role": "user", "content": user_input})

        total_tokens = count_total_tokens(messages, DEFAULT_MODEL)
        print(f"[현재 토큰 수: {total_tokens} / {INPUT_TOKEN_LIMIT}]")

        enforce_token_limit(messages, INPUT_TOKEN_LIMIT)

        print("\nChatbot: ", end="")
        response = chat_completion_stream(messages)
        print()

        messages.append({"role": "assistant", "content": response})

        save_to_json_file(messages, FILENAME)

chatbot()