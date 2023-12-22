# image processing
# --------------------------------------------
import cv2
from PIL import Image
import numpy as np
import imutils
# --------------------------------------------


def save_image_cv2(image, path):
    cv2.imwrite(path, image)
# --------------------------------------------
# step 1 crop link


def CropImage(path, fileName, final_path):
    img = Image.open(path)
    width, height = img.size
    img_cropped = img.crop((0, 0, width, height-6))
    img_cropped.save(f'{final_path}{fileName}')
    return img_cropped
# --------------------------------------------
# step 2 gray image


def GrayImage(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# --------------------------------------------


def simple_blur(img):
    return cv2.blur(img, (4, 4))
# ------------------------------------------


def GaussianBlur(img):
    return cv2.GaussianBlur(img, (0, 0), 6)
# --------------------------------------------


def sharping(gray_img, gblur_img):
    return cv2.addWeighted(gray_img, 1.80, gblur_img, -0.60, 0)
# ------------------------------------------


def MedianImage(img):
    median_img = cv2.medianBlur(img, 3)
    median_img = cv2.medianBlur(median_img, 3)
    median_img = cv2.medianBlur(median_img, 3)
    return median_img
# --------------------------------------------
# step 3 dilate


def dilateImage(img):
    return cv2.dilate(img, None, iterations=1)
# --------------------------------------------


def TImage(img):
    return cv2.applyColorMap(img, cv2.COLORMAP_HOT)
# --------------------------------------------


def convert_to_binary2(img):
    ret, thresh_img = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)
    return thresh_img
# --------------------------------------------


def convert_to_binary(img):
    ret, thresh_img = cv2.threshold(img, 10, 200, cv2.THRESH_BINARY)
    return thresh_img
# --------------------------------------------


def InvertImage(img):
    return cv2.bitwise_not(img)
# --------------------------------------------


def bitwise_not(img):
    return cv2.bitwise_not(img)
# --------------------------------------------


