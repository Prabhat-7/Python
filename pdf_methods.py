import pypdf as p
import os
def get_text(pdf,page_no=None):
    with open(pdf,"rb") as f:
        reader=p.PdfReader(f)
        txt=[]
        if page_no==None:
            for pages in reader.pages:
                txt.append(pages.extract_text())
            return "\n".join(txt)
        else:
            return reader.pages[page_no-1].extract_text()
def split_all_pages(pdf):
    with open(pdf,"rb") as f:
        reader=p.PdfReader(pdf) #read the pdf
        for i in range(len(reader.pages)): #iterate through each page
            each_page=reader.pages[i] 
            writer=p.PdfWriter() #For each page, create a new PdfWriter object
            writer.add_page(each_page) 
            filename=os.path.basename(pdf)
            output_name=f"{filename.replace(".pdf",)}_{i}.pdf" #filename fpr each of the splitted pdfs
            with open(output_name,"wb") as out:
            #writer: This is an instance of p.PdfWriter that has had a page added to it (writer.add_page(each_page)).
            # write(out): This method writes the content of the PdfWriter object to the file represented by out.

                writer.write(out) 
            print(f"Created a pdf {output_name}")   
def split(pdf,start_page=0,end_page=0,output_name="output.pdf"):
    with open(pdf,"rb") as f:
        reader=p.PdfReader(pdf)
        writer=p.PdfWriter()
        for page_no in range(start_page,end_page):#doesn't include the last page
            page=reader.pages[page_no]
            writer.add_page(page)
        with open(output_name,"wb") as out:
            writer.write(out)
    print(f"Created pdf {output_name}")       


def get_nth_page(pdf,page_no,output_name="output.pdf"):
    with open(pdf,"rb") as f:
        reader=p.PdfReader(pdf)
        writer=p.PdfWriter()
        writer.add_page(reader.pages[page_no-1])
        with open(output_name,"wb") as out:
            writer.write(out)
        print(f"Created a pdf {output_name}")  
def get_page_no(pdf):
    with open(pdf,"rb"):
        return len(p.PdfReader(pdf).pages)
def fetch_all_files(parent_dir:str,extension:str):
    target_files=[]
    for dirpath,dirname,filesname in os.walk(parent_dir):
        for name in filesname:
            if name.endswith(extension):
                target_files.append(name)
    return target_files
def merge_pdf(list_of_files,output_name="merged.pdf"):
    merger=p.PdfWriter()
    with open(output_name,"wb") as f:
        for file in list_of_files:
           merger.append(file)
        merger.write(f)
def rotator(pdf,page_no,rotation):
    reader=p.PdfReader(pdf)
    writer=p.PdfWriter()
    writer.add_page(reader.pages[page_no-1].rotate(rotation))
    with open("rotated_page.pdf","wb") as f:
        writer.write(f)

