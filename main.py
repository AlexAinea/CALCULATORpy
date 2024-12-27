from tkinter import *

# Function to handle button clicks
def append_number(number):
    print(f"Button {number} clicked")  # You can update this to append the number to a display

root = Tk()
root.title("CALCULATOR")

window_width = 400
window_height = 600

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y position for the window to appear at the center
x_pos = (screen_width // 2) - (window_width // 2)
y_pos = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

# Main frame
main_frame = Frame(root, bg="white", width=window_width, height=window_height)
main_frame.pack_propagate(False)  # Prevent the frame from resizing itself
main_frame.pack()

# Output frame
output_frame = Frame(main_frame, bg="black", width=350, height=70)  # Specify both width and height
output_frame.grid(row=0 , column=0, pady=20)

# Input frame
input_frame = Frame(main_frame, bg="black", width=350, height=500)
input_frame.grid_propagate(False)
input_frame.grid(row=1 , column=0)

# Input buttons
"""
buttons = []

for i in range(9):
    button = Button(
        input_frame,
        text=str(i + 1),
        font=("Arial", 24),
        width=5,  # Adjust button width
        height=2,  # Adjust button height
        command=lambda i=i: append_number(i + 1),
    )
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)  # Add padding for spacing
    buttons.append(button)

# Adding a "0" button at the bottom center
zero_button = Button(
    input_frame,
    text="0",
    font=("Arial", 24),
    width=5,
    height=2,
    command=lambda: append_number(0),
)
zero_button.grid(row=3, column=1, padx=5, pady=5)
"""
butt_one = Button(input_frame, text="1", command=lambda: update_to_one(), width=7, height=3)
butt_one.grid(row=0, column=0, padx=8, pady=10)

butt_two = Button(input_frame, text="2", command=lambda: update_to_two(), width=7, height=3)
butt_two.grid(row=0, column=1, padx=8, pady=10)

butt_three = Button(input_frame, text="3", command=lambda: update_to_three(), width=7, height=3)
butt_three.grid(row=0, column=2, padx=8, pady=10)

butt_four = Button(input_frame, text="4", command=lambda: update_to_four(), width=7, height=3)
butt_four.grid(row=1, column=0, padx=8, pady=10)

butt_five = Button(input_frame, text="5", command=lambda: update_to_five(), width=7, height=3)
butt_five.grid(row=1, column=1, padx=8, pady=10)

butt_six = Button(input_frame, text="6", command=lambda: update_to_six(), width=7, height=3)
butt_six.grid(row=1, column=2, padx=8, pady=10)

butt_seven = Button(input_frame, text="7", command=lambda: update_to_seven(), width=7, height=3)
butt_seven.grid(row=2, column=0, padx=8, pady=10)

butt_eight = Button(input_frame, text="8", command=lambda: update_to_eight(), width=7, height=3)
butt_eight.grid(row=2, column=1, padx=8, pady=10)

butt_nine = Button(input_frame, text="9", command=lambda: update_to_nine(), width=7, height=3)
butt_nine.grid(row=2, column=2, padx=8, pady=10)

# Function to update the output display
def update_to_one():
    pass

def update_to_two():
    pass

def update_to_three():
    pass

def update_to_four():
    pass

def update_to_five():
    pass

def update_to_six():
    pass

def update_to_seven():
    pass

def update_to_eight():
    pass

def update_to_nine():
    pass

root.mainloop()
