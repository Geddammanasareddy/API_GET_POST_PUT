from django.db import models

# Create your models here.
class Product_category(models.Model):
    Pcid=models.IntegerField()
    Pcname=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Pcname
    

class Product(models.Model):  
    Pcname=models.ForeignKey(Product_category,on_delete=models.CASCADE)
    Pid=models.IntegerField()
    Pname=models.CharField(max_length=100)
    Pprice=models.DecimalField(max_digits=8,decimal_places=2)
    Pdescription=models.CharField(max_length=100)
    Pdate=models.DateField()

    def __str__(self):
        return self.Pname
        