import openai, os, json


openai.api_key = "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"

# system_msg = input("What type of chatbot would you like to create?\n")
# messages.append({"role": "system", "content": system_msg})

# print("Your new assistant is ready!")
# while input != "quit()":
#     message = input()
#     messages.append({"role": "user", "content": message})
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages)
#     reply = response["choices"][0]["message"]["content"]
#     messages.append({"role": "assistant", "content": reply})
#     print("\n" + reply + "\n")


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

iamtheai(input('ENTER YOUR USER PROMPT'))

iamtheai(input('ENTER YOUR USER PROMPT'))

iamtheai(input('ENTER YOUR USER PROMPT'))

iamtheai(input('ENTER YOUR USER PROMPT'))

iamtheai(input('ENTER YOUR USER PROMPT'))

iamtheai(input('ENTER YOUR USER PROMPT'))

iamtheai(input('ENTER YOUR USER PROMPT'))

iamtheai(input('ENTER YOUR USER PROMPT'))

iamtheai(input('ENTER YOUR USER PROMPT'))
iamtheai(input('ENTER YOUR USER PROMPT'))

iamtheai(input('ENTER YOUR USER PROMPT'))

iamtheai(input('ENTER YOUR USER PROMPT'))

iamtheai(input('ENTER YOUR USER PROMPT'))

iamtheai(input('ENTER YOUR USER PROMPT'))