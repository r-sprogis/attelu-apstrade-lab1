import numpy as np
from PIL import Image


def darken(img_a: Image.Image, img_b: Image.Image) -> Image.Image:
    a = np.array(img_a, dtype=np.uint8)
    b = np.array(img_b, dtype=np.uint8)

    c = np.where(b <= a, b, a)

    return Image.fromarray(c, "RGBA")

def screen(img_a: Image.Image, img_b: Image.Image) -> Image.Image:
    a = np.array(img_a, dtype=np.float32) / 255.0
    b = np.array(img_b, dtype=np.float32) / 255.0

    c = 1.0 - (1.0 - a) * (1.0 - b)

    c = (c * 255).astype(np.uint8)
    return Image.fromarray(c, "RGBA")

def linear_dodge(img_a: Image.Image, img_b: Image.Image) -> Image.Image:
    a = np.array(img_a, dtype=np.float32) / 255.0
    b = np.array(img_b, dtype=np.float32) / 255.0

    c = np.clip(a + b, 0.0, 1.0)

    c = (c * 255).astype(np.uint8)
    return Image.fromarray(c, "RGBA")

def hard_light(img_a: Image.Image, img_b: Image.Image) -> Image.Image:
    a = np.array(img_a, dtype=np.float32) / 255.0
    b = np.array(img_b, dtype=np.float32) / 255.0

    c = np.where(a <= 0.5,
                 2 * a * b,
                 1 - 2 * (1 - a) * (1 - b))
    
    c = (c * 255).clip(0, 255).astype(np.uint8)
    return Image.fromarray(c, "RGBA")

if __name__ == "__main__":
    img_a = Image.open("a.jpeg").convert("RGBA")
    img_b = Image.open("b.jpeg").convert("RGBA")

    result = darken(img_a, img_b)
    result.save("darken.png")

    result = screen(img_a, img_b)
    result.save("screen.png")

    result = linear_dodge(img_a, img_b)
    result.save("linear_dodge.png")

    result = hard_light(img_a, img_b)
    result.save("hard_light.png")

