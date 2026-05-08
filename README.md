# Panorama Image Stitching using SIFT and RANSAC

## Authors

* Teona Ambarkova – 233231
* Marko Kadzbanov – 233151

---

## Overview

This project implements an automatic panorama image stitching system using computer vision algorithms in Python and OpenCV.

Multiple overlapping images are combined into a single seamless panorama using:

* SIFT feature detection
* Feature matching
* RANSAC homography estimation
* Gaussian blending

The system supports recursive stitching of multiple images and produces smooth panoramic outputs without visible seams.

---

## Features

* Automatic panorama generation
* SIFT keypoint detection
* Robust feature matching
* Homography estimation using RANSAC
* Gaussian weighted blending
* Recursive stitching for multiple images
* Automatic cropping of black borders

---

## Project Structure

```bash
stitch/
│
├── image_stitching/
│   ├── image_stitching.py
│   ├── read_images.py
│   ├── recursion.py
│   └── utils.py
│
├── inputs/
├── outputs/
│
└── panorama.py
```

---

## Requirements

Install dependencies:

```bash
pip install opencv-python opencv-contrib-python numpy matplotlib
```

---

## How to Run

```bash
python panorama.py
```

---

## Output

The program generates:

* `mapped_image.jpg` — visualization of matched keypoints
* `panorama_image.jpg` — final panoramic image

---

## Algorithms Used

### SIFT

Detects scale and rotation invariant keypoints.

### Feature Matching

Matches descriptors using Euclidean distance.

### RANSAC

Removes outliers and estimates homography.

### Gaussian Blending

Creates smooth transitions between overlapping images.

---

## Technologies

* Python
* OpenCV
* NumPy
* Matplotlib

---

## References

* David Lowe — *Distinctive Image Features from Scale-Invariant Keypoints*
* Richard Szeliski — *Image Alignment and Stitching: A Tutorial*
* [OpenCV Documentation](https://docs.opencv.org)
