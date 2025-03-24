from PIL import Image
import numpy as np
import os

def encrypt_decrypt_image(input_path, output_path, key):
    try:
        img = Image.open(input_path)
        img_array = np.array(img)
        encrypted_img = Image.fromarray((img_array ^ key).astype(np.uint8), mode=img.mode)
        encrypted_img.save(output_path)
        print(f"✅ Processed image saved: {output_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    action = input("Enter 'e' to encrypt or 'd' to decrypt: ").strip().lower()
    input_path = input("Enter input image path: ").strip()

    if not os.path.exists(input_path):
        print("❌ Error: File not found.")
        exit()

    output_path = input("Enter output image path: ").strip()

    try:
        key = int(input("Enter encryption key (0-255): ").strip())
        if not (0 <= key <= 255):
            raise ValueError("Key must be between 0 and 255")
        encrypt_decrypt_image(input_path, output_path, key)
    except ValueError:
        print("❌ Error: Invalid key. Enter a number between 0 and 255.")

