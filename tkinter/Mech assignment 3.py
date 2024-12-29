import tkinter as tk
from tkinter import messagebox
import math
root = tk.Tk()
root.geometry("1080x600")
root.resizable(False, False)
root.title("Mechanics Assignment")
image = tk.PhotoImage(file='Screenshot(7).png')
image_resized = image.subsample(4, 4)
label1 = tk.Label(root, image=image_resized)
label1.image = image_resized
label1.place(x=30, y=120)
def submit():
    try:
        F1 = float(e1.get())
        F2 = float(e2.get())
        if F1<=0 or F2<=0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for F1 and F2.")
        return
    Ax=F2/2
    Ay=F1+(F2*0.866)-3.6
    Ra=math.sqrt((Ax)**2+(Ay)**2)
    M=abs(83.2-(18*F2*0.866))
    label5.config(text=f"Ans: Resultant force at A, Ra = {round(Ra, 3)} kN")
    label6.config(text=f" Magnitude of Moment, M ={round(M,3)} kN-m")
label2 = tk.Label(root, text="5/122) Give input for forces acting at A and at 30 degrees from y-axis as shown in question.",font=
                  ('Comic Sans MS', 16), fg="yellow", bg="black")
label2.place(x=10, y=10)
c1 = tk.Label(root, text="Value of F1(kN):", font=('Arial', 20), fg="white", bg="black")
c1.place(x=580, y=150)
e1 = tk.Entry(root, font=('Helvetica', 20), bg="white", fg="black", width=15)
e1.place(x=790, y=150)
c2 = tk.Label(root, text="Value of F2(kN):", font=('Arial', 20), fg="white", bg="black")
c2.place(x=580, y=200)
e2 = tk.Entry(root, font=('Helvetica', 20), bg="white", fg="black", width=15)
e2.place(x=790, y=200)
button = tk.Button(root, text="Submit", font=('Arial', 18), height=2, width=10, command=submit, bg="green", fg="black")
button.place(x=750, y=360)
label5 = tk.Label(root, text="", font=('Arial', 20), fg="white", bg="black")
label5.place(x=20, y=460)
label6 = tk.Label(root, text="", font=('Arial', 20), fg="white", bg="black")
label6.place(x=20, y=500)
root.mainloop()
