# PDF Image Extractor

This Python script extracts images from a PDF file using pdfminer.six and Pillow libraries.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup

1. Clone this repository or download the script files.

2. Ensure your PDF file is named `file.pdf` and is in the same directory as the script.

3. Install the required packages:

   ```
   pip3 install -r requirements.txt
   ```

## Usage

1. Place your PDF file (named `file.pdf`) in the same directory as the script.

2. Run the script:

   ```
   python3 main.py
   ```

3. The extracted images will be saved in a new directory named `PDF_Images` within the same folder.

## Notes

- The script will extract both standalone images and images within figures.
- Extracted images will be saved in their original format when possible.
- If you encounter any issues, ensure that your PDF file is not encrypted or password-protected.

## License

This project is open source and available under the [MIT License](LICENSE).
