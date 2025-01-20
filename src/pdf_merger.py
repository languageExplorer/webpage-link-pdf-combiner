import os
from PyPDF2 import PdfMerger, PdfReader


def combine_pdfs(directory_path, output_path, skip_start=0, skip_end=0):
    pdf_merger = PdfMerger()

    pdf_files = sorted(
        [f for f in os.listdir(directory_path) if f.startswith("file") and f.endswith(".pdf")],
        key=lambda x: int(x[4:-4])
    )

    for filename in pdf_files:
        file_path = os.path.join(directory_path, filename)
        reader = PdfReader(file_path)
        num_pages = len(reader.pages)

        start_page = min(skip_start, num_pages)
        end_page = max(num_pages - skip_end, start_page)

        if start_page < end_page:
            pdf_merger.append(file_path, pages=(start_page, end_page))

    pdf_merger.write(output_path)
    pdf_merger.close()
    print(f"PDFs have been combined and saved to {output_path}")
