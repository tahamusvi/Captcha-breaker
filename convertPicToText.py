import os
from google.cloud import vision

# Create a client instance
client = vision.ImageAnnotatorClient()

# Set the path to the image file
image_path = 'test/ts2/a.png'

# Perform OCR on the image
response = client.annotate_image(image_path)

# Extract the OCR result
ocr_result = response.full_resource.annotations[0].description

# Print the OCR result
print(ocr_result)