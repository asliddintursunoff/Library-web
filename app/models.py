from django.db import models

class Book(models.Model):
    rasm=models.ImageField(upload_to="images/book" , null=True,blank=True)
    kitob_nomi =models.CharField(max_length=100)
    describtion = models.TextField(help_text="Kitob haqida malumot")
    kitob_pdf = models.FileField(upload_to="pdf/book",null=False,blank=False,help_text="Kitobni kiriting")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.kitob_nomi

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"