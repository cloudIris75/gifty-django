from django.db import models

CATEGORY_CHOICES = (
    ('음료', '음료'),
    ('푸드', '푸드'),
    ('상품', '상품')
)

class Brand(models.Model):
    name = models.CharField(max_length=80)
    img_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Gifticon(models.Model):
    name = models.CharField(max_length=80)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.CharField(max_length=80, choices=CATEGORY_CHOICES)
    img_path = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=80)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.CharField(max_length=80, choices=CATEGORY_CHOICES)
    img_path = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name