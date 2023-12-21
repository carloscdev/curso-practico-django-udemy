from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated") # campos de solo lectura
    list_display = ("title", "author", "published", "post_categories") # que campos se muestran en la lista
    ordering = ("author", "published") # orden de los campos
    search_fields = ("title", "content", "author__username", "categories__name") # campos por los que se puede buscar
    date_hierarchy = "published" # jerarquia de fechas
    list_filter = ("author__username", "categories__name") # filtros

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")]) # devuelve las categorias separadas por comas

    post_categories.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)