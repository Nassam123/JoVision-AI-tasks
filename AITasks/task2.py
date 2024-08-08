from PIL import Image
import tkinter as tk
from tkinter import filedialog

def convert_to_grayscale(image_path):
    # Open the image
    image = Image.open(image_path)
    grayscale_image = Image.new("L", image.size)
    
    # Get pixel data
    pixels = image.load()
    grayscale_pixels = grayscale_image.load()
    
    
    for i in range(image.width):
        for j in range(image.height):
            
            pixel_values = pixels[i, j]
            if len(pixel_values) == 4:  # RGBA
                r, g, b, _ = pixel_values
            else:  # RGB
                r, g, b = pixel_values
            
            
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            grayscale_pixels[i, j] = gray
    

    grayscale_image.show()
    
    return grayscale_image

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

convert_to_grayscale(get_image_file())
