from PIL import Image
import pandas as pd
import tkinter as tk
from tkinter import filedialog

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

def process_image(image_path):
    img = Image.open(image_path)
    
    width, height = img.size
    
    bottom_line = [img.getpixel((x, height - 1)) for x in range(width)]
    mean_green = sum(pixel[1] for pixel in bottom_line) / len(bottom_line)
    pressure_detected = mean_green > 150  
    img_right = img.crop((width // 2, 0, width, height))
    
  
    Fingers = [
        img_right.crop((0, 0, width // 2, height // 10)), 
        img_right.crop((0, height // 5, width // 2, height // 3)),  
        img_right.crop((0, height // 3, width // 2, height // 2)),  
        img_right.crop((0, height // 2, width // 2, height // 1.5)),  
        img_right.crop((0, height // 1.5, width // 2, height)) 
    ]
    
    finger_names = ['thumb', 'index', 'middle', 'ring', 'pinky']
    
    finger_data = {}
    
    for finger_name, finger in zip(finger_names, Fingers):
        pixels = finger.load()
        finger_width, finger_height = finger.size
        pressure_detected = False
        
        for x in range(finger_width):
            for y in range(finger_height):
                r, g, b = pixels[x, y]
                if r >= 10 and g >= 150 and b >= 240:
                    pressure_detected = True
                    break
            if pressure_detected:
                break
        
        
        finger_data[finger_name] = 1 if pressure_detected else 0
    
    return finger_data, pressure_detected

def save_to_excel(data, file_name):
    df = pd.DataFrame([data])
    df.to_excel(file_name, index=False)


finger_data, pressure_detected = process_image(get_image_file())

finger_data['overall_pressure'] = 1 if pressure_detected else 0

save_to_excel(finger_data, 'finger_pressure_data.xlsx')

print(finger_data)
