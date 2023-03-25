import tkinter as tk
import random

# how many steps in the story
STEPS = 10
step = 0

# define updates
def create_query(option):
    query = f"Do option {option}, "
    # continue story
    if (STEPS != step):
        query += "keep the story going"
    else: # end of story
        # determine win or loss
        if (0.75 < random.random()):
            temp = "win"
        else:
            temp = "lose"
        query += f"finsh the story, having the hero {temp}"

    # if starting the last third of the story, make the boss
    if ((STEPS - step) == STEPS // 3):
        query += "make up a video game boss."

    # if not at the end, give more options
    if (STEPS != step):
        query += " Give the player 2 new options for how the story goes."
    
    print("Query: " + query) # DEBUG
    return query

def update(option):
    # create query
    query = create_query(option)
    # GPT Query here
    results = ""
    # parse results
    story = "story"
    op1text = "option1"
    op2text = "option2"
    # update window
    story.config(text=story)
    op1label.config(text=op1text)
    op2label.config(text=op2text)
    # update num of steps
    step += 1

def close_window():
    root.destroy()
    

# create window
root = tk.Tk()
root.title("HUSU-CYOA")

# generate story image and text
# TODO: story image
story = tk.Label(root, text="Hello World!")
story.grid  (row=1, column=0, sticky=tk.W, padx=5, pady=5)

# picking character
if (step == 0):
    # create radio buttons for character selection
    pass

# end of game
elif (step == STEPS):
    # button to close window/accept results
    close = tk.Button(root, text="Close Window", command=close_window)
    pass

# regular turn
else:
    # option 1------
    option1 = tk.Button(root, text="Option 1", command=lambda: update(1))
    op1label = tk.Label(root, text="")
    # option 2------
    option2 = tk.Button(root, text="Option 2", command=lambda: update(2))
    op2label = tk.Label(root, text="")
    # place items on window
    option1.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
    op1label.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
    option2.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
    op2label.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

# window loop
root.geometry("600x400")
root.mainloop()
