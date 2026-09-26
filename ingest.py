import pymupdf
import os
##(extract > chunk > embed > store > retrieve) full pipeline 
def extract_text_from_pdf(filepath): #works on one file like "papers/TPLogAD.pdf"
    doc=pymupdf.open(filepath)
    full_text=""
    for page in doc:
        full_text+=page.get_text()
    doc.close()
    return full_text

def load_all_papers(folder='papers'): # finds every pdf in the folder
    papers={}
    for filename in os.listdir(folder): #returns a list of everything in papers folder
        if filename.endswith('.pdf'):
            filepath=os.path.join(folder,filename) #build full path to the file.
            text=extract_text_from_pdf(filepath) #call 1st func
            papers[filename]=text
    return papers

if __name__ == "__main__":
    all_papers=load_all_papers()
    print(f"\nLoaded {len(all_papers)} papers.")
    for filename, text in all_papers.items():
        print(f"{filename}: {len(text)} characters")

