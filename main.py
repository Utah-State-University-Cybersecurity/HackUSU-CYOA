import tkinter as tk
import random
import time
import openai # pip install openai

# how many steps in the story
STEPS = 10
step = -1 # start at -1 for menu screen
op1label_name = ""
op2label_name = ""
# track items on screen with frames 
frames = []

# AI----------------------------------
openai.api_key = "YOUR_API_KEY_HERE"

chatlog = []
def query(prompt):
    message = prompt
    chatlog.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = chatlog)
    reply = response["choices"][0]["message"]["content"]
    chatlog.append({"role": "assistant", "content": reply})
    return reply

def parse(response):
    # cover beginning and end edge cases    
    if (step == -1 or step == STEPS):
        response = response.replace("\n\n", "\n")
        return [response, "", ""]
    
    op1index = response.find("Option 1: ")
    op2index = response.find("Option 2")

    # cut string
    summary = response[:op1index]
    option1 = response[op1index+10:op2index].replace("\n", "")
    option2 = response[op2index+10:].replace("\n", "")

    return [summary, option1, option2]

def create_query(option):
    global step
    global STEPS

    if (step == -1):
        return "Make up 5 random video game characters."
    # create character
    if (step == 0):
        return f"Begin writing a story involving hero {option}. Give the reader two options to choose from to continue the story."

    query = f"Do option {option}, "
    # continue story
    if (STEPS != step):
        query += "keep the story going"
    else: # end of story
        # determine win or loss
        temp = "win" if (0.75 < random.random()) else "Lose"
        query += f"finsh the story, having the hero {temp}"

    # if starting the last third of the story, make the boss
    if ((STEPS - step) == STEPS // 3):
        query += "make up a video game boss."

    # if not at the end, give more options
    if (STEPS != step):
        query += " Give the player 2 new options for how the story goes."
    
    return query

# Tkinter-----------------------------
def update(option):
    global step
    global STEPS
    global op1label_name
    global op2label_name
    # check for menu screen
    if (step == -1):
        if (option == "garbage"):
            story.config(text="Welcome to ChatGPT Choose Your Own Adventure.\nSelect your adventure length below!\nSelect a Length!")
            return
        elif (option == "Short"):  STEPS = 10
        elif (option == "Medium"): STEPS = 15
        elif (option == "Long"):   STEPS = 25

    # check to make sure character was selected
    if (step == 0):
        if (option == 0):
            t = story.cget('text')
            if (not "\nSelect a Character!" in t):
                t = story.cget('text') + "\nSelect a Character!"
            story.config(text=t)
            return
    
    # create query
    results = parse(query(create_query(option)))
    # update num of steps
    step += 1
    gameloop()
    # update window
    story.config(text=results[0])
    # not at beginning or end, update option text
    if (step != -1 and step != STEPS):
        for frame in frames:
            for widget in frame.winfo_children():
                if widget.winfo_name() == "op1":
                    widget.config(text=results[1])
                if widget.winfo_name() == "op2":
                    widget.config(text=results[2])

def gameloop():
    global step
    global STEPS
    global op1label_name
    global op2label_name
    remove_buttons()
    # menu screen
    if (step == -1):
        story.config(text="Welcome to ChatGPT Choose Your Own Adventure.\nSelect your adventure length below!")
        # select length
        selected_value = tk.StringVar()
        selected_value.set("garbage")
        ranges = ["Short", "Medium", "Long"]
        frame = tk.Frame(root)
        frame.grid(row=2, column=0, columnspan=len(ranges), sticky=tk.W)
        frames.append(frame)
        for i in range(len(ranges)):
            button = tk.Radiobutton(frame, text=ranges[i], variable=selected_value, value=ranges[i])
            button.pack(side='left')
        # button to confirm length
        frame2 = tk.Frame(root)
        frame2.grid(row=3, column=0, columnspan=1, sticky=tk.W, padx=5, pady=5)
        frames.append(frame2)
        selectLengthButton = tk.Button(frame2, text="Select Length", command=lambda: update(selected_value.get()))
        selectLengthButton.pack(side='left')

    # picking character
    elif (step == 0):
        # setup var for selecting character
        selected_value = tk.StringVar()
        selected_value.set(0)
        # create radio buttons for character selection
        frame = tk.Frame(root)
        frame.grid(row=2, column=0, columnspan=3, sticky="w", padx=5, pady=5)
        for i in range(1, 6):
            button = tk.Radiobutton(frame, text=str(i), variable=selected_value, value=i)
            button.pack(side='left')
        # button for confirming character selection
        frame2 = tk.Frame(root)
        frame2.grid(row=3, column=0, columnspan=1, sticky=tk.W, padx=5, pady=5)
        frames.append(frame2)
        selectCharButton = tk.Button(frame2, text="Select Character", command=lambda: update(selected_value.get()))
        selectCharButton.pack(side='left')

    # end of game
    elif (step == STEPS):
        # create frame
        frame1 = tk.Frame(root)
        frame1.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        frames.append(frame1)
        frame2 = tk.Frame(root)
        frame2.grid(row=3, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        frames.append(frame2)
        # button to save comic strip
        save = tk.Button(frame1, text="Save Adventure", command=save_comic, padx=5)
        save.pack(side='left')
        # button to close window
        reset = tk.Button(frame1, text="Play Again", command=reset_game, padx=5)
        reset.pack(side='left')
        close = tk.Button(frame2, text="Close Window", command=close_window, padx=5)
        close.pack(side='left')

    # regular turn
    else:
        # create frames
        op1frame = tk.Frame(root)
        op1frame.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        frames.append(op1frame)
        # option 1
        option1 = tk.Button(op1frame, text="Option 1", command=lambda: update(1))
        op1label = tk.Label(op1frame, text="op1text", wraplength=500, justify='left', name="op1")
        # option 2
        op2frame = tk.Frame(root)
        op2frame.grid(row=3, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        frames.append(op2frame)
        option2 = tk.Button(op2frame, text="Option 2", command=lambda: update(2))
        op2label = tk.Label(op2frame, text="op2text", wraplength=500, justify='left', name="op2")
        # place items on window
        option1.pack(side='left', anchor="nw")
        op1label.pack(side='left', anchor="nw")
        option2.pack(side='left', anchor="nw")
        op2label.pack(side='left', anchor="nw")

def close_window():
    root.destroy()

def remove_buttons():
    for frame in frames:
        frame.destroy()
    frames.clear()

def save_comic():
    try:
        # handle saving the file
        fileName = "adventure_" + str(time.time()) + ".txt"
        file = open(fileName, "w")
        for i in range(len(chatlog)):
            if chatlog[i]["role"] == "assistant":
                file.write(chatlog[i]["content"])
        file.close()
        # give user update on save status
        t = story.cget('text')
        if (not "\nStory Saved!" in t):
            t = story.cget('text') + "\nStory Saved!\nAdventure saved as: " + fileName
        story.config(text=t)
    except:
        t = story.cget('text') + "\nError saving file! Try again!"
        story.config(text=t)

def reset_game():
    global step
    remove_buttons()
    step = -1
    chatlog.clear()
    gameloop()

# create window
root = tk.Tk()
root.title("HUSU-CYOA")

# generate story image and text
# TODO: Story name
# TODO: Story image
story = tk.Label(root, text="Hello World!", anchor="w")
story.config(wraplength=500, justify='left')
story.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

# init call
gameloop()

# window loop
root.geometry("600x400")
root.mainloop()
