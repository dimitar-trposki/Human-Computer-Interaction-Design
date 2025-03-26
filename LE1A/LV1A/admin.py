from django.contrib import admin

from LV1A.models import Rating, Genre, Translator, Book, Author


# Register your models here.
class RatingBookInline(admin.TabularInline):
    model = Rating
    extra = 0

    # def has_delete_permission(self, request, obj=None):
    #     if obj is None:
    #         return False
    #     return obj.user == request.user


class RatingAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "rating", "comment")

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class TranslatorAdmin(admin.ModelAdmin):
    list_display = ("name", "nationality", "date_of_birth")


class BookAdmin(admin.ModelAdmin):
    exclude = ("user_added",)

    # list_display = ("name", "author", "genre", "publication_date",
    #                 "user_added", "number_of_pages", "book_cover", "is_available",
    #                 "translators")
    inlines = [RatingBookInline, ]
    list_filter = ("is_available",)

    def save_model(self, request, obj, form, change):
        obj.user_added = request.user
        return super(BookAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user_added == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user_added == request.user:
            return True
        return False


admin.site.register(Genre, GenreAdmin)
admin.site.register(Translator, TranslatorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Rating)
admin.site.register(Author)
