import pytesseract # type: ignore
from PIL import Image # type: ignore
import tkinter as tk
from tkinter import filedialog

def extract_text(image_path):
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        return text
    except Exception as e:
        return f"Error: {e}"

def get_image_file():
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )

    if file_path:
        return file_path
    else:
        print("No file selected.")
        exit(0)

print(extract_text(get_image_file()))