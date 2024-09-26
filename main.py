import io
import os
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTImage, LTFigure
from PIL import Image

def save_image(lt_image, output_dir, page_num, image_num):
    if lt_image.stream:
        file_stream = io.BytesIO(lt_image.stream.get_data())
        try:
            img = Image.open(file_stream)
            image_name = f'image_p{page_num}_{image_num}.{img.format.lower()}'
            img.save(os.path.join(output_dir, image_name))
            print(f"Saved: {image_name}")
        except Exception as e:
            print(f"Error saving image: {e}")

def extract_images(pdf_path, output_dir):
    image_count = 0
    for page_num, page_layout in enumerate(extract_pages(pdf_path), start=1):
        for element in page_layout:
            if isinstance(element, LTImage):
                image_count += 1
                save_image(element, output_dir, page_num, image_count)
            elif isinstance(element, LTFigure):
                for figure_element in element:
                    if isinstance(figure_element, LTImage):
                        image_count += 1
                        save_image(figure_element, output_dir, page_num, image_count)

def main():
    print("PDF Image Extractor")
    print("==================")

    # Get the current directory (where main.py is located)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_filename = "file.pdf"
    pdf_path = os.path.join(current_dir, pdf_filename)

    # Check if file exists
    if not os.path.isfile(pdf_path):
        print(f"Error: The file '{pdf_filename}' does not exist in the current directory.")
        return

    # Create output directory
    output_dir = os.path.join(current_dir, "PDF_Images")
    os.makedirs(output_dir, exist_ok=True)

    # Extract images
    extract_images(pdf_path, output_dir)
    print(f"\nImage extraction complete. Images saved in: {output_dir}")

if __name__ == "__main__":
    main()