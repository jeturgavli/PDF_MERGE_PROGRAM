import os
from PyPDF2 import PdfMerger

def merge_pdfs(input_folder, output_folder):
    merger = PdfMerger()

    pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]

    pdf_files.sort()

    for pdf_file in pdf_files:
        merger.append(os.path.join(input_folder, pdf_file))

    output_filename = os.path.join(output_folder, 'MERG_0001.pdf')
    serial_number = 1
    while os.path.exists(output_filename):
        serial_number += 1
        output_filename = os.path.join(output_folder, f'MERG_{serial_number:04d}.pdf')

    with open(output_filename, 'wb') as output:
        merger.write(output)

    merger.close()

# Loop to continue merging until user decides to stop
while True:
    print("This Is PDF MERGE Program \n")
    input_folder = input("Enter the folder path containing the PDF files: ")

    if not os.path.isdir(input_folder):
        print("Error: The specified folder does not exist.")
        continue

    program_directory = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(program_directory, 'OutputFolder')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    merge_pdfs(input_folder, output_folder)
    print("PDF files merged successfully!")

    choice = input("Do you want to merge more PDFs? (Y/N): ").strip().lower()
    if choice != 'y':
        break
