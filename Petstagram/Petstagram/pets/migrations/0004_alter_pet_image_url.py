# Generated by Django 3.2.3 on 2021-07-12 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_auto_20210624_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image_url',
            field=models.FileField(upload_to=''),
        ),
    ]
