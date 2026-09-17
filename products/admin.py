from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "product_type",
        "stock",
        "is_featured",
        "is_active",
        "created_at",
    )
    list_filter = (
        "category",
        "product_type",
        "is_featured",
        "is_active",
    )
    search_fields = (
        "name",
        "description",
        "theme",
    )
    prepopulated_fields = {"slug": ("name",)}
    list_editable = (
        "price",
        "stock",
        "is_featured",
        "is_active",
    )
    ordering = ("-created_at",)