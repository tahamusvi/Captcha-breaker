from keras.models import load_model
from imutils import paths
import numpy as np
import imutils
import cv2
import pickle
from ImageFunctions import InvertImage
import shutil

dataset = {}


def resize_to_fit(image, width, height):
    """
    A helper function to resize an image to fit within a given size
    :param image: image to resize
    :param width: desired width in pixels
    :param height: desired height in pixels
    :return: the resized image
    """

    # grab the dimensions of the image, then initialize
    # the padding values
    (h, w) = image.shape[:2]

    # if the width is greater than the height then resize along
    # the width
    if w > h:
        image = imutils.resize(image, width=width)

    # otherwise, the height is greater than the width so resize
    # along the height
    else:
        image = imutils.resize(image, height=height)

    # determine the padding values for the width and height to
    # obtain the target dimensions
    padW = int((width - image.shape[1]) / 2.0)
    padH = int((height - image.shape[0]) / 2.0)

    # pad the image then apply one more resizing to handle any
    # rounding issues
    image = cv2.copyMakeBorder(image, padH, padH, padW, padW,
        cv2.BORDER_REPLICATE)
    image = cv2.resize(image, (width, height))

    # return the pre-processed image
    return image
#---------------------------
MODEL_FILENAME = "captcha_model.hdf5"
MODEL_LABELS_FILENAME = "model_labels.dat"
CAPTCHA_IMAGE_FOLDER = "generated_captcha_images"
#---------------------------
with open(MODEL_LABELS_FILENAME, "rb") as f:
    lb = pickle.load(f)
    
model = load_model(MODEL_FILENAME)

captcha_image_files = list(paths.list_images(CAPTCHA_IMAGE_FOLDER))


destination_folder = "dataset"

for image_file in captcha_image_files:
    image = cv2.imread(image_file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = InvertImage(image)
    image = cv2.copyMakeBorder(image, 20, 20, 20, 20, cv2.BORDER_REPLICATE)
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    contours = contours[1] if imutils.is_cv3() else contours[0]

    letter_image_regions = []

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if w / h > 1.25:
            half_width = int(w / 2)
            letter_image_regions.append((x, y, half_width, h))
            letter_image_regions.append((x + half_width, y, half_width, h))
        else:
            letter_image_regions.append((x, y, w, h))

    
    if len(letter_image_regions) != 1:
        print("Failed to extract letter from the captcha!")
        exit(1)

    
    letter_image_regions = sorted(letter_image_regions, key=lambda x: x[0])

    for letter_bounding_box in letter_image_regions:
        x, y, w, h = letter_bounding_box

        letter_image = image[y - 2 : y + h + 2, x - 2 : x + w + 2]

        letter_image = resize_to_fit(letter_image, 20, 20)

        letter_image = np.expand_dims(letter_image, axis=2)
        letter_image = np.expand_dims(letter_image, axis=0)

        prediction = model.predict(letter_image)

        letter = lb.inverse_transform(prediction)[0]
        print("Predicted letter:", letter)

        if(not letter in dataset):
            dataset[letter] = 0
        dataset[letter] += 1
        
        destination_file = f"{destination_folder}/{letter}/{letter}{dataset[letter]}.png"

        shutil.move(image_file, destination_file)


    


    

