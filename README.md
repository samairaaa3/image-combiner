# 🖼️ Image Combiner with Green Screen Removal

This project replaces the green background in an image (`kid-green.jpg`) with a new background (`beach.jpg`) using **Python** and the **Pillow** library.

---

## 📌 Overview

- Uses pixel-by-pixel comparison to detect green screen
- Replaces green pixels with corresponding pixels from the background
- Fully implemented in Python using basic image processing (no OpenCV!)

---

## 🧠 How It Works

1. Loads both images (`kid-green.jpg` and `beach.jpg`)
2. Detects green pixels in the foreground
3. Replaces them with pixels from the background
4. Saves the result as `combinedImages.png`

---
# Result
![combinedImages](https://github.com/user-attachments/assets/94e72b40-0362-405c-8eec-e0c8d4a570a8)
