from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
root.title("Image Slider")
root.iconbitmap('C:/Codemy/video 9-Image Viewing App/picture.ico')

# Path to the directory containing the images
img_dir = 'image'

# List of image files
listimg = os.listdir(img_dir)

# Ensure the list of images is not empty
if not listimg:
    raise Exception("No images found in the directory.")

# Initial image index
i = 0

# Initial position of the image
j = 1

# Total number of images
k = len(listimg)

# Define the target size for the images
image_size = (1200, 630)  # width, height

# Function to update the displayed image and its name
def updateImage():
    global imglabel, img, name_label, i, j, Imageindex
    
    # Wrap around the index
    i = i % k
    j = (i + 1) % k
    if j == 0:
        j = k

    img_path = os.path.join(img_dir, listimg[i])
    img = Image.open(img_path)
    img = img.resize(image_size, Image.LANCZOS)  # Resize the image using LANCZOS filter
    img = ImageTk.PhotoImage(img)
    
    imglabel.config(image=img)
    imglabel.image = img  # Keep a reference to prevent garbage collection
    
    nameimg = listimg[i].split('.')[0]
    name_label.config(text=nameimg)
    
    Imageindex.config(text=f'Image {j} of {k}')

# Create label for image name
nameimg = listimg[i].split('.')[0]
name_label = Label(root, text=nameimg, font=("Arial", 16))
name_label.grid(row=0, column=1, columnspan=3, pady=10)

# Initial image display using grid
img_path = os.path.join(img_dir, listimg[i])
img = Image.open(img_path)
img = img.resize(image_size, Image.LANCZOS)  # Resize the image using LANCZOS filter
img = ImageTk.PhotoImage(img)
imglabel = Label(root, image=img)
imglabel.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

# Label to display the image index
Imageindex = Label(root, text=f'Image {j} of {k}')
Imageindex.grid(row=3, column=4, columnspan=3)

# Function to display the next image
def slideimageright():
    global i, j
    i += 1
    updateImage()

# Function to display the previous image
def slideimageleft():
    global i, j
    i -= 1
    updateImage()

# Navigation buttons using grid
button_left_imag = Button(root, text="<<", command=slideimageleft)
button_left_imag.grid(row=2, column=0, sticky=W, pady=10)

button_right_imag = Button(root, text=">>", command=slideimageright)
button_right_imag.grid(row=2, column=4, sticky=E, pady=10)

button_exit = Button(root, text="Exit", command=root.destroy)
button_exit.grid(row=3, column=1, columnspan=3, pady=10)

# Configure column weights to center the image and buttons
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()
