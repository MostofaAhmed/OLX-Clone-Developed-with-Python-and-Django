# Generated by Django 3.0.3 on 2020-03-25 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20200324_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='main_product/'),
        ),
    ]
