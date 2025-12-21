from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ComplaintForm,  CustomUserRegisterForm
from .models import Complaint, Attachment
from django.contrib.auth import login
from .forms import CustomUserRegisterForm

from django.contrib.admin.views.decorators import staff_member_required
from .forms import ReplyForm
from .models import Complaint, ReplyAttachment

def register_view(request):
    if request.method == "POST":
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserRegisterForm()
    return render(request, "registration/register.html", {"form": form})

def home(request):
    return render(request, 'citygram/home.html')




@login_required
def create_complaint(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST, request.FILES)
        files = request.FILES.getlist("attachments")
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.reporter = request.user
            complaint.save()
            for f in files:
                Attachment.objects.create(complaint=complaint, file=f)
            return redirect("my_complaints")
    else:
        form = ComplaintForm()
    return render(request, "complaint_form.html", {"form": form})


@login_required
def my_complaints(request):
    complaints = Complaint.objects.filter(reporter=request.user).order_by("-created_at")
    return render(request, "my_complaints.html", {"complaints": complaints})



@staff_member_required
def reply_to_complaint(request, complaint_id):
    complaint = Complaint.objects.get(id=complaint_id)
    if request.method == "POST":
        form = ReplyForm(request.POST, request.FILES)
        files = request.FILES.getlist("attachments")
        if form.is_valid():
            form.save_with_files(complaint, request.user, files)
           
            return redirect("admin:citygram_complaint_change", complaint.id) 
    else:
        form = ReplyForm()
    return render(request, "reply_to_complaint.html", {"form": form, "complaint": complaint})