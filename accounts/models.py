from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	GENDER_CHOICES = [('m', 'Male'), ('f', 'Female'), ('o', 'Other')]

	#Contact
	phone_number = models.CharField(max_length=20, default='')
	phone_number_verified = models.BooleanField(default=False)

	#Address
	city = models.CharField(default='', max_length=200)
	prov_state = models.CharField(default='', max_length=2)

	#User Data
	gender = models.CharField(choices=GENDER_CHOICES, default='', max_length = 2)
	age = models.IntegerField(default=0)

	score = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)

	#Premium Features
	max_houses = models.IntegerField(default=1)
