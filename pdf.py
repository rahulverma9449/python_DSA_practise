# import aspose.words as aw

# fileNames = [ "Input1.pdf", "Input2.pdf" ]

# output = aw.Document()
# # Remove all content from the destination document before appending.
# output.remove_all_children()

# for fileName in fileNames:
#     input = aw.Document(fileName)
#     # Append the source document to the end of the destination document.
#     output.append_document(input, aw.ImportFormatMode.KEEP_SOURCE_FORMATTING)

# output.save("Output.pdf")

from pypdf import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()