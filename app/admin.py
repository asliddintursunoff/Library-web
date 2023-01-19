from django.contrib import admin

# Register your models here.



from .models import Book



class BookAdmin(admin.ModelAdmin):
    list_display = ['kitob_nomi',"rasm","kitob_pdf"]
    list_filter = ('kitob_nomi',"time")
    list_per_page = 10
    search_fields = ['kitob_nomi']

    class Meta:
        model = Book


admin.site.register(Book, BookAdmin)
