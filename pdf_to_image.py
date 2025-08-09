from pdf2image import convert_from_path

def pdf_to_image(pdf_path, image_path):
    pages = convert_from_path(pdf_path, dpi=200)
    # Save the first page as image
    pages[0].save(image_path, 'PNG')
    print(f"Image saved: {image_path}")