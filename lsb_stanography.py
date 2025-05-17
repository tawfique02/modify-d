import sys
import re
from PIL import Image
from tqdm import tqdm

def extract_lsb_data(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    bits = ''
    for pixel in pixels:
        for color in pixel[:3]:  # RGB channels only
            bits += str(color & 1)

    # Convert bits to bytes
    data = ''
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break
        char = chr(int(byte, 2))
        data += char
    return data

def search_flag(data, pattern):
    return re.findall(pattern, data)

def main():
    print(r"""
  ____  _                   _       _     _           
 / __|| | ___  _ __ _ _() __ | |_ | | ___  ___ 
 \___ \| _/ _ \| '| '| |/ _` | ' \| |/ _ \/ __|
  __) | || () | |  | |  | | (| | |) | |  _/\_ \
 |/ \\/||  ||  ||\,|./||\||_/
                                                    
Steg-LSB Extractor - v1.0.0
Developed by Md Tawfique Elahey.
    """)

    image_path = input("Enter the image file name (e.g., download.png): ").strip()
    pattern = input("Enter the flag pattern (e.g., FLAG{.*?}, CTF{.*?}): ").strip()

    print("\nExtracting LSB data and searching for pattern...\n")
    raw_data = extract_lsb_data(image_path)

    # Simulate progress
    for i in tqdm(range(100), desc="Overall Progress", ncols=70):
        pass

    flags = search_flag(raw_data, pattern)
    if flags:
        print("\nFound flag(s):")
        for flag in flags:
            print("  ->", flag)
    else:
        print("\nNo flags found with the given pattern.")

if __name__ == "__main__":
    main()
