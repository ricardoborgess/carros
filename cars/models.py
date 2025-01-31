from django.db import models

class Brand(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True) # Se auto encrementa
    model = models.CharField(max_length=200) # Campo de texto 
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True) # Numero inteiro
    model_year = models.IntegerField(blank=True, null=True) # Numero inteiro
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True) # Numero real
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.model


class CarInventory(models.Model):
    cars_count = models.IntegerField() # Armazena quantos carros tem no estoque
    cars_value = models.FloatField()  # Armazena os valores de todos os carros do estoque
    created_at = models.DateTimeField(auto_now_add=True) # Armazena data e hora que foi criado o registro

    class Meta:
        ordering = ['-created_at'] # Vai ordenar de ordem decrescente


    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'
