from PIL import Image
from pathlib import Path

path = "test.jpg"
width = 100
output_file = "output.txt"


ASCII_CHARS = "@%#*+=-:. "
ASCII_CHARS_DETAILED = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "



def resize_image(image, new_width, aspect_correction=0.55):
    width, height = image.size
    new_height = int(new_width * (height / width) * aspect_correction)
    return image.resize((new_width, new_height), Image.LANCZOS)


def to_grayscale(image):
    return image.convert("L")


def pixel_to_ascii(pixel_value, chars):
    index = int(pixel_value / 255 * (len(chars) - 1))
    return chars[index]


def image_to_ascii(image_path, width=100, invert=False, detailed=False, output_file="output.txt"):
    image = Image.open(image_path)

    chars = ASCII_CHARS_DETAILED if detailed else ASCII_CHARS
    if invert:
        chars = chars[::-1]

    image = resize_image(image, width)
    image = to_grayscale(image)

    pixels = list(image.getdata())
    img_width = image.width

    rows = []
    for i in range(0, len(pixels), img_width):
        row = "".join(pixel_to_ascii(p, chars) for p in pixels[i : i + img_width])
        rows.append(row)

    ascii_art = "\n".join(rows)

    Path(output_file).write_text(ascii_art, encoding="utf-8")
    print(f"Saved to {output_file}")

    return ascii_art


image_to_ascii(path, width=width, output_file=output_file)