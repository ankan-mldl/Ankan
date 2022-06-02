"""
Programme to check whether an inserted image is clicked in
day time or in night time.
"""

import os

try:
    from PIL import Image
except ImportError:
    exit("Please install the package PIL and try again.")


def time_checker(image_file):
    # loading the image
    img = Image.open(image_file).convert('L')

    # extracting the size of the image
    width, height = img.size

    # empty dictionary to store the pixel counts
    pixel_counts = {}

    # looping over all the pixels
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))

            if pixel in pixel_counts:
                pixel_counts[pixel] += 1
            else:
                pixel_counts[pixel] = 1
    

    # calculating sum all the pixels that has value greater than 150
    pixel_sum = 0

    for pix, cnt in pixel_counts.items():
        if pix >= 125:
            pixel_sum = pixel_sum + cnt
    

    # calculating the percentage of that sum over the total number of pixels
    # present in the image
    percentage = (pixel_sum / sum(pixel_counts.values())) * 100
    
    if percentage >= 40.0:
        print('Day')
    else:
        print('Night')
    
    


# main function
if __name__ == '__main__':
    image = input("Enter the image name with extension: ").strip()
    
    if os.path.isfile(image):
        time_checker(image_file=image)
    else:
        print("The entered file doesn't exist.")


