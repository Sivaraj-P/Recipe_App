# Generated by Django 4.1.5 on 2023-07-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reciepe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reciepe_details',
            name='food_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]