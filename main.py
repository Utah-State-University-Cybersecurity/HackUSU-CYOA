import tkinter as tk
import random
import openai

# how many steps in the story
# track items on screen with buttons 
global STEPS
global step
global buttons
STEPS = 10
step = -1 # start at -1 for menu screen
buttons = []

# AI----------------------------------
openai.api_key = "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"

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
    
    op1index = response.find("Option 1")
    op2index = response.find("Option 2")

    # cut string
    summary = response[:op1index]
    option1 = response[op1index+9:op2index].replace("\n", "")
    option2 = response[op2index+9:].replace("\n", "")

    return [summary, option1, option2]

# Tkinter-----------------------------
# define updates
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

def update(option):
    global STEPS
    global step
    global buttons
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
    # not at beginning or end
    if (step != -1 and step != STEPS):
        buttons[2].config(text=results[1])
        buttons[3].config(text=results[2])

def gameloop():
    global STEPS
    global step
    global buttons
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
        for i in range(len(ranges)):
            button = tk.Radiobutton(frame, text=ranges[i], variable=selected_value, value=ranges[i])
            button.pack(side='left')
            buttons.append(button)
        # button to confirm length
        selectLengthButton = tk.Button(root, text="Select Length", command=lambda: update(selected_value.get()))
        selectLengthButton.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        buttons.append(selectLengthButton)

    # picking character
    elif (step == 0):
        # setup var for selecting character
        selected_value = tk.IntVar()
        selected_value.set(0)
        # create radio buttons for character selection
        frame = tk.Frame(root)
        frame.grid(row=2, column=0, columnspan=5, sticky=tk.W)
        for i in range(1, 6):
            button = tk.Radiobutton(frame, text=str(i), variable=selected_value, value=str(i))
            button.pack(side='left')
            buttons.append(button)
        # button for confirming character selection
        selectCharButton = tk.Button(root, text="Select Character", command=lambda: update(selected_value.get()))
        selectCharButton.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        buttons.append(selectCharButton)

    # end of game
    elif (step == STEPS):
        # create frame
        frame1 = tk.Frame(root)
        frame1.grid(row=2, column=0, columnspan=2, sticky="w")
        # button to save comic strip
        # TODO: implement
        # save = tk.Button(frame1, text="Save Comic", command=save_comic)
        # save.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        # button to close window
        close = tk.Button(frame1, text="Close Window", command=close_window)
        close.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

    # regular turn
    else:
        # create frames
        frame1 = tk.Frame(root)
        frame1.grid(row=2, column=0, columnspan=2, sticky="w")
        frame2 = tk.Frame(root)
        frame2.grid(row=3, column=0, columnspan=2, sticky="w")
        # option 1
        option1 = tk.Button(frame1, text="Option 1", command=lambda: update(1))
        op1label = tk.Label(frame1, text="op1text")
        # option 2
        option2 = tk.Button(frame2, text="Option 2", command=lambda: update(2))
        op2label = tk.Label(frame2, text="op2text")
        # place items on window
        option1.pack(side='left', anchor="nw")
        op1label.config(wraplength=500, justify='left')
        op1label.pack(side='left', anchor="nw")
        option2.pack(side='left', anchor="nw")
        op2label.config(wraplength=500, justify='left')
        op2label.pack(side='left', anchor="nw")

        # add buttons to what's on screen
        buttons.append(option1)
        buttons.append(option2)
        buttons.append(op1label)
        buttons.append(op2label)

def close_window():
    root.destroy()

def remove_buttons():
    for button in buttons:
        button.grid_forget()
        button.destroy()
    buttons.clear()

def save_comic():
    # TODO: implement
    pass

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
