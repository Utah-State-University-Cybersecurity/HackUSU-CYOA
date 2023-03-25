import openai, os, json

openai.api_key = "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"

def iamtheai(prompt):
    message = prompt
    chatlog.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = chatlog)
    reply = response["choices"][0]["message"]["content"]
    chatlog.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
    print()
    print()
    print()
    print()
    

chatlog = []

iamtheai(input('ENTER YOUR USER PROMPT'))

