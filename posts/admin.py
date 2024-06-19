from django.contrib import admin
from .models import Post, Comment

class CommentAdminInLine(admin.TabularInline):
    model = Comment
    feilds = ["text", "created_at"]

class PostAdmin(admin.ModelAdmin):
    list_display =["id","title", "created_at"]
    inlines = [CommentAdminInLine]

admin.site.register(Post,PostAdmin)
