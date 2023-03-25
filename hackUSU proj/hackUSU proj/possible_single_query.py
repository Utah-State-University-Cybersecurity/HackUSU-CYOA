import openai, os, json


openai.api_key = "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"

def asktheapi(prompt):
    prompt = prompt
    prompt = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    print(prompt.choices[0].message.content)
    print()