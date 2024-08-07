import tkinter as tk
from tkinter import font

def toggle_bold():
    current_font = text_widget.cget("font")
    font_name, font_size, *font_styles = current_font.split()
    if "bold" in font_styles:
        font_styles.remove("bold")
    else:
        font_styles.append("bold")
    new_font = f"{font_name} {font_size} {' '.join(font_styles)}"
    text_widget.config(font=new_font)

def toggle_italic():
    current_font = text_widget.cget("font")
    font_name, font_size, *font_styles = current_font.split()
    if "italic" in font_styles:
        font_styles.remove("italic")
    else:
        font_styles.append("italic")
    new_font = f"{font_name} {font_size} {' '.join(font_styles)}"
    text_widget.config(font=new_font)

def toggle_underline():
    current_font = text_widget.cget("font")
    font_name, font_size, *font_styles = current_font.split()
    if "underline" in font_styles:
        font_styles.remove("underline")
    else:
        font_styles.append("underline")
    new_font = f"{font_name} {font_size} {' '.join(font_styles)}"
    text_widget.config(font=new_font)

app = tk.Tk()
app.title("Python Note App 📝")
app.geometry("600x400")

text_widget = tk.Text(app, wrap='word', font=("Arial", 12))
text_widget.pack(expand=True, fill='both')

toolbar = tk.Frame(app)
toolbar.pack(side='top', fill='x')

bold_button = tk.Button(toolbar, text="Bold", command=toggle_bold)
bold_button.pack(side='left')

italic_button = tk.Button(toolbar, text="Italic", command=toggle_italic)
italic_button.pack(side='left')

underline_button = tk.Button(toolbar, text="Underline", command=toggle_underline)
underline_button.pack(side='left')

app.mainloop()
