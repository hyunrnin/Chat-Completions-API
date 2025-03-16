import os

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

_ = load_dotenv(find_dotenv())

API_KEY = os.environ["API_KEY"]
BASE_URL = "https://api.together.xyz"
DEFAULT_MODEL = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

messages = [
    {"role": "user", "content": "여기에 원하는 질문 입력."},
]


def chat_completion(messages, model=DEFAULT_MODEL, temperature=0.7, **kwargs):
    response = client.chat.completions.create(
    model=DEFAULT_MODEL,
    messages=messages,
    temperature=temperature,
    stream=False,
    **kwargs,
    )

    print(response.usage.prompt_tokens)
    print(response.usage.completion_tokens)
    print(response.usage.total_tokens)

    return response.choices[0].message.content

def chat_completion_stream(messages, model=DEFAULT_MODEL, temperature=0.7, **kwargs):
    response = client.chat.completions.create(
    model=DEFAULT_MODEL,
    messages=messages,
    temperature=temperature,
    stream=True,
    **kwargs,
    )

    responce_content = ""

    for chunk in response:
        chunk_content = chunk.choices[0].delta.content
        if chunk_content is not None:
            print(chunk_content, end="")
            responce_content += chunk_content

    print()

    return responce_content

print(chat_completion(messages, max_completion_tokens=200))