from pathlib import Path
from collections import Counter
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

FILE_TYPES = {
    "Videos": {".mp4", ".mkv", ".avi", ".mov", ".flv"},
    "PDFs": {".pdf"},
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"},
    "Documents": {".doc", ".docx", ".txt", ".rtf"},
    "Excel": {".xls", ".xlsx", ".csv"},
    "Audio": {".mp3", ".wav", ".aac", ".flac"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
}

EXTENSION_MAP = {
    ext: category
    for category, extensions in FILE_TYPES.items()
    for ext in extensions
}

WINDOW_WIDTH = 450
WINDOW_HEIGHT = 220


def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, folder)


def unique_destination(path: Path) -> Path:
    if not path.exists():
        return path

    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    counter = 1

    while True:
        candidate = parent / f"{stem} ({counter}){suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def organize_folder():
    folder = Path(path_entry.get().strip())

    if not folder.is_dir():
        messagebox.showerror("Error", "Please select a valid folder.")
        return

    organize_btn.config(state="disabled")
    root.update_idletasks()

    moved = 0
    skipped = 0
    stats = Counter()

    for item in folder.iterdir():
        if item.is_dir():
            continue

        category = EXTENSION_MAP.get(item.suffix.lower())

        if category is None:
            skipped += 1
            continue

        try:
            destination_folder = folder / category
            destination_folder.mkdir(exist_ok=True)

            destination = unique_destination(destination_folder / item.name)
            shutil.move(str(item), str(destination))

            moved += 1
            stats[category] += 1

        except Exception:
            skipped += 1

    organize_btn.config(state="normal")

    lines = [f"{name:<12}: {stats[name]}" for name in FILE_TYPES if stats[name]]

    summary = (
        "Organization Complete\n\n"
        + "\n".join(lines)
        + f"\n\nMoved   : {moved}"
        + f"\nSkipped : {skipped}"
    )

    messagebox.showinfo("F.I.L.E.", summary)


root = tk.Tk()

try:
    root.iconbitmap("assets/app_icon.ico")
except Exception:
    pass

root.title("F.I.L.E")
root.resizable(False, False)
root.configure(bg="#D4D0C8")

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

x = (screen_w - WINDOW_WIDTH) // 2
y = (screen_h - WINDOW_HEIGHT) // 2

root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")

tk.Label(
    root,
    text="File Intelligence and Local Engine",
    font=("MS Sans Serif", 11, "bold"),
    bg="#D4D0C8",
).pack(pady=(12, 2))

tk.Label(
    root,
    text="Select the folder you want to organize:",
    font=("MS Sans Serif", 10),
    bg="#D4D0C8",
).pack(pady=(2, 10))

frame = tk.Frame(root, bg="#D4D0C8")
frame.pack(fill="x", padx=20)

path_entry = tk.Entry(
    frame,
    font=("MS Sans Serif", 9),
    bd=2,
    relief="sunken",
)
path_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

tk.Button(
    frame,
    text="Browse...",
    command=browse_folder,
    font=("MS Sans Serif", 9),
).pack(side="right")

organize_btn = tk.Button(
    root,
    text="Organize Folder",
    command=organize_folder,
    font=("MS Sans Serif", 10, "bold"),
)
organize_btn.pack(pady=(15, 5))


def show_help():
    messagebox.showinfo(
        "F.I.L.E. Help",
        "• Click Browse... and select a folder.\n"
        "• Click Organize Folder.\n"
        "• Files are sorted into folders based on type.\n"
        "• Unknown file types are left unchanged.\n"
        "• Existing files are never overwritten.",
    )


tk.Button(
    root,
    text="Help",
    command=show_help,
    font=("MS Sans Serif", 9),
).pack()

root.mainloop()