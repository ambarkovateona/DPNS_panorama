

import sys
import cv2
import numpy as np

from stitch.image_stitching import read_images,recursion




def main(image_dir_list):
    """Main function of the Repository.
    Takes in list of image dir, runs the complete image stitch pipeline
    to create and export a panoramic image in the /outputs/ folder.

    Args:
        image_dir_list (List): List of image dirs passed in cmdline
    """

    images_list, no_of_images = read_images.read(image_dir_list)
    result, mapped_image = recursion.recurse(images_list, no_of_images)
    cv2.imwrite("outputs/panorama_image.jpg", result)
    result = np.uint8(result)
    preview = cv2.resize(result, (1600, 600))  # или пробај (1280, 480)

    cv2.imshow("Panorama Preview", preview)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    result = np.uint8(result)
    cv2.imwrite("stitch/outputs/panorama_image.jpg", result)
    cv2.imwrite("stitch/outputs/mapped_image.jpg", mapped_image)

    print(f"Panoramic image saved at: outputs/panorama_image.jpg")


if __name__ == "__main__":
    image_list = []
    for i in range(1, len(sys.argv)):
        image_list.append(sys.argv[i])
    main(image_list)