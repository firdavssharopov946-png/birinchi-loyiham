from django.db import models

class Mahsulot(models.Model):
    nomi = models.CharField(max_length=100)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    miqdori = models.IntegerField()

    def __str__(self):
        return self.nomi
class Mijoz(models.Model):
    ism = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20, null=True, blank=True)
    manzil = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.ism
class Mahsulot(models.Model):
    nomi = models.CharField(max_length=100)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    # Bo'sh qolishiga ruxsat berish:
    miqdori = models.IntegerField(null=True, blank=True, default=0)


class Buyurtma(models.Model):
    mijoz_nomi = models.CharField(max_length=255)
    telefon = models.CharField(max_length=20)
    mahsulot_nomi = models.CharField(max_length=255)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    sana = models.DateTimeField(auto_now_add=True)
    holat = models.CharField(max_length=50, default="Kutilmoqda")

    def __str__(self):
        return self.mijoz_nomi