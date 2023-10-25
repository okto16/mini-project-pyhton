import PyPDF2

pdf = PyPDF2.PdfFileMerger()

# Tambahkan gambar-gambar ke PDF
pdf.append("image1.jpg")
pdf.append("image2.jpg")
# ...

# Simpan sebagai PDF
with open("output.pdf", "wb") as output_pdf:
    pdf.write(output_pdf)