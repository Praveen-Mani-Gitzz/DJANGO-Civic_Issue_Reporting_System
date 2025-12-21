from django import forms
from .models import Complaint
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Reply, ReplyAttachment

# forms for hanldles user input and validations
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = [
            "title",
            "description",
            "category",
            "address",
            "priority",
            "start_date",
            "contact_date",
            "contact_phone",
            "contact_email",
        ]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "contact_date": forms.DateInput(attrs={"type": "date"}),
        }
        
class CustomUserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            
            
class ReplyForm(forms.ModelForm):
    attachments = forms.FileField(required=False)

    class Meta:
#Controls:
# ordering
# verbose_name
# table name
# unique_together
        model = Reply
        fields = ("message",)

    def save_with_files(self, complaint, author, files):
        reply = self.save(commit=False)
        reply.complaint = complaint
        reply.author = author
        reply.save()

        for f in files:
            ReplyAttachment.objects.create(reply=reply, file=f)

        return reply