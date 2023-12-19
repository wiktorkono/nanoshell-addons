from tkinter import Tk, Label
from PIL import Image, ImageTk
import os

imgPath = None
image = None
photo = None
label = None

def get_valid_image_path():
    while True:
        path = input("Enter the absolute or relative path of the image or directory you want to view (press Enter to exit): ")
        if not path:
            exit()
        if os.path.exists(path):
            return path
        else:
            print("Invalid path or directory not found. Please try again.")



def load_image(image_path):
    try:
        image = Image.open(image_path)
        return image
    except Exception as e:
        print("Error loading image:", e)
        return None

def resize_image(image):
    root = Tk()
    if image.size[1] > root.winfo_screenheight():
        scale_factor = root.winfo_screenheight() / image.size[1] * 0.90
        image = image.resize((int(image.size[0] * scale_factor), int(image.size[1] * scale_factor)))
    root.destroy()
    return image

def photoview(prompt):
    def get_image_paths(directory):
        image_extensions = ('.jpg', '.jpeg', '.png', '.gif')
        return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(image_extensions)]

    if prompt.startswith("photoview"):
        imgPath = prompt.replace("photoview", "").strip()
    else:
        imgPath = get_valid_image_path()

    root = Tk()
    root.title("Picture Viewer")

    # Check if the path is a directory
    if os.path.isdir(imgPath):
        image_paths = get_image_paths(imgPath)
        if not image_paths:
            print("No image files found in the directory.")
            exit()
        imgPath = image_paths[0]

    image = load_image(imgPath)
    if image is None:
        exit()

    image = resize_image(image)
    root.title(os.path.basename(imgPath))

    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo)
    label.pack()

    def change_image(event):
        nonlocal imgPath, image, photo, label

        image_paths = get_image_paths(os.path.dirname(imgPath))
        if event.keysym == 'Right':
            try:
                current_index = image_paths.index(imgPath)
                if current_index == len(image_paths) - 1:
                    imgPath = image_paths[0]
                else:
                    imgPath = image_paths[current_index + 1]
            except ValueError:
                imgPath = image_paths[0]
        elif event.keysym == 'Left':
            try:
                current_index = image_paths.index(imgPath)
                if current_index == 0:
                    imgPath = image_paths[-1]
                else:
                    imgPath = image_paths[current_index - 1]
            except ValueError:
                imgPath = image_paths[-1]
        image = load_image(imgPath)
        if image is not None:
            image = resize_image(image)
            photo = ImageTk.PhotoImage(image)
            label.configure(image=photo)
            root.title(os.path.basename(imgPath))

    root.bind('<Left>', lambda event: change_image(event))
    root.bind('<Right>', lambda event: change_image(event))

    root.mainloop()

