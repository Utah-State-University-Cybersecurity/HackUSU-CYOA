import os, openai, time, base64

openai.api_key = "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"

# openai.api_key = os.getenv("OPENAI_API_KEY")
photo = openai.Image.create(
  prompt="Zephyr and his ally barely make it out alive, but the enemy's plan is now in motion. With limited time, they must rally their allies and prepare for the impending attack. Zephyr is determined to make up for his mistake and stop the enemy's nefarious plan.",
  n=1,
  size="1024x1024",
  response_format="b64_json")



for i in range(0, len(photo['data'])):
    b64 = photo['data'][i]['b64_json']
    filename = f'image_{int(time.time())}_{i}.png'
    print('Saving file ' + filename)
    with open(filename, 'wb') as f:
        f.write(base64.urlsafe_b64decode(b64))
        
        
'''
openai.Image.create_edit(
  image=open("otter.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="A cute baby sea otter wearing a beret",
  n=1,
  size="1024x1024")
  
'''

# print(photo)