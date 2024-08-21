#!/Users/yz/github/myenv/bin/python

from PyPDF2 import PdfReader
# Open a PDF file
with open("US_Applicant_Privacy_Notice_2.pdf", "rb") as file:
    pdf = PdfReader(file)
    metadata = pdf.metadata

print (metadata)
# Print PDF metadata
print(f"Title: {metadata.title}")
print(f"Author: {metadata.author}")
print(f"Creator: {metadata.creator}")
print(f"Created Date: {metadata['/CreationDate']}")
print(f"Modified Date: {metadata['/ModDate']}")

###################### Modify Metadata ######################
import pikepdf
# Open the PDF file
with pikepdf.Pdf.open("US_Applicant_Privacy_Notice_2.pdf") as pdf:
    # Access the metadata
    metadata = pdf.docinfo
    # Modify metadata fields
    metadata["/Title"] = "Updated Privacy Notice"
    metadata["/Author"] = "Elaine Zhou"
    metadata["/Subject"] = "Privacy Notice for US Applicants"
    metadata["/Keywords"] = "privacy, notice, US, applicants"
    if "/Creator" in metadata:
        del metadata["/Creator"]
    # Save the updated PDF with the modified metadata
    pdf.save("US_Applicant_Privacy_Notice_2_updated.pdf")

######################## Verify ###########################
with open("US_Applicant_Privacy_Notice_2_updated.pdf", "rb") as file:
    pdf = PdfReader(file)
    metadata = pdf.metadata

print (metadata)
print(f"Title: {metadata.title}")
print(f"Author: {metadata.author}")
print(f"Creator: {metadata.creator}")
print(f"Created Date: {metadata['/CreationDate']}")
print(f"Modified Date: {metadata['/ModDate']}")