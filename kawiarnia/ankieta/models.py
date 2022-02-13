from django.db import models

# Create your models here.
class Pytanie(models.Model):
    tekst_pytania=models.CharField(max_length=300)
    data_publikacji=models.DateTimeField('data publikacji')
    obraz=models.CharField(max_length=300,default='brak.jpg')
    
    def __str__(self):
        return self.tekst_pytania.upper()
    
    class Meta:
        verbose_name = "Pytanie"
        verbose_name_plural ="Pytania"
    
class Odpowiedz(models.Model):
    pytanie=models.ForeignKey(Pytanie,on_delete=models.CASCADE)
    tekst_dpowiedzi=models.CharField(max_length=400)
    glosy=models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.tekst_dpowiedzi.upper()} - il. głosów: {self.glosy}'
    
    class Meta:
        verbose_name = "Odpowidź"
        verbose_name_plural ="Odpowiedzi"