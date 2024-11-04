import fitz  
from PIL import Image
import pytesseract
from reportlab.pdfgen import canvas
from io import BytesIO
import argparse

def pdf_to_text_pdf(input_pdf_path, output_pdf_path=None, output_txt_path=None):
    # Open the input PDF
    doc = fitz.open(input_pdf_path)
    text_output = []

    # Process each page
    for page_number in range(doc.page_count):
        page = doc[page_number]
        
        # Extract images from the page
        image_list = page.get_images(full=True)
        if not image_list:
            continue

        for img_index, img_info in enumerate(image_list):
            xref = img_info[0]
            base_image = doc.extract_image(xref)
            img_data = base_image["image"]
            
            # Convert to PIL Image for OCR
            img = Image.open(BytesIO(img_data))

            # Perform OCR on the image
            text = pytesseract.image_to_string(img)
            text_output.append(f"Page {page_number + 1} Image {img_index + 1}:\n{text}\n")

    # Save to text file if specified
    if output_txt_path:
        with open(output_txt_path, 'w', encoding='utf-8') as f:
            f.writelines(text_output)
        print(f"OCR text saved to {output_txt_path}")

    # Save to PDF if specified
    if output_pdf_path:
        c = canvas.Canvas(output_pdf_path)
        text = c.beginText(40, 800)
        text.setFont("Helvetica", 10)

        for line in text_output:
            text.textLine(line)
            if text.getY() < 40:  # Move to the next page if the text gets too low
                c.drawText(text)
                c.showPage()
                text = c.beginText(40, 800)
                text.setFont("Helvetica", 10)

        c.drawText(text)
        c.save()
        print(f"OCR PDF saved to {output_pdf_path}")

# Command-line interface
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a PDF of images to text using OCR.")
    parser.add_argument("input_pdf", help="Path to the input PDF file.")
    parser.add_argument("--output_pdf", help="Path to the output PDF file.", default=None)
    parser.add_argument("--output_txt", help="Path to the output TXT file.", default=None)
    
    args = parser.parse_args()
    
    # Run the function with specified arguments
    pdf_to_text_pdf(args.input_pdf, args.output_pdf, args.output_txt)
