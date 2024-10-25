import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Prompt the user for the filename to load the reconstructed images
file_name = input("paste here filemane, like 'reconstructed_images.txt: ")

# Load the data from the text file
try:
    reconstructed_images = np.loadtxt(file_name)  # Load reconstructed images into a NumPy array
except Exception as e:
    print(f"Failed to upload file: {e}")  # Print error message if file loading fails
    exit()  # Exit the program if there is an error

# Define parameters for slices
n_slices = reconstructed_images.shape[0]  # Get the total number of slices (first dimension of the array)
initial_slice = n_slices // 2  # Set the initial slice to be the middle slice

# Create a figure and axis for displaying the image
fig, ax = plt.subplots(figsize=(10, 6))  # Create a new figure with specified size
plt.subplots_adjust(bottom=0.25)  # Adjust the layout to make space for the slider

# Display the initial slice as a grayscale image
img = ax.imshow(reconstructed_images[initial_slice].reshape(151, 151), cmap='gray')  # Reshape 1D array to 2D image
ax.set_title(f'Reconstructed Slice at index {initial_slice}')  # Set the title of the plot
ax.set_xlabel('X-axis')  # Label for X-axis
ax.set_ylabel('Y-axis')  # Label for Y-axis

# Add a colorbar to the image
cbar = plt.colorbar(img, ax=ax)  # Create a colorbar to show the intensity scale

# Create a slider to change the index of the slice displayed
ax_slider = plt.axes([0.25, 0.1, 0.5, 0.03])  # Define the position of the slider
slice_slider = Slider(ax_slider, 'Slice', 0, n_slices - 1, valinit=initial_slice, valfmt='%0.0f')  # Create the slider

# Function to update the displayed image when the slider value changes
def update(val):
    slice_index = int(slice_slider.val)  # Get the current value of the slider (index of the slice)
    img.set_data(reconstructed_images[slice_index].reshape(151, 151))  # Update the image data with the new slice
    ax.set_title(f'Reconstructed Slice at index {slice_index}')  # Update the title to reflect the new slice index
    cbar.update_normal(img)  # Update the color scale to match the new image
    plt.draw()  # Redraw the figure to show the updated image

# Bind the update function to the slider
slice_slider.on_changed(update)  # Call update whenever the slider is changed

# Show the figure with the initial image
plt.show()  # Display the plot window with the slider and image
