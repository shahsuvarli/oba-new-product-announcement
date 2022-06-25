from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class ProcessFlow(models.Model):
	display_name = models.CharField(max_length=100)
	sends_to_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
	responsible_person = models.CharField(max_length=100)

	def __str__(self):
		return self.display_name


class Product(models.Model):
	barcode = models.CharField(max_length=100)
	product_name = models.CharField(max_length=100)
	created_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	pending = models.CharField(max_length=100)


class BlogModel(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	assigned_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=100)
	text = models.TextField()

	def __str__(self):
		return self.title