import PyPDF2

def read_pdf_file(file_path):
    # Open the PDF file in binary mode
    with open(file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Get the number of pages in the PDF
        num_pages = len(pdf_reader.pages)

        # Loop through each page and extract text
        for page_num in range(num_pages):
            # Get the page object
            page = pdf_reader.pages[page_num]

            # Extract text from the page
            page_text = page.extract_text()

            # Print or process the extracted text as needed
            print(f"Page {page_num + 1}:\n{page_text}\n")

if __name__ == "__main__":
    # Replace 'path_to_your_pdf.pdf' with the actual file path of your PDF
    file_path = 'path_to_your_pdf.pdf'
    f_path = 'docs/sample.pdf'
    read_pdf_file(f_path)
    # isme loop kro for all files in the folder
    
