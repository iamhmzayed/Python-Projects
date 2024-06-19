#Project_3_PDF_MERGER

from PyPDF2 import PdfMerger

allpdf = ["1.pdf", "2.pdf"]

merger = PdfMerger()

for pdf in allpdf:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
