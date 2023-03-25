import openai, os, json


openai.api_key = "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"

def query_gpt(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

prompt = "Hello, how are you?"
response = query_gpt(prompt)
print(response)


# Set up the OpenAI API client
openai.api_key = "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"

# Set the prompt for DALL-E to generate images from
prompt = "a bird with the head of a lion and the body of a snake"

# Set the parameters for the DALL-E image generation
model = "image-alpha-001"
num_images = 1

# Generate the image using DALL-E
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=1024,
    n=model,
    stop=None,
    temperature=0.5,
    frequency_penalty=0,
    presence_penalty=0,
)

# Parse the response to get the generated image(s)
output_data = response.choices[0].text
output_json = json.loads(output_data)
output_images = output_json["data"]

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

'''Lets start this programming right now'''

input('Welcome to your SuperStory! \n\n-Press any key to continue-')