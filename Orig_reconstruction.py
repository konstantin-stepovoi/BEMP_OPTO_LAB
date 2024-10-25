import h5py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Open the .mat file
file_path = 'suture/Reconstruction/Reconstructed.mat'  # Replace with your file path
with h5py.File(file_path, 'r') as f:
    # Get the array R
    R = f['R'][:]  # Load data from group R

# Define parameters for slices
n_slices = R.shape[2]  # Total number of slices
initial_slice = n_slices // 2  # Initial slice

# Create a figure and axis for displaying
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)  # Leave space for the slider

# Display the first slice
img = ax.imshow(R[:, :, initial_slice], cmap='gray')
ax.set_title(f'Slice at index {initial_slice}')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Add color bar
cbar = plt.colorbar(img, ax=ax)

# Create a slider for changing the slice index
ax_slider = plt.axes([0.25, 0.1, 0.5, 0.03])  # [left, bottom, width, height]
slice_slider = Slider(ax_slider, 'Slice', 0, n_slices - 1, valinit=initial_slice, valfmt='%0.0f')

# Function to update the image when the slider changes
def update(val):
    slice_index = int(slice_slider.val)  # Get the current value of the slider
    img.set_data(R[:, :, slice_index])  # Update image data
    ax.set_title(f'Slice at index {slice_index}')  # Update title
    cbar.update_normal(img)  # Update color bar
    plt.draw()  # Redraw the figure

# Link the update function to the slider
slice_slider.on_changed(update)

# Show the figure
plt.show()
