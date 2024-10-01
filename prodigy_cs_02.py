from PIL import Image
def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    # Encrypt by modifying each pixel using the key
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[height]
            encrypted_pixel = (b, g, r)
            pixels[i, j] = encrypted_pixel

    img.save("output_path")
    print("Image encrypted successfully")
    
def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    
    width, height = img.size

    # Decrypt by reversing the encryption process using the same key
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            

    img.save("output_path")
    print("Image decrypted successfully")
    
    input_image = r"C:\Users\IRA\Documents\PRODIGY_CS_02.PY\car.png"
    encrypted_image = r"C:\Users\IRA\Documents\PRODIGY_CS_02.PY\encrypted_image.png"
    decrypted_image = r"C:\Users\IRA\Documents\PRODIGY_CS_02.PY\decrypted_image.png"
    
    encrypt_image(input_image, encrypted_image, key=None)
    
    decrypt_image(encrypted_image, decrypted_image, key=None)

