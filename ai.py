import dashscope
from dashscope import MultiModalConversation
import json

dashscope.api_key = 'sk-47407d15aec84552bbc717d5b8a83886'

image_path = 'mountain.jpg'

question = '这张图片里有什么？'

test = 'this is change 2'

response = MultiModalConversation.call(
    model='qwen-vl-plus',
    messages=[
        {
            'role': 'user',
            'content': [
                {'image': image_path},
                {'text': question}
            ]
        }
    ],
    result_format='message'
)

print(response['output']['choices'][0]['message']['content'][0]['text'])