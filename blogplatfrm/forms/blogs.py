from django import forms
from blogplatfrm.models import User
    
class BlogEntryForm(forms.Form):
    title = forms.CharField(max_length=200,required=True)
    content = forms.Textarea() 