from django.db.models.signals import pre_save, pre_delete, post_save, post_delete 
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
from gemini_api.client import car_gemini_ai


def car_inventory_update():
    cars_count = Car.objects.all().count() # Calcula a quantidade de carros que tem no estoque
    cars_value = Car.objects.aggregate( # Calcula o valor total da soma dos carros em estoque
        total_value=Sum('value')
    )['total_value']
    CarInventory.objects.create( # Cria na tabela 
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio: 
        ai_bio = car_gemini_ai( instance.model, instance.brand, instance.factory_year )
        instance.bio = ai_bio


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()