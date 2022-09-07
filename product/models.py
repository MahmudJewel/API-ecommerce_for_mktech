from django.db import models

# Create your models here.

class product(models.Model):
	name =models.CharField(max_length=50)
	stock = models.PositiveIntegerField()
	price = models.PositiveIntegerField()
	img1 =models.ImageField(default="product/default.png", upload_to="product/", null=True, blank=True)
	img2 =models.ImageField(default="product/default.png", upload_to="product/", null=True, blank=True)

	def __str__(self):
		return self.name

