import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry("1480x1000")
root.resizable(False, False)
root.title("Mechanics Assignment")
image = tk.PhotoImage(file='Screenshot(5).png')
image_resized = image.subsample(3, 3)
label1 = tk.Label(root, image=image_resized)
label1.image = image_resized
label1.place(x=30, y=120)
def submit():
    try:
        F = float(e1.get())
        M = float(e2.get())
        if F<=0 or M <= 0:
            raise ValueError
    except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values for F and M0.")
            return
    R = F*0.9659
    M0 = M-(F*0.9659*40)+(F*0.2588*10)
    d = M0/R
    y_intercept = -d
    label5.config(text=f"Ans:y_intercept of line of action of single equivalent force, y_intercept = {round(y_intercept, 3)} mm")
label2 = tk.Label(root, text="2/76)  Enter the value of Force exerted at A and the value of M0 exerted by the hidden torsional spring.",
                  font=('Comic Sans MS', 16), fg="yellow", bg="black")
label2.place(x=10, y=10)
c1 = tk.Label(root, text="Force at A(N):", font=('Arial', 20), fg="white", bg="black")
c1.place(x=580, y=150)
e1 = tk.Entry(root, font=('Helvetica', 20), bg="white", fg="black", width=15)
e1.place(x=790, y=150)
c2 = tk.Label(root, text="Value of M0(N-mm):", font=('Arial', 20), fg="white", bg="black")
c2.place(x=510, y=200)
e2 = tk.Entry(root, font=('Helvetica', 20), bg="white", fg="black", width=15)
e2.place(x=790, y=200)
button = tk.Button(root, text="Submit", font=('Arial', 18), height=2, width=10, command=submit, bg="green", fg="black")
button.place(x=750, y=360)
label5 = tk.Label(root, text="", font=('Arial', 20), fg="white", bg="black")
label5.place(x=20, y=560)
root.mainloop()
