import pdfplumber
import pandas as pd
import re

def bbva2Excl(pdf_path):
    movimientos = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            for line in text.split('\n'):
                match = re.match()