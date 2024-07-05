import tkinter as tk
from tkinter import filedialog
import os


def filter_files(file_paths, save_directory):

    for file_path_get in file_paths:
        file_name_with_ext = os.path.basename(file_path_get)
        file_name, _ = os.path.splitext(file_name_with_ext)
    
        valid_lines = []
        with open(file_path_get, "r") as file:
            header = file.readline().strip()
            valid_lines.append(header)
            for line in file:
                if line.strip().endswith('1'):
                    valid_lines.append(line.strip().replace('.', ','))

        file_path_write = os.path.join(save_directory, f"(FILTERED) {file_name}.csv")

        with open(file_path_write, "w") as file:
            file.write("\n".join(valid_lines))
            

root = tk.Tk()
root.withdraw()

file_paths_get = filedialog.askopenfilenames(
    title="Select a CSV file", 
    filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )

if file_paths_get:
    save_directory = filedialog.askdirectory(
        title="Select directory to save files"
    )

    if save_directory:
        filter_files(file_paths_get, save_directory)