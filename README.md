# Overview
The goal of this project was to create a Choose Your Own Adventure style game powered by OpenAI's ChatGPT-3.5-turbo  

We did this by calling the API for GPT with a very specific prompt, parsing the results, and displaying it all in a tkinter window.  

**We're honored to have won the beginner award for AI and Machine Learning at [HackUSU](https://www.hackusu.com/) 2023.**

# Video Demos
| Hackathon | Current |
|---|---|
| [![Hackathon Demo](http://img.youtube.com/vi/Z_0t5PnRWzw/0.jpg)](http://www.youtube.com/watch?v=Z_0t5PnRWzw "GPT Powered Choose-Your-Own-Adventure -- HackUSU 2023") | Video coming soon! |

# Usage
## Prerequisites
In order to run this program you'll need 
* An API key from openAI
* Python 3.7 or higher
* OpenAI library

## Setup
1. Install the OpenAI Library for python with ```pip install openai```
1. Download ```main.py```
2. Repleace the API key with your own OpenAI API key

## Running the program
1. Run ```python main.py``` in the terminal or your favorite python-supporting IDE  
2. The program will launch a tkinter window, all further instructions refer to the window 
3. Select the length of your adventure (Short-10 turns, Medium-15 turns, or Long-25 turns) and then click the "Select Length" button
4. The AI will then generate 5 characters to choose from, select the button corresponding to the character you'd like to be and click "Select Character"
5. The AI will then start the story and give you two options, select the option you'd like to continue with
6. Repeat the previous step until the story is over
7. Select "Close Window" to end the experience
8. To play again, repeat instructions

# Stretch Goals
Features we wanted to include but weren't able to due to the time constraint  
These features may get added in the future  
- [ ] generate dalle images for each scene
- [ ] save story with images and text
- [x] option save story text to file
- [ ] ChatGPT api call async so loading symbol can be displayed to user instead of the app going unresponsive
- [ ] ability to go back and replay scenarios (select different option)
- [x] "Play Again" button
- [ ] Refactor code to better conform to python coding standards 

# Contributors
|Name | Github | Linkedin | 
|---|---|---|
| Carter Watson      | [Github](https://github.com/cartwatson)      | [LinkedIn](https://www.linkedin.com/in/cartwatson)                    |
| Chandler McClellan | [Github](https://github.com/spacemagicmango) | [LinkedIn](https://www.linkedin.com/in/chandler-mcclellan-765a85261/) |
| Joseph Johnson     | [Github](https://github.com/jpjohnson-31337) | [LinkedIn](https://www.linkedin.com/in/joseph-johnson-52bb011b0/)     |  
