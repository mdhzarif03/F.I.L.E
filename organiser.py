import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

FILE_TYPES = {
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".docx", ".doc", ".txt", ".rtf"],
    "Excel": [".xlsx", ".xls", ".csv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"]
}

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, folder_selected)

def organize_folder():
    target_path = path_entry.get().strip()
    
    if not target_path or not os.path.exists(target_path):
        messagebox.showerror("Error", "Please select a valid folder path.")
        return

    try:
        moved_count = 0
        for file in os.listdir(target_path):
            full_file_path = os.path.join(target_path, file)
            
            if os.path.isfile(full_file_path):
                _, file_extension = os.path.splitext(file)
                file_extension = file_extension.lower()

                for folder_name, extensions in FILE_TYPES.items():
                    if file_extension in extensions:
                        destination_folder = os.path.join(target_path, folder_name)
                        
                        if not os.path.exists(destination_folder):
                            os.makedirs(destination_folder)
                        
                        shutil.move(full_file_path, os.path.join(destination_folder, file))
                        moved_count += 1
                        break
        
        messagebox.showinfo("Success", f"Done! Successfully organized {moved_count} files.")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("File Organizer")
root.geometry("450x150")
root.resizable(False, False)

label = tk.Label(root, text="Select the folder you want to organize:", font=("Arial", 10))
label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5, fill='x', padx=20)

path_entry = tk.Entry(frame, width=40)
path_entry.pack(side=tk.LEFT, padx=5, expand=True, fill='x')

browse_btn = tk.Button(frame, text="Browse", command=browse_folder)
browse_btn.pack(side=tk.RIGHT, padx=5)

organize_btn = tk.Button(root, text="Organize Folder", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=organize_folder)
organize_btn.pack(pady=15)

root.mainloop()