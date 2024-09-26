import tkinter as tk
from tkinter import font

# Create the main app window
root = tk.Tk()
root.title("Note App with Formatting")
root.geometry("500x500")

# Create a Text widget for writing notes
text_area = tk.Text(root, wrap='word', undo=True, font=("Arial", 12))
text_area.pack(expand=1, fill='both')

# Define formatting functions
def make_bold():
    current_tags = text_area.tag_names("sel.first")
    if "bold" in current_tags:
        text_area.tag_remove("bold", "sel.first", "sel.last")
    else:
        text_area.tag_add("bold", "sel.first", "sel.last")

    bold_font = font.Font(text_area, text_area.cget("font"))
    bold_font.configure(weight="bold")
    text_area.tag_configure("bold", font=bold_font)

def make_italic():
    current_tags = text_area.tag_names("sel.first")
    if "italic" in current_tags:
        text_area.tag_remove("italic", "sel.first", "sel.last")
    else:
        text_area.tag_add("italic", "sel.first", "sel.last")

    italic_font = font.Font(text_area, text_area.cget("font"))
    italic_font.configure(slant="italic")
    text_area.tag_configure("italic", font=italic_font)

def make_underline():
    current_tags = text_area.tag_names("sel.first")
    if "underline" in current_tags:
        text_area.tag_remove("underline", "sel.first", "sel.last")
    else:
        text_area.tag_add("underline", "sel.first", "sel.last")

    underline_font = font.Font(text_area, text_area.cget("font"))
    underline_font.configure(underline=True)
    text_area.tag_configure("underline", font=underline_font)

# Create a toolbar frame for formatting buttons
toolbar_frame = tk.Frame(root)
toolbar_frame.pack(side='top', fill='x')

# Bold button
bold_button = tk.Button(toolbar_frame, text="Bold", command=make_bold)
bold_button.pack(side='left')

# Italic button
italic_button = tk.Button(toolbar_frame, text="Italic", command=make_italic)
italic_button.pack(side='left')

# Underline button
underline_button = tk.Button(toolbar_frame, text="Underline", command=make_underline)
underline_button.pack(side='left')

# Run the main application loop
root.mainloop()
