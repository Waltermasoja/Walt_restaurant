from django.contrib import admin
from .models import product,post,choice,chat_comment,chat_post

admin.site.register(product)
admin.site.register(post)
admin.site.register(choice)
admin.site.register(chat_post)
admin.site.register(chat_comment)


