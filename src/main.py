import asyncio
import shutil

from get_internal_links import get_internal_links
from filter_strings import filter_strings
from convert_to_pdf import print_page_to_pdf
from pdf_merger import combine_pdfs

# Define URL and output path
url = "" # ⚠️ Write the URL here
output_pdf_path = "" # ⚠️ Write the output path here

urls_to_print = filter_strings(url, get_internal_links(url))

print("\n".join(urls_to_print))

for i in range(0, len(urls_to_print)):
    asyncio.run(print_page_to_pdf(urls_to_print[i], "/tmp/pdfs_to_combine/file" + str(i) + ".pdf"))

combine_pdfs("/tmp/pdfs_to_combine/", output_pdf_path, 1 ,1)

shutil.rmtree("/tmp/pdfs_to_combine/", ignore_errors=True)

