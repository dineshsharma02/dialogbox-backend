from django import forms

class FAQUploadForm(forms.Form):
    tenant_id = forms.CharField(label = "Tenant ID",max_length=100)
    csv_file = forms.FileField(label="Upload CSV (question,answer)")