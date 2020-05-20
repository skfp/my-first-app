from django import forms

class ExcelUploadForm(forms.Form):
    csv_file=forms.FileField(label="select a file with words list")




#(upload_to('static/data/')) 