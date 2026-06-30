import os
import shutil

downloads_path = input('Enter your downloads folder location: ')

file_types = {
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".docx", ".doc", ".txt", ".rtf"],
    "Excel": [".xlsx", ".xls", ".csv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"]
}
os.chdir(downloads_path)

for file in os.listdir(downloads_path):
    if os.path.isfile(file):
        file_name, file_extension = os.path.splitext(file)
        file_extension = file_extension.lower()

        for folder_name, extensions in file_types.items():
            if file_extension in extensions:
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)

                shutil.move(file, os.path.join(folder_name, file))
                break