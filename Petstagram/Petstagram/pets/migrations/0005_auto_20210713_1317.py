# Generated by Django 3.2.3 on 2021-07-13 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_alter_pet_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='image_url',
        ),
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(default=None, upload_to='images/pets'),
        ),
    ]
