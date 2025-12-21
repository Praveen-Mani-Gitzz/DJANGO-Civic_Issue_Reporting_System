from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.html import format_html



class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ("Road", "Road"),
        ("Water", "Water"),
        ("Electricity", "Electricity"),
        ("Garbage", "Garbage"),
        ("Sewage", "Sewage"),
        ("Street Light", "Street Light"),
        ("Public Park", "Public Park"),
        ("Drainage", "Drainage"),
        ("Traffic", "Traffic"),
        ("Others", "Others"),
    ]

    PRIORITY_CHOICES = [
        ("One Day", "Within a day"),
        ("One Week", "Within a week"),
        ("One Month", "Within a month"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
        ("Delayed", "Delayed"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    address = models.CharField(max_length=250)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)

    start_date = models.DateField(null=True, blank=True)
    contact_date = models.DateField(null=True, blank=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")

    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class Attachment(models.Model):
    complaint = models.ForeignKey(
        Complaint, 
        on_delete=models.CASCADE, 
        related_name="attachments"
    )
    file = models.FileField(upload_to="attachments/")

    def preview(self):
        url = self.file.url.lower()

        if url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            return format_html('<img src="{}" style="height:80px;border-radius:6px;">', self.file.url)

        if url.endswith(('.mp4', '.mov', '.avi', '.mkv')):
            return format_html(
                '<video width="150" controls>'
                '  <source src="{}" type="video/mp4">'
                '</video>',
                self.file.url
            )
        return "File"

    preview.short_description = "Preview"



class Reply(models.Model):
    complaint = models.ForeignKey(
        Complaint,
        on_delete=models.CASCADE,
        related_name="replies"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        snippet = (self.message[:50] + "...") if len(self.message) > 50 else self.message
        return f"Reply to {self.complaint.title} — {snippet}"


class ReplyAttachment(models.Model):
    reply = models.ForeignKey(
        Reply,
        on_delete=models.CASCADE,
        related_name="attachments"
    )
    file = models.FileField(upload_to="reply_attachments/")

    def is_image(self):
        return self.file.name.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp"))

    def is_video(self):
        return self.file.name.lower().endswith((".mp4", ".mov", ".avi", ".mkv"))
