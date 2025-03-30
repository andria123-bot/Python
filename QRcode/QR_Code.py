import qrcode

def generate_qr_code(link, output_file="qrcode.png"):
    """
    Generates a QR code for the given link and saves it as an image file.

    :param link: The URL or link to encode in the QR code.
    :param output_file: The name of the output image file (default: qrcode.png).
    """
    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code (1 is the smallest)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in the QR code
            border=4,  # Border size around the QR code
        )

        # Add the link to the QR code
        qr.add_data(link)
        qr.make(fit=True)

        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a file
        img.save(output_file)
        print(f"QR code saved as {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Take user input for the link
    link = input("Enter the link to generate a QR code: ")

    # Generate the QR code
    generate_qr_code(link)