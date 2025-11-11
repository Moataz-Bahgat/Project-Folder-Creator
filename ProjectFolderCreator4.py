import os
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil

# --- Configuration ---
TEMPLATE_FILENAME = "BOM template.xls"
# Assumes the template is in the same directory as this Python script
template_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), TEMPLATE_FILENAME)
# Define the available subfolders (without numbering)
DEFAULT_SUBFOLDERS = ["CAD Files", "PDF", "DXF", "Bill of Material", "Other"]
# ---------------------

def create_folders():
    base_path = base_path_var.get()
    project_name = project_name_var.get().strip()
    
    # Get the list of folders selected by the user
    selected_folders = [
        folder for folder, var in folder_vars.items() if var.get() == 1
    ]
    
    if not base_path:
        messagebox.showerror("Error", "Please select a location first.")
        return
    if not project_name:
        messagebox.showerror("Error", "Please enter a valid Project Name.")
        return
    if not selected_folders:
        messagebox.showwarning("Warning", "Please select at least one folder to create.")
        return
    
    full_path = os.path.join(base_path, project_name)
    
    try:
        # Check if the main folder exists and ask for confirmation
        if os.path.exists(full_path):
            folder_list_str = "\n".join([f"- {f}" for f in selected_folders])
            confirm = messagebox.askyesno(
                "Warning", 
                f"The folder '{project_name}' already exists.\nDo you want to add/update the following selected subfolders?\n\n{folder_list_str}"
            )
            if not confirm:
                return
        
        # 1. Create the main project folder
        os.makedirs(full_path, exist_ok=True)
        
        # 2. Create only the selected subfolders
        bom_path = ""
        for folder in selected_folders:
            folder_path = os.path.join(full_path, folder)
            os.makedirs(folder_path, exist_ok=True)
            if folder == "Bill of Material":
                bom_path = folder_path
        
        # 3. Copy the BOM template if "Bill of Material" was selected
        if bom_path:
            if os.path.exists(template_file_path):
                destination_file_path = os.path.join(bom_path, TEMPLATE_FILENAME)
                shutil.copy(template_file_path, destination_file_path)
            else:
                messagebox.showwarning("Warning", f"Could not find the template file: '{TEMPLATE_FILENAME}'.\nBOM folder was still created.")

        messagebox.showinfo("Success", f"Project folders created successfully at:\n{full_path}")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

def browse_folder():
    folder_selected = filedialog.askdirectory(title="Select base folder for the new project")
    if folder_selected:
        base_path_var.set(folder_selected)

# --- GUI Setup ---
root = tk.Tk()
root.title("Project Template by Eng. Moataz-Bahgat")
root.geometry("450x380")
root.resizable(False, False)

# --- Widgets ---

# Project Name
tk.Label(root, text="Project Name (e.g., K-001-Cabinet):").pack(anchor="w", padx=10, pady=(10,0))
project_name_var = tk.StringVar()
tk.Entry(root, textvariable=project_name_var, width=65).pack(padx=10, pady=5)

# Base Path
tk.Label(root, text="Base Location for New Folder:").pack(anchor="w", padx=10, pady=(5,0))
base_path_var = tk.StringVar()
path_frame = tk.Frame(root)
path_frame.pack(padx=10, pady=5, fill="x")

tk.Entry(path_frame, textvariable=base_path_var, width=45, state="readonly").pack(side="left", expand=True, fill="x")
tk.Button(path_frame, text="Browse...", command=browse_folder).pack(side="right", padx=5)

# Folder Selection
tk.Label(root, text="Select Subfolders to Create:").pack(anchor="w", padx=10, pady=(5,0))

# Frame for checkboxes
checkbox_frame = tk.Frame(root)
checkbox_frame.pack(padx=10, pady=5, anchor="w")

# Dictionary to hold the variable for each checkbox
folder_vars = {}
for folder_name in DEFAULT_SUBFOLDERS:
    var = tk.IntVar(value=1) # Set default to checked (1)
    folder_vars[folder_name] = var
    tk.Checkbutton(checkbox_frame, text=folder_name, variable=var).pack(anchor="w", pady=1)

# Create Button
tk.Button(root, text="Create Selected Project Structure", command=create_folders, bg="#0078D7", fg="white", height=2).pack(padx=10, pady=15, fill="x")

root.mainloop()