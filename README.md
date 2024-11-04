# pdfTextify
OCR Tool for creating text PDFs from image PDFs (of texts, e.g. old typewriter scans)

Wraps the tesseract program with pyton libraries for PDF processing. Still in progress but can produce some ok text files.

## Prerequisited 
Install to your PATH tesseract (OCR programs) from University of Mannheim.

Then,

``` pip install -r requirements.txt ```


## Usage 
To run the script from the command line:

``` python script_name.py input_images.pdf --output_pdf output_text.pdf --output_txt output_text.txt ```

PDF only: --output_pdf can be provided alone to save only the PDF.
Text file only: Use --output_txt alone to save only the text output.
Both PDF and Text: Specify both --output_pdf and --output_txt to generate both formats.
