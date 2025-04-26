# QR Code Generator in Python

This project demonstrates how to create QR codes easily using Python.
You can generate basic or fully customized QR codes with just a few lines of code!

---

## Installation

First, install the required library:

```bash
pip install qrcode
```

---

## Project Structure

```
QR-Code-Generator-in-Python/
|➜ generate_basic_qr.py
|➜ generate_custom_qr.py
|➜ README.md
```

---

## Two Ways to Generate a QR Code

### 1. Normal QR Code (Simple)

**File:** `generate_basic_qr.py`

```python
# generate_basic_qr.py

import qrcode

def generate_basic_qr(data, output_file):
    img = qrcode.make(data)
    img.save(output_file)

if __name__ == "__main__":
    generate_basic_qr("https://github.com/2611ansh?tab=repositories", "github_qr.png")
```

---

### 2. Custom QR Code (Advanced)

**File:** `generate_custom_qr.py`

```python
# generate_custom_qr.py

import qrcode
from PIL import Image

def generate_custom_qr(data, output_file, fill_color="black", back_color="white"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(output_file)

if __name__ == "__main__":
    generate_custom_qr(
        data="https://github.com/2611ansh?tab=repositories",
        output_file="custom_github_qr.png",
        fill_color="red",
        back_color="white"
    )
```

---

## Output

- `github_qr.png` ➜ Basic QR code
- `custom_github_qr.png` ➜ Customized QR code with red fill and white background

---

## 📌 Notes

- `version` controls the size and complexity of the QR code (higher value = bigger QR).
- `error_correction` improves QR readability even if partially damaged.
- `box_size` defines how many pixels each box of the QR code is.
- `border` specifies the width (in boxes) around the QR code.

---

## Connect with Me

🔗 [GitHub Profile](https://github.com/2611ansh?tab=repositories)

---
