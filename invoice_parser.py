from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
from pathlib import Path
import shutil
from datetime import datetime

class invoiceParser:
    def __init__(self, path):
        self.path = path
    
    def getPdfData(self):
        #self.templ = templ
        templates = read_templates(fr'path/Template/')
        self.result = extract_data(f'{self.path}',templates=templates)
        return self.result

    #def validateResults(self):
    #    total = self.result['amount']
    #    to_validate = self.result['lines'][0].get('charges')
    #    #return float(total)
    #    a = to_validate.split('\n')
    #    for i in range(len(a)):
    #        a[i] = float(a[i])
    #    if round(sum(a),2) == total:
    #        return "Validation successful"
    #    else:
    #        return "Total and charge mismatch"

    def validationofres(self):
        for fields in self.result:
            if self.result[fields] is None:
                return f"Null Values in invoice {self.result['issuer']}"
        return self.result
    
    def moveProcessed(self, pr_path):
        self.pr_path = pr_path
        shutil.move(self.path, self.pr_path)

