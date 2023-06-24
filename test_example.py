# test_example.py

import pywinstyles
import customtkinter
from tkinter.colorchooser import askcolor

def change_style(e):
    if e=="Choose Style": return
    toplevel = customtkinter.CTkToplevel(root)
    toplevel.title("")
    toplevel.geometry("500x500+50+50")
    
    pywinstyles.apply_style(toplevel, e)
    
def change_header():
    color = askcolor(title="Choose color")
    if color[1]:
        pywinstyles.change_header_color(root, color=color[1])

def change_title():
    color = askcolor(title="Choose color")
    if color[1]:
        pywinstyles.change_title_color(root, color=color[1])

def change_border():
    color = askcolor(title="Choose color")
    if color[1]:
        pywinstyles.change_border_color(root, color=color[1])
    
root = customtkinter.CTk()
root.geometry("500x200")
root.title("Test")

styles = ["Choose Style", "dark", "mica", "aero", "transparent", "acrylic", "win7",
          "inverse", "popup", "native", "optimised", "light"]

customtkinter.CTkLabel(root, text="pywinstyles test example").pack(pady=5)
customtkinter.CTkOptionMenu(root, values=styles, command=change_style).pack(padx=10, pady=10, fill="x")
customtkinter.CTkButton(root, text="Change Header Color", command=change_header).pack(padx=10, pady=0, fill="x")
customtkinter.CTkButton(root, text="Change Title Color", command=change_title).pack(padx=10, pady=10, fill="x")
customtkinter.CTkButton(root, text="Change Border Color", command=change_border).pack(padx=10, pady=0, fill="x")

root.mainloop()
