import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import mysql.connector

# Connect to MySQL
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sumeet123",
        database="outpass"
    )
    cursor = db.cursor()
except mysql.connector.Error as e:
    print("Error connecting to MySQL:", e)
    exit()

# Function to save data
def save_data():
    try:
        # Collect data
        name = name_var.get()
        roll_number = roll_var.get()
        batch = batch_var.get()
        year = year_var.get()
        branch = branch_var.get()
        leave_from = from_date.get()
        leave_to = to_date.get()
        reason = reason_var.get()
        destination = destination_var.get()
        student_phone = student_phone_var.get()
        parent_phone = parent_phone_var.get()
        student_email = student_email_var.get()
        parent_email = parent_email_var.get()
        warden_email = warden_email_var.get()

        # Validate mandatory fields
        if not (name and roll_number and batch and year and branch and leave_from and leave_to and reason and destination):
            messagebox.showerror("Validation Error", "All fields are required!")
            return

        # Insert into database
        query = """INSERT INTO OutpassDetails 
                   (name, roll_number, batch, year, branch, leave_from, leave_to, reason, destination, 
                   student_phone, parent_phone, student_email, parent_email, warden_email) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (name, roll_number, batch, year, branch, leave_from, leave_to, reason, destination,
                  student_phone, parent_phone, student_email, parent_email, warden_email)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Outpass Request Submitted Successfully!")
    except Exception as e:
        messagebox.showerror("Database Error", f"Error: {e}")

# GUI setup
root = tk.Tk()
root.title("College Outpass System")
root.geometry("600x700")

# Variables
name_var = tk.StringVar()
roll_var = tk.StringVar()
batch_var = tk.StringVar()
year_var = tk.StringVar()
branch_var = tk.StringVar()
reason_var = tk.StringVar()
destination_var = tk.StringVar()
student_phone_var = tk.StringVar()
parent_phone_var = tk.StringVar()
student_email_var = tk.StringVar()
parent_email_var = tk.StringVar()
warden_email_var = tk.StringVar()

# Fields
tk.Label(root, text="College Outpass System", font=("Arial", 18)).pack(pady=10)

fields_frame = tk.Frame(root)
fields_frame.pack(pady=10)

tk.Label(fields_frame, text="Name:").grid(row=0, column=0, sticky="w")
tk.Entry(fields_frame, textvariable=name_var, width=40).grid(row=0, column=1, pady=5)

tk.Label(fields_frame, text="Roll Number:").grid(row=1, column=0, sticky="w")
tk.Entry(fields_frame, textvariable=roll_var, width=40).grid(row=1, column=1, pady=5)

tk.Label(fields_frame, text="Batch:").grid(row=2, column=0, sticky="w")
tk.Entry(fields_frame, textvariable=batch_var, width=40).grid(row=2, column=1, pady=5)

tk.Label(fields_frame, text="Year:").grid(row=3, column=0, sticky="w")
ttk.Combobox(fields_frame, textvariable=year_var, values=["1st", "2nd", "3rd", "4th"], width=38).grid(row=3, column=1, pady=5)

tk.Label(fields_frame, text="Branch:").grid(row=4, column=0, sticky="w")
ttk.Combobox(fields_frame, textvariable=branch_var, values=["CSE", "IT", "BT", "BI", "BSc", "MSc", "MTech", "BBA"], width=38).grid(row=4, column=1, pady=5)

tk.Label(fields_frame, text="Leave From:").grid(row=5, column=0, sticky="w")
from_date = DateEntry(fields_frame, width=36, date_pattern="yyyy-mm-dd")
from_date.grid(row=5, column=1, pady=5)

tk.Label(fields_frame, text="Leave To:").grid(row=6, column=0, sticky="w")
to_date = DateEntry(fields_frame, width=36, date_pattern="yyyy-mm-dd")
to_date.grid(row=6, column=1, pady=5)

tk.Label(fields_frame, text="Reason:").grid(row=7, column=0, sticky="w")
tk.Entry(fields_frame, textvariable=reason_var, width=40).grid(row=7, column=1, pady=5)

tk.Label(fields_frame, text="Destination:").grid(row=8, column=0, sticky="w")
tk.Entry(fields_frame, textvariable=destination_var, width=40).grid(row=8, column=1, pady=5)

tk.Label(fields_frame, text="Student Phone:").grid(row=9, column=0, sticky="w")
tk.Entry(fields_frame, textvariable=student_phone_var, width=40).grid(row=9, column=1, pady=5)

tk.Label(fields_frame, text="Parent Phone:").grid(row=10, column=0, sticky="w")
tk.Entry(fields_frame, textvariable=parent_phone_var, width=40).grid(row=10, column=1, pady=5)

tk.Label(fields_frame, text="Student Email:").grid(row=11, column=0, sticky="w")
tk.Entry(fields_frame, textvariable=student_email_var, width=40).grid(row=11, column=1, pady=5)

tk.Label(fields_frame, text="Parent Email:").grid(row=12, column=0, sticky="w")
tk.Entry(fields_frame, textvariable=parent_email_var, width=40).grid(row=12, column=1, pady=5)

tk.Label(fields_frame, text="Warden Email:").grid(row=13, column=0, sticky="w")
tk.Entry(fields_frame, textvariable=warden_email_var, width=40).grid(row=13, column=1, pady=5)

# Submit Button
tk.Button(root, text="Submit", command=save_data, bg="green", fg="white").pack(pady=20)

# Run the application
root.mainloop()
