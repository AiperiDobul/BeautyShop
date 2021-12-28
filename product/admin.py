from django.contrib import admin
from .models import *


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('user', 'text')


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ProductReview, CommentAdmin)



