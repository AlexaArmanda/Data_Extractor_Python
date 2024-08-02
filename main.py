import re 
import fitz
import PIL.Image
import io
import tabula
import pandas
from pdfminer.high_level import extract_pages, extract_text

# Extract content 

for pg_layout in extract_pages("State_Of_Hedgehogs.pdf"):
    for element in pg_layout:
        print(element)


# Extract text based on RegEx pattern 

text = extract_text("State_Of_Hedgehogs.pdf")
print(text)
pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = pattern.findall(text)
print(matches)

# Extract images from PDF

pdf = fitz.open("State_Of_Hedgehogs.pdf")
counter=1
for i in range(len(pdf)):
    page=pdf[i]
    images = page.get_images()
    for image in images:
        base_image=pdf.extract_image(image[0])
        print(base_image)
        image_data = base_image["image"]
        img = PIL.Image.open(io.BytesIO(image_data))
        extension = base_image["ext"]
        img.save(open(f"image{counter}.{extension}", "wb"))
        counter +=1

# Extract tables from PDF

page_nr=4
pages=page_nr
tables =tabula.read_pdf("table.pdf")
df = tables[0]
print(df[df.Participants > 3])
print(tables)