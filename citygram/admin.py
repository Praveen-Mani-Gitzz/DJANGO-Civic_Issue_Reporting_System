
from django.contrib import admin
from .models import Complaint, Attachment, Reply, ReplyAttachment

class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 0
    readonly_fields = ("preview",)

class ReplyAttachmentInline(admin.TabularInline):
    model = ReplyAttachment
    extra = 0
    readonly_fields = ()



class ReplyInline(admin.StackedInline):
    model = Reply
    extra = 0
    inlines = [ReplyAttachmentInline]  

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "priority", "status", "reporter", "created_at")
    list_filter = ("status", "category", "priority")
    search_fields = ('title', 'description', 'reporter__username')
    inlines = [AttachmentInline]  

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ("complaint", "author", "created_at")
    search_fields = ("message", "complaint__title")
    inlines = [ReplyAttachmentInline]

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("id", "complaint", "file")
