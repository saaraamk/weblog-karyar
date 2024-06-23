from django.contrib import admin
from .models import Post, Comment, Author, Like


# class CommentAdminInLine(admin.TabularInline):
#     model = Comment
#     feilds = ["text", "created_at"]

# class PostAdmin(admin.ModelAdmin):
#     list_display =["id","title", "created_at"]
#     inlines = [CommentAdminInLine]

# admin.site.register(Post,PostAdmin)

class AuthorAdmin(admin.ModelAdmin):
    feilds = ["user_name", "created_at"]

admin.site.register(Author, AuthorAdmin)


class PostAdmin(admin.ModelAdmin):
    feilds = ["text", "created_at"]

admin.site.register(Post, PostAdmin)

admin.site.register(Comment)

admin.site.register(Like)
