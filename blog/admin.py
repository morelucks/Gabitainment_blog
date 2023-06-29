from django.contrib import admin

# Register your models here.
from .models import Post, Author, Tag, Comment
class PostAdmin(admin.ModelAdmin):
    list_filter=("Author", "tags", "date")
    list_display=("title", "date", "Author")
    prepopulated_fields={"slug":("title",)}

class AuthorAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name","email_address")

class CommentAdmin(admin.ModelAdmin):
    list_display=("user_name", "post")
admin.site.register(Post, PostAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)