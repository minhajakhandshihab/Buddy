# Generated by Django 4.0.3 on 2022-03-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minhajapp', '0009_packages_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quan',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]