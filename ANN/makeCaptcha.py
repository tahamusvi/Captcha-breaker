from PIL import Image, ImageDraw, ImageFont
import random
import string
import math
import os


def generate_captcha(word_length=1, image_size=(28, 25), font_size=25):
    global i

    # Create a blank image
    # Use RGBA mode for transparency
    image = Image.new("RGBA", image_size, (0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Choose a random word for the captcha
    captcha_word = ''.join(random.choices(
        string.ascii_letters + string.digits, k=word_length))

    # Load a font
    font = ImageFont.truetype("arial.ttf", font_size)

    # Initial position for the text
    x, y = 4, 0

    for char in captcha_word:
        global i
        # Apply random transformations to each character
        rotation_angle = random.uniform(-30, 30)
        skew_angle = random.uniform(-0.2, 0.2)
        scale_factor = random.uniform(0.8, 1.2)
        warp_matrix = [
            1.0, 0.0, random.uniform(-0.1, 0.1), 0.0, 1.0, random.uniform(-0.1, 0.1)]

        # Rotate, skew, and scale the character
        char_image = Image.new(
            'RGBA', (font_size, font_size), (255, 255, 255, 0))
        char_draw = ImageDraw.Draw(char_image)
        char_draw.text((0, 0), char, font=font, fill=(
            255, 255, 255, 255))  # Use RGBA for character color

        char_image = char_image.rotate(rotation_angle, expand=1)
        char_image = char_image.transform(
            char_image.size, Image.AFFINE, (1, skew_angle, 0, 0, 1, 0), Image.BICUBIC)
        char_image = char_image.resize(
            (int(font_size * scale_factor), int(font_size * scale_factor)), Image.BILINEAR)
        char_image = char_image.transform(
            char_image.size, Image.AFFINE, warp_matrix, Image.BICUBIC)

        # Paste the transformed character onto the main image
        image.paste(char_image, (x, y), char_image)

        image = image.convert('RGB')
        image = image.convert('P', palette=Image.ADAPTIVE, colors=256)

        # Update the position for the next character
        x += char_image.width
        # + random.randint(5, 10)

    # Save the captcha image
    captcha_word = str(captcha_word)
    if captcha_word.isnumeric():
        pass
    elif captcha_word.islower():
        captcha_word = "lower_" + captcha_word
    else:
        captcha_word = "upper_" + captcha_word

    path = r"trainCaptcha/" + captcha_word + "/"
    if not os.path.exists(path):
        os.makedirs(path)
    image.save(path + str(i) + ".png")


if __name__ == "__main__":
    for i in range(10000):
        generate_captcha()
