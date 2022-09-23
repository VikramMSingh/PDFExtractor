# -*- coding: utf-8 -*-
from PyPDF2 import PdfReader
def to_text(path):
    pdf = PdfReader(path)
    pages = pdf.pages
    for page in pages:
        text = page.extract_text()
            #line = text.split("\n")
            #tables = page.extract_tables()
        #self.a.append(line)
        #return self.a
    return text.encode('utf-8')

    
