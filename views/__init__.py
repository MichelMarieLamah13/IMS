from PIL import Image, ImageTk


def get_image(name, height=345, width=181):
    img = Image.open(f"images/{name}")
    img = img.resize((width, height), Image.ANTIALIAS)
    imgtk = ImageTk.PhotoImage(img)
    return imgtk
