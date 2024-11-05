from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
# Load the Lena image
image_path = '/content/drive/My Drive/Colab Notebooks/cryptosystem/lena_256x256.png'
image = Image.open(image_path).convert("RGB")

# Convert the image to a numpy array
image_array = np.array(image)

# Scramble the pixel positions
np.random.seed(42)  # For reproducibility
scrambled_image_array = image_array.copy()
height, width, _ = scrambled_image_array.shape
pixel_positions = np.arange(height * width)
np.random.shuffle(pixel_positions)

# Reshape the shuffled positions back to the 2D form
new_positions = np.unravel_index(pixel_positions, (height, width))

# Assign pixels to new positions
scrambled_image_array[new_positions[0], new_positions[1], :] = image_array.reshape(-1, 3)

# Define Caesar encryption keys for each channel
key_R = 50
key_G = 100
key_B = 150

# Apply Caesar Encryption to each channel in the scrambled image
encrypted_scrambled_image_array = scrambled_image_array.copy()
encrypted_scrambled_image_array[:, :, 0] = (encrypted_scrambled_image_array[:, :, 0] + key_R) % 256  # Red channel
encrypted_scrambled_image_array[:, :, 1] = (encrypted_scrambled_image_array[:, :, 1] + key_G) % 256  # Green channel
encrypted_scrambled_image_array[:, :, 2] = (encrypted_scrambled_image_array[:, :, 2] + key_B) % 256  # Blue channel

# Convert numpy arrays back to images
scrambled_image = Image.fromarray(scrambled_image_array.astype('uint8'))
encrypted_scrambled_image = Image.fromarray(encrypted_scrambled_image_array.astype('uint8'))

# Plot original, scrambled, and encrypted scrambled images with their histograms
fig, axs = plt.subplots(2, 3, figsize=(9, 6))

# Display Original Image
axs[0, 0].imshow(image)
axs[0, 0].set_title("Original Image", fontsize=8)
axs[0, 0].axis("off")

# Plot combined histogram for the original image (R, G, B channels)
colors = ['red', 'green', 'blue']
for i, color in enumerate(colors):
    axs[1, 0].hist(image_array[:, :, i].ravel(), bins=256, color=color, alpha=0.5)
axs[1, 0].set_title("Histogram - Original Image", fontsize=8)

# Display Scrambled Image
axs[0, 1].imshow(scrambled_image)
axs[0, 1].set_title("Piksel Konumlarını Değiştirme image", fontsize=8)
axs[0, 1].axis("off")

# Plot combined histogram for the scrambled image (R, G, B channels)
for i, color in enumerate(colors):
    axs[1, 1].hist(scrambled_image_array[:, :, i].ravel(), bins=256, color=color, alpha=0.5)
axs[1, 1].set_title("Histogram - Piksel Konumlarını Değiştirme image", fontsize=8)

# Display Encrypted Scrambled Image
axs[0, 2].imshow(encrypted_scrambled_image)
axs[0, 2].set_title("Encrypted Piksel Konumlarını Değiştirme image", fontsize=8)
axs[0, 2].axis("off")

# Plot combined histogram for the encrypted scrambled image (R, G, B channels)
for i, color in enumerate(colors):
    axs[1, 2].hist(encrypted_scrambled_image_array[:, :, i].ravel(), bins=256, color=color, alpha=0.5)
axs[1, 2].set_title("Histogram - Piksel Konumlarını Değiştirme image", fontsize=8)

plt.tight_layout()
plt.show()
