from django.contrib import admin
from .models import *


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('author', 'text')


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ProductReview, CommentAdmin)



