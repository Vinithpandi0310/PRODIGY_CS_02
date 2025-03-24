import requests
from PIL import Image
import numpy as np
from io import BytesIO

def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Image downloaded and saved as {save_path}")
    else:
        print("Failed to download the image.")

def encrypt_decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img)
    encrypted_array = img_array ^ key
    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_img.save(output_path)
    print(f'Processed image saved as {output_path}')

if __name__ == "__main__":
    image_url = input("Enter image URL: ")
    input_path = "downloaded_image.jpg"
    download_image(image_url, input_path)
    
    action = input("Enter 'e' to encrypt or 'd' to decrypt: ")
    output_path = input("Enter output image path: ")
    key = int(input("Enter encryption key (0-255): "))
    
    encrypt_decrypt_image(input_path, output_path, key)
