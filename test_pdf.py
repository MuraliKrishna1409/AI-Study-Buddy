from pdf_reader import extract_text_from_pdf

pdf_text = extract_text_from_pdf("sample.pdf")

print("\n===== PDF CONTENT =====\n")
print(pdf_text[:1000])