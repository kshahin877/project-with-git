from django.contrib import admin
from . models import Category,Author,Post 




# Register your models here.
class post(admin.ModelAdmin):
    list_display=["__str__","author","category"]
    class meta:
        model=Post
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post,post)
