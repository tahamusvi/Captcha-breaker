from PIL import Image, ImageDraw, ImageFont
import random
import string
import math

def generate_captcha(word_length=5, image_size=(140, 50), font_size=25):
    # Create a blank image
    image = Image.new("RGBA", image_size, (0, 0, 0))  # Use RGBA mode for transparency
    draw = ImageDraw.Draw(image)

    # Choose a random word for the captcha
    captcha_word = ''.join(random.choices(string.ascii_uppercase + string.digits, k=word_length))

    # Load a font
    font = ImageFont.truetype("arial.ttf", font_size)

    # Initial position for the text
    x, y = 8, 10

    for char in captcha_word:
        # Apply random transformations to each character
        rotation_angle = random.uniform(-30, 30)
        skew_angle = random.uniform(-0.2, 0.2)
        scale_factor = random.uniform(0.8, 1.2)
        warp_matrix = [1.0, 0.0, random.uniform(-0.1, 0.1), 0.0, 1.0, random.uniform(-0.1, 0.1)]

        # Rotate, skew, and scale the character
        char_image = Image.new('RGBA', (font_size, font_size), (255, 255, 255, 0))
        char_draw = ImageDraw.Draw(char_image)
        char_draw.text((0, 0), char, font=font, fill=(255, 255, 255, 255))  # Use RGBA for character color

        char_image = char_image.rotate(rotation_angle, expand=1)
        char_image = char_image.transform(char_image.size, Image.AFFINE, (1, skew_angle, 0, 0, 1, 0), Image.BICUBIC)
        char_image = char_image.resize((int(font_size * scale_factor), int(font_size * scale_factor)), Image.BILINEAR)
        char_image = char_image.transform(char_image.size, Image.AFFINE, warp_matrix, Image.BICUBIC)

        # Paste the transformed character onto the main image
        image.paste(char_image, (x, y), char_image)

        # Update the position for the next character
        x += char_image.width
        # + random.randint(5, 10)

    # Save the captcha image
    image.save("trainCaptcha/" + str(captcha_word) + ".png")

if __name__ == "__main__":
    for i in range(20000):
        generate_captcha()
