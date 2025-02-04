from django.contrib import admin
from blog.models import Post, Tag, Comment

class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'likes', 'tags')

class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)

class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('post', 'author')
    list_display = ('author',)

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)