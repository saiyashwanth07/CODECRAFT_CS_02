from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path):
    # Open the image
    image = Image.open('/content/images.jpg')
    pixels = np.array(image)

    # Swap the red and blue channels
    encrypted_pixels = pixels.copy()
    encrypted_pixels[:, :, 0], encrypted_pixels[:, :, 2] = encrypted_pixels[:, :, 2], encrypted_pixels[:, :, 0]

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image.save(output_image_path)

def decrypt_image(input_image_path, output_image_path):
    # Open the image
    image = Image.open('/content/images.jpg')
    pixels = np.array(image)

    # Swap the red and blue channels back
    decrypted_pixels = pixels.copy()
    decrypted_pixels[:, :, 0], decrypted_pixels[:, :, 2] = decrypted_pixels[:, :, 2], decrypted_pixels[:, :, 0]

    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image.save(output_image_path)

if __name__ == "__main__":
    input_image_path = "/content/images.jpg"
    output_image_path = "encrypted_image.png"

    # Encrypt the image
    encrypt_image(input_image_path, output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

    # Decrypt the image
    decrypted_image_path = "decrypted_image.png"
    decrypt_image(output_image_path, decrypted_image_path)
    print(f"Image decrypted and saved as {decrypted_image_path}")