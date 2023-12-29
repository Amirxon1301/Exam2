from django.db import models





class Suv(models.Model):
    brend = models.CharField(max_length=30)
    narx = models.PositiveIntegerField()
    litr = models.PositiveIntegerField()
    batafsil = models.TextField()

class Mijoz(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    manzil = models.CharField(max_length=40)
    qarz = models.PositiveIntegerField()
    user = models.CharField(max_length=30)

class Admin(models.Model):
    ism = models.CharField(max_length=39)
    yosh = models.PositiveIntegerField()
    ish_vaqti = models.CharField(max_length=30)
    user = models.CharField(max_length=30)

class Haydovchi(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    kiritilgan_sana = models.DateField()

class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
    sana = models.DateField()
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdor = models.PositiveIntegerField()
    umumiy_narx = models.PositiveIntegerField()
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)



