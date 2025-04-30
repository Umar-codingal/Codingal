import tkinter as tk
from tkinter import messagebox


def calculate_denominations(amount):
    denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    result = {}

    for denom in denominations:
        if amount >= denom:
            count = amount // denom
            result[denom] = count
            amount -= denom * count

    return result


def calculate():
    try:
        amount = int(entry_amount.get())
        if amount <= 0:
            messagebox.showerror("Error", "Please enter a positive amount.")
            return

        denominations = calculate_denominations(amount)
        result_text = "\n".join([f"₹{denom}: {count}" for denom, count in denominations.items()])
        result_label.config(text=f"Denominations:\n{result_text}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer amount.")


# Create the main window
root = tk.Tk()
root.title("Denomination Calculator")
root.geometry("400x300")
root.configure(bg="#f5f5f5")

# Header Label
header_label = tk.Label(root, text="Denomination Calculator", font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#333")
header_label.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#f5f5f5")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter the amount:", font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=0, padx=5, pady=5)
entry_amount = tk.Entry(input_frame, font=("Arial", 12))
entry_amount.grid(row=0, column=1, padx=5, pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", font=("Arial", 12, "bold"), bg="#4caf50", fg="white", command=calculate)
calculate_button.pack(pady=15)

# Result Frame
result_frame = tk.Frame(root, bg="#f5f5f5")
result_frame.pack(pady=10)

result_label = tk.Label(result_frame, text="", font=("Arial", 12), bg="#f5f5f5", justify="left")
result_label.pack()

# Footer Label
footer_label = tk.Label(root, text="Created with ❤️ using Tkinter", font=("Arial", 10), bg="#f5f5f5", fg="#777")
footer_label.pack(side="bottom", pady=10)

# Run the application
root.mainloop()