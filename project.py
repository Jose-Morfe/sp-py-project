from turtle import*

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Text Adventure")

# Create a writer turtle for text and buttons
writer = Turtle()
writer.hideturtle()
writer.penup()
writer.color("white")

# 1. Draw the Story Text
writer.goto(-350, 350)
story_text = (
    "You enter the store. It is dark, abandoned, and silent.\n"
    "Yesterday it was full of life; now it's a hollow shell.\n\n"
    "What do you do?"
)
screen.bgpic(r"DarkStore.gif")
writer.write(story_text, font=("Arial", 16, "normal"))

# 2. Define Button Coordinates (X_min, X_max, Y_min, Y_max)
# Button 1: Leave the store
btn1_x, btn1_y = 300, 50
# Button 2: Stay and explore
btn2_x, btn2_y = 300, -20

# 3. Draw the Interactive Options
writer.goto(btn1_x, btn1_y)
writer.write("Leave the store", font=("Arial", 14, "bold"))

writer.goto(btn2_x, btn2_y)
writer.write("Stay and explore", font=("Arial", 14, "bold"))

# 4. Define Action Functions
def leave_action():
    writer.clear()
    writer.goto(300, 0)
    writer.write("You turn back and walk out into the night then you feel like something is behind you and your neck snaps... You Died", font=("Arial", 18, "italic"))

def explore_action():
    writer.clear()
    writer.goto(300, 0)
    writer.write("You step deeper into the dark, silent aisles...", font=("Arial", 18, "italic"))

    

# 5. Handle the Click Detection
def handle_click(x, y):
    # Check if click is near "Leave the store" text area
    if (btn1_x <= x <= btn1_x + 150) and (btn1_y <= y <= btn1_y + 25):
        leave_action()
        
    # Check if click is near "Stay and explore" text area
    elif (btn2_x <= x <= btn2_x + 150) and (btn2_y <= y <= btn2_y + 25):
        explore_action()
        screen.bgpic(r"BLOODYFLOOR.gif")


# 6. Listen for Clicks
screen.onscreenclick(handle_click)
screen.mainloop()
