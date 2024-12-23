from tkinter import *

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

main_frame = Frame(root, bg="white", width=window_width, height=window_height)
main_frame.pack()

root.mainloop()
