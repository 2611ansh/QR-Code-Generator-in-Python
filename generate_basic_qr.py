"""
Basic QR Code Generator
This script generates a simple QR code with default settings.
"""

import qrcode

def generate_basic_qr(data, output_file):
    """
    Generates a basic QR code.

    Args:
        data (str): The data or URL to encode into the QR code.
        output_file (str): The filename where the QR code image will be saved.
    """
    img = qrcode.make(data)
    img.save(output_file)

if __name__ == "__main__":
    # Example usage
    generate_basic_qr(
        data="https://github.com/2611ansh?tab=repositories",
        output_file="github_qr.png"
    )