def clear_img(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    opening_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    return opening_img
# --------------------------------------------


def remove_white_pixel(img):
    width, height = img.shape[:2]

    for x in range(width):
        for y in range(height):
            count = 0
            pxl = img[x, y]
            if np.all(pxl == [255, 255, 255]):
                for i in range(max(x - 1, 0), min(x + 2, width)):
                    for j in range(max(y - 1, 0), min(y + 2, height)):
                        if np.all(img[i, j] == [255, 255, 255]):
                            count += 1

                if count < 5:
                    img[x, y] = 0

    return img
# --------------------------------------------


def threshImage(path, fileName, final_path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(
        blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    cv2.imwrite(f'{final_path}{fileName}', opening)
    return opening
# ------------------------------------------


def cut_image_R(img, img2):
    width, height = img2.size

    # cut from the left and then right
    flag = False
    left_row = 0
    right_row = 0

    for x in range(width):
        for y in range(height):
            pxl = img[y, x]
            if all(pxl != [0, 0, 0]):
                flag = True
                break

        if flag:
            break

        else:
            left_row = x

    flag = False
    for x in range(0, width):
        for y in range(height):
            pxl = img[y, -x-1]
            if all(pxl != [0, 0, 0]):
                flag = True
                break

        if flag:
            break

        else:
            right_row = x

    img_cropped = img2.crop((left_row, 0, width - right_row, height))
    img_cropped.save(f'1.png')
    return cv2.imread(f'1.png')
# ------------------------------------------


def cut_image(path, fileName, final_path):
    img = cv2.imread(path)
    # height, width = img.shape[:2]
    img2 = Image.open(path)
    width, height = img2.size

    # cut from the left and then right
    flag = False
    left_row = 0
    right_row = 0

    for x in range(width):
        for y in range(height):
            pxl = img[y, x]
            if all(pxl != [0, 0, 0]):
                flag = True
                break

        if flag:
            break

        else:
            left_row = x

    flag = False
    # print(width)
    for x in range(0, width):
        for y in range(height):
            pxl = img[y, -x-1]
            if all(pxl != [0, 0, 0]):
                flag = True
                break

        if flag:
            break

        else:
            right_row = x

    # img = Image.open(path)
    # print(right_row)
    # print(left_row)

    img_cropped = img2.crop((left_row, 0, width - right_row, height))
    img_cropped.save(f'{final_path}/{fileName}')
# ------------------------------------------


def rotate_image(path, fileName, final_path, degree):
    img2 = Image.open(path)

    if(degree):
        rotated_image = img2.transpose(
            Image.ROTATE_90).transpose(Image.FLIP_LEFT_RIGHT)
    else:
        rotated_image = img2.transpose(
            Image.ROTATE_270).transpose(Image.FLIP_LEFT_RIGHT)

    rotated_image.save(f'{final_path}/{fileName}')
# ------------------------------------------


def separate_image(path, fileName, final_path, name=None):
    img = cv2.imread(path)
    img2 = Image.open(path)
    width, height = img2.size
    img_rows = []
    for x in range(width):
        c_row = 0
        for y in range(height):
            pxl = img[y, x]
            c_row += sum(pxl)
        img_rows.append(c_row)

    def sort_image():
        sorted_img_rows = sorted(img_rows)
        img_rows_reformatted = []
        for i, index in enumerate(img_rows):
            img_rows_reformatted.append([index, i])
        sorted_img_rows = sorted(img_rows_reformatted)
        return sorted_img_rows

    already_used = []
    target_row = []
    sorted_img_rows = sort_image()

    for i in sorted_img_rows[5:-5]:
        if i[1] not in already_used:
            target_row.append(i[1])
            for j in range(17):
                try:
                    already_used.append(i[1] + j - 8)
                except:
                    pass
        if len(target_row) == 4:
            break

    target_row = sorted(target_row)
    img_cropped = []
    img_cropped.append(img2.crop((0, 0, target_row[0], height)))
    for i in range(3):
        img_cropped.append(
            img2.crop((target_row[i], 0, target_row[i + 1], height)))
    img_cropped.append(img2.crop((target_row[3], 0, width, height)))
    if(name):
        for i in range(5):
            try:
                img_cropped[i].save(f'{final_path}{name[i]}.png')
            except:
                pass
    else:
        for i in range(5):
            try:
                img_cropped[i].save(f'{final_path}{i}{fileName}')
                # cut_image(f'{final_path}{i}{fileName}',f"{i}{fileName}",f'{final_path}')
                # rotate_image(f'{final_path}{i}{fileName}',f"{i}{fileName}",f'{final_path}',True)
                # cut_image(f'{final_path}{i}{fileName}',f"{i}{fileName}",f'{final_path}')
                # rotate_image(f'{final_path}{i}{fileName}',f"{i}{fileName}",f'{final_path}',True)
            except:
                pass
# ------------------------------------------
def separate_image_alternative(path, fileName, final_path, name=None):
    img = cv2.imread(path)
    img = InvertImage(img)
    img2 = Image.open(path)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REPLICATE)

    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    letter_image_regions = []

    # Now we can loop through each of the four contours and extract the letter
    # inside of each one
    for contour in contours:
        # Get the rectangle that contains the contour
        (x, y, w, h) = cv2.boundingRect(contour)

        # Compare the width and height of the contour to detect letters that
        # are conjoined into one chunk
        # if w / h > 1.25:
        #     # This contour is too wide to be a single letter!
        #     # Split it in half into two letter regions!
        #     half_width = int(w / 2)
        #     letter_image_regions.append((x, y, half_width, h))
        #     letter_image_regions.append((x + half_width, y, half_width, h))
        # else:
        #     # This is a normal letter by itself
        #     letter_image_regions.append((x, y, w, h))
        letter_image_regions.append((x, y, w, h))

    letter_image_regions = sorted(letter_image_regions, key=lambda x: x[0])
    print(letter_image_regions)
    img_cropped = []

    for coords in letter_image_regions:
        try:
            img_cropped.append(img2.crop((coords[0], coords[1], coords[2], coords[3])))
        except:
            pass

    if(name):
        for i in range(5):
            try:
                img_cropped[i].save(f'{final_path}{name[i]}.png')
            except:
                pass
    else:
        for i in range(5):
            try:
                img_cropped[i].save(f'{final_path}{i}{fileName}')
                # cut_image(f'{final_path}{i}{fileName}',f"{i}{fileName}",f'{final_path}')
                # rotate_image(f'{final_path}{i}{fileName}',f"{i}{fileName}",f'{final_path}',True)
                # cut_image(f'{final_path}{i}{fileName}',f"{i}{fileName}",f'{final_path}')
                # rotate_image(f'{final_path}{i}{fileName}',f"{i}{fileName}",f'{final_path}',True)
            except:
                pass
# ------------------------------------------


def add_black_border(path, fileName, final_path, n):
    image = Image.open(path)
    bordered_image = Image.new(
        image.mode, (image.width + 2 * n, image.height + 2 * n), color=0)
    bordered_image.paste(image, (n, n))

    bordered_image.save(f'{final_path}/{fileName}')
# ------------------------------------------
