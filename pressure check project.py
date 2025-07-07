import tkinter as tk
from tkinter import messagebox

# Function to check "pressure" level
def check_pressure():
    try:
        hours = float(entry_hours.get())
        if hours > 8:
            messagebox.showwarning("Pressure Alert", "⚠️ You are overworked! Take a break.")
        else:
            messagebox.showinfo("Good", "✅ Your working hours are balanced.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for hours.")

# Function to save/submit data (can extend later)
def submit_data():
    name = entry_name.get()
    task = entry_task.get()
    hours = entry_hours.get()
    notes = entry_notes.get("1.0", tk.END)

    print(f"Name: {name}\nTask: {task}\nHours: {hours}\nNotes:\n{notes}")
    messagebox.showinfo("Submitted", "Your data has been recorded.")

# GUI Setup
root = tk.Tk()
root.title("Data Analyst Daily Tracker")
root.geometry("600x500")
root.configure(bg="lightblue")

tk.Label(root, text="Data Analyst Daily Tracker", font=("Arial", 20, "bold"), bg="lightblue").pack(pady=10)

# Form fields
tk.Label(root, text="Name:", font=("Arial", 14), bg="lightblue").pack()
entry_name = tk.Entry(root, font=("Arial", 14), width=40)
entry_name.pack()

tk.Label(root, text="Task Today:", font=("Arial", 14), bg="lightblue").pack()
entry_task = tk.Entry(root, font=("Arial", 14), width=40)
entry_task.pack()

tk.Label(root, text="Hours Worked:", font=("Arial", 14), bg="lightblue").pack()
entry_hours = tk.Entry(root, font=("Arial", 14), width=20)
entry_hours.pack()

tk.Label(root, text="Notes / Summary:", font=("Arial", 14), bg="lightblue").pack()
entry_notes = tk.Text(root, font=("Arial", 12), height=5, width=50)
entry_notes.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="lightblue")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Submit", font=("Arial", 14), command=submit_data, bg="green", fg="white").grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Check Pressure", font=("Arial", 14), command=check_pressure, bg="red", fg="white").grid(row=0, column=1, padx=10)

root.mainloop()
