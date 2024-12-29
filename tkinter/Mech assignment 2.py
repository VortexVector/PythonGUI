import tkinter as tk
from tkinter import messagebox, Frame
import math
root = tk.Tk()
root.geometry("1080x600")
root.resizable(False, False)
root.title("Mechanics Assignment")
image = tk.PhotoImage(file='Screenshot (3).png')
image_resized = image.subsample(3, 3)
label1 = tk.Label(root, image=image_resized)
label1.image = image_resized
label1.place(x=30, y=120)
def submit():
    try:
        mass_of_man = float(e1.get())
        mass_of_ladder = float(e2.get())
        length_of_ladder = float(e3.get())
        coefficient_of_static_friction = float(e4.get())
        if mass_of_man<=0 or mass_of_ladder<=0 or length_of_ladder<=0 or coefficient_of_static_friction<0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for Mass_of_man, Mass_of_ladder,"
                                              "length_of_ladder and coefficient_of_static_friction.")
        return
    na=(mass_of_man+mass_of_ladder)*9.81
    alfa=math.sqrt((length_of_ladder)**2-(1.5)**2)
    x = ((coefficient_of_static_friction * na * (alfa)) - (mass_of_ladder * 9.81 * 0.75)) / (mass_of_man * 9.81)
    s=(length_of_ladder/1.5)*x
    if s<0:
        s=0
    label5.config(text=f"Ans: Distance of man from the ground, s = {round(s, 3)} m")
label2 = tk.Label(root, text="6/33)  Give input for Mass of man,Mass of ladder,length of ladder,coefficient of static friction.",
                  font=('Comic Sans MS', 16), fg="yellow", bg="black")
label2.place(x=10, y=10)
c1 = tk.Label(root, text="Mass of man(kg):", font=('Arial', 20), fg="white", bg="black")
c1.place(x=450, y=150)
e1 = tk.Entry(root, font=('Helvetica', 20), bg="white", fg="black", width=15)
e1.place(x=790, y=150)
c2 = tk.Label(root, text="Mass of ladder(kg):", font=('Arial', 20), fg="white", bg="black")
c2.place(x=450, y=200)
e2 = tk.Entry(root, font=('Helvetica', 20), bg="white", fg="black", width=15)
e2.place(x=790, y=200)
c3 = tk.Label(root, text="Length of Ladder(m):", font=('Arial', 20), fg="white", bg="black")
c3.place(x=450, y=250)
e3 = tk.Entry(root, font=('Helvetica', 20), bg="white", fg="black", width=15)
e3.place(x=790, y=250)
c4 = tk.Label(root, text="Coefficient of static friction:", font=('Arial',20), fg="white", bg="black")
c4.place(x=450, y=300)
e4 = tk.Entry(root, font=('Helvetica', 20), bg="white", fg="black", width=15)
e4.place(x=790, y=300)
button = tk.Button(root, text="Submit", font=('Arial', 18), height=2, width=10, command=submit, bg="green", fg="black")
button.place(x=670, y=360)
label5 = tk.Label(root, text="", font=('Arial', 20), fg="white", bg="black")
label5.place(x=20, y=460)
root.mainloop()