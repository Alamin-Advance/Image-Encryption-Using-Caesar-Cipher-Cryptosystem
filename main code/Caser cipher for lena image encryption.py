from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open the 512x512 Lena image
lena_image = Image.open("/content/drive/My Drive/Colab Notebooks/cryptosystem/Lena.png")  # Replace with the path to the downloaded image
lena_image_256 = lena_image.resize((256, 256))

# Save or use the 256x256 Lena image
lena_image_256.save("/content/drive/My Drive/Colab Notebooks/cryptosystem/lena_256x256.png")
lena_image_256.show()
# Load the 256x256 Lena image
image_path = '/content/drive/My Drive/Colab Notebooks/cryptosystem/lena_256x256.png'
image = Image.open(image_path).convert("RGB")

# Convert image to numpy array for easy manipulation
image_array = np.array(image)

# Define Caesar encryption keys for each channel
key_R = 50
key_G = 100
key_B = 150

# Apply Caesar Encryption to each channel
encrypted_image_array = image_array.copy()
encrypted_image_array[:, :, 0] = (encrypted_image_array[:, :, 0] + key_R) % 256  # Red channel
encrypted_image_array[:, :, 1] = (encrypted_image_array[:, :, 1] + key_G) % 256  # Green channel
encrypted_image_array[:, :, 2] = (encrypted_image_array[:, :, 2] + key_B) % 256  # Blue channel

# Convert the numpy array back to an image
encrypted_image = Image.fromarray(encrypted_image_array.astype('uint8'))

# Plot original and encrypted images with their histograms
fig, axs = plt.subplots(2, 2, figsize=(6, 5))

# Display Original Image
axs[0, 0].imshow(image)
axs[0, 0].set_title("Original Image")
axs[0, 0].axis("off")

# Plot histogram for the original image (R, G, B channels separately)
colors = ['red', 'green', 'blue']
for i, color in enumerate(colors):
    axs[0, 1].hist(image_array[:, :, i].ravel(), bins=256, color=color, alpha=0.5)
axs[0, 1].set_title("Histogram - Original Image")

# Display Encrypted Image
axs[1, 0].imshow(encrypted_image)
axs[1, 0].set_title("Encrypted Image")
axs[1, 0].axis("off")



# Plot histogram for the encrypted image (R, G, B channels separately)
for i, color in enumerate(colors):
    axs[1, 1].hist(encrypted_image_array[:, :, i].ravel(), bins=256, color=color, alpha=0.5)
axs[1, 1].set_title("Histogram - Encrypted Image")

plt.tight_layout()
plt.show()

