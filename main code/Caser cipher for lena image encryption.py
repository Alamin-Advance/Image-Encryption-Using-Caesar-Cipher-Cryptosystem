from PIL import Image

# Open the 512x512 Lena image
lena_image = Image.open("/content/drive/My Drive/Colab Notebooks/cryptosystem/Lena.png")  # Replace with the path to the downloaded image
lena_image_256 = lena_image.resize((256, 256))

# Save or use the 256x256 Lena image
lena_image_256.save("/content/drive/My Drive/Colab Notebooks/cryptosystem/lena_256x256.png")
lena_image_256.show()
