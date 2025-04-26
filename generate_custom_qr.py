# generate_custom_qr.py

import qrcode
from PIL import Image

def generate_custom_qr(data, output_file, fill_color="black", back_color="white", box_size=10, border=4):
    """
    Generates a customized QR code.

    Args:
        data (str): The data or URL to encode.
        output_file (str): The output file name.
        fill_color (str, optional): Color of the QR code. Defaults to 'black'.
        back_color (str, optional): Background color. Defaults to 'white'.
        box_size (int, optional): Size of each QR box. Defaults to 10.
        border (int, optional): Border size. Defaults to 4.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
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
        back_color="white",
        box_size=12,
        border=6
    )