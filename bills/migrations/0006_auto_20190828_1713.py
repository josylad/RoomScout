# Generated by Django 2.2.4 on 2019-08-28 21:13

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('bills', '0005_auto_20190828_1712'),
	]

	operations = [
		migrations.AlterField(
			model_name='billset',
			name='month',
			field=models.DateTimeField(),
		),
	]
