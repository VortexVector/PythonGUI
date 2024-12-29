import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry("1080x600")
root.resizable(False, False)
root.title("Mechanics Assignment")
image = tk.PhotoImage(file='Screenshot (8).png')
image_resized = image.subsample(3, 3)
label1 = tk.Label(root, image=image_resized)
label1.image = image_resized
label1.place(x=30, y=120)
def submit():
  try:
    load_C = float(e1.get())
    load_D = float(e2.get())
    load_G = float(e3.get())
    if load_C <= 0 or load_D <= 0 or load_G <= 0:
      raise ValueError("Values must be greater than 0")
  except ValueError as ve:
    messagebox.showerror("Invalid Input", f"Please enter valid numeric values for load_C, load_D, load_G")
    return
  F_BG = load_G / (2 * 0.654)
  F_BC = (3 / 2) * (load_G) / 0.866
  label5.config(text=f"Ans: Force at joint BG, F_BG  = {round(F_BG, 3)} T kN")
  label6.config(text=f"Force at joint BC, F_BC = {round(F_BC, 3)} C kN")
label2 = tk.Label(root, text="Enter values for forces at junctions C,D,G.",
                  font=('Comic Sans MS', 16), fg="yellow", bg="black")
label2.place(x=10, y=10)
c1 = tk.Label(root, text="load_C(kN):", font=('Arial', 20), fg="white", bg="black")
c1.place(x=565, y=150)
e1 = tk.Entry(root, font=('Helvetica', 20), bg="white", fg="black", width=15)
e1.place(x=790, y=150)
c2 = tk.Label(root, text="load_D(kN):", font=('Arial', 20), fg="white", bg="black")
c2.place(x=565, y=200)
e2 = tk.Entry(root, font=('Helvetica', 20), bg="white", fg="black", width=15)
e2.place(x=790, y=200)
c3 = tk.Label(root, text="load_G(kN):", font=('Arial', 20), fg="white", bg="black")
c3.place(x=565, y=250)
e3 = tk.Entry(root, font=('Helvetica', 20), bg="white", fg="black", width=15)
e3.place(x=790, y=250)
button = tk.Button(root, text="Submit", font=('Arial', 18), height=2, width=10, command=submit, bg="green", fg="black")
button.place(x=750, y=360)
label5 = tk.Label(root, text="", font=('Arial', 20), fg="white", bg="black")
label5.place(x=20, y=460)
label6 = tk.Label(root, text="", font=('Arial', 20), fg="white", bg="black")
label6.place(x=20, y=500)
root.mainloop()
