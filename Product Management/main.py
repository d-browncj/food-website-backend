import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
import os

FILENAME = "products.csv"
ICON_PATH = r"C:\Users\sohai\Downloads\foodie-master\foodie-master\assets\images\emsi-logo-removebg-preview.ico"

def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                tree.insert("", "end", values=row)

def save_data():
    with open(FILENAME, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row_id in tree.get_children():
            row = tree.item(row_id)['values']
            writer.writerow(row)

def add_entry():
    def save_new_entry():
        nom = nom_entry.get()
        prix = prix_entry.get()
        date = date_entry.get()
        quantiter = quantiter_entry.get()
        tree.insert("", "end", values=(nom, prix, date, quantiter))
        save_data()
        add_dialog.destroy()

    add_dialog = tk.Toplevel(root)
    add_dialog.title("Ajouter un produit")
    add_dialog.iconbitmap(ICON_PATH)  # Set the icon for the add dialog

    tk.Label(add_dialog, text="Nom", bg="#e0f7e0").grid(row=0, column=0, padx=10, pady=5)
    nom_entry = tk.Entry(add_dialog)
    nom_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(add_dialog, text="Prix", bg="#e0f7e0").grid(row=1, column=0, padx=10, pady=5)
    prix_entry = tk.Entry(add_dialog)
    prix_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(add_dialog, text="Date", bg="#e0f7e0").grid(row=2, column=0, padx=10, pady=5)
    date_entry = tk.Entry(add_dialog)
    date_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(add_dialog, text="Quantiter", bg="#e0f7e0").grid(row=3, column=0, padx=10, pady=5)
    quantiter_entry = tk.Entry(add_dialog)
    quantiter_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(add_dialog, text="Save", command=save_new_entry, bg="#28a745", fg="white").grid(row=4, columnspan=2, pady=10)

def modify_entry():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "No item selected to modify")
        return

    def save_modified_entry():
        nom = nom_entry.get()
        prix = prix_entry.get()
        date = date_entry.get()
        quantiter = quantiter_entry.get()
        tree.item(selected_item, values=(nom, prix, date, quantiter))
        save_data()
        modify_dialog.destroy()

    item_values = tree.item(selected_item, "values")
    
    modify_dialog = tk.Toplevel(root)
    modify_dialog.title("Modifier le produit")
    modify_dialog.iconbitmap(ICON_PATH)  # Set the icon for the modify dialog

    tk.Label(modify_dialog, text="Nom", bg="#e0f7e0").grid(row=0, column=0, padx=10, pady=5)
    nom_entry = tk.Entry(modify_dialog)
    nom_entry.insert(0, item_values[0])
    nom_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(modify_dialog, text="Prix", bg="#e0f7e0").grid(row=1, column=0, padx=10, pady=5)
    prix_entry = tk.Entry(modify_dialog)
    prix_entry.insert(0, item_values[1])
    prix_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(modify_dialog, text="Date", bg="#e0f7e0").grid(row=2, column=0, padx=10, pady=5)
    date_entry = tk.Entry(modify_dialog)
    date_entry.insert(0, item_values[2])
    date_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(modify_dialog, text="Quantiter", bg="#e0f7e0").grid(row=3, column=0, padx=10, pady=5)
    quantiter_entry = tk.Entry(modify_dialog)
    quantiter_entry.insert(0, item_values[3])
    quantiter_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(modify_dialog, text="Save", command=save_modified_entry, bg="#28a745", fg="white").grid(row=4, columnspan=2, pady=10)

def delete_entry():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
        save_data()
    else:
        messagebox.showwarning("Warning", "No item selected to delete")

# Create main window
root = tk.Tk()
root.title("Product Management")

# Set window dimensions
root.geometry("600x400")

# Set window icon
root.iconbitmap(ICON_PATH)

# Configure style
style = ttk.Style()
style.theme_use('clam')  # Set a theme that is easy to customize
style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background="#28a745", foreground="white")
style.configure("Treeview", font=("Helvetica", 10), background="#e0f7e0", fieldbackground="#e0f7e0", foreground="black")
style.configure("TButton", font=("Helvetica", 10), background="#28a745", foreground="white")
style.map("TButton", background=[('active', '#218838')])

# Create Treeview (Table)
columns = ("nom", "prix", "date", "quantiter")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("nom", text="Nom")
tree.heading("prix", text="Prix in MAD")
tree.heading("date", text="Date")
tree.heading("quantiter", text="Quantiter")

# Adjust column widths
tree.column("nom", width=150)
tree.column("prix", width=100)
tree.column("date", width=150)
tree.column("quantiter", width=100)

# Load data from CSV
load_data()

tree.pack(fill="both", expand=True, padx=10, pady=10)

# Create buttons
button_frame = tk.Frame(root, bg="#e0f7e0")
button_frame.pack(fill="x", pady=10)

inner_frame = tk.Frame(button_frame, bg="#e0f7e0")
inner_frame.pack(anchor="center")

add_button = ttk.Button(inner_frame, text="Ajouter", command=add_entry)
modify_button = ttk.Button(inner_frame, text="Modifier", command=modify_entry)
delete_button = ttk.Button(inner_frame, text="Suprimer", command=delete_entry)

add_button.pack(side="left", padx=5, pady=5)
modify_button.pack(side="left", padx=5, pady=5)
delete_button.pack(side="left", padx=5, pady=5)

# Run the application
root.mainloop()
