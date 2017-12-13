from django.db import models

class USER(models.Model):
	email = models.CharField('email',max_length=20, unique=True)
	pw = models.CharField('pw',max_length=10)
	name = models.CharField('name',max_length=30)

class SESSION(models.Model):
	id_USER = models.ForeignKey(USER, on_delete=models.CASCADE)
	sess = models.CharField('sess', max_length=30, unique=True)
	class Meta:
		unique_together = (('id_USER', 'sess',))
