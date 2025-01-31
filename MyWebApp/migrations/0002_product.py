# Generated by Django 5.1 on 2024-09-29 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWebApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.FileField(upload_to='uploaded_images/')),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('discount', models.IntegerField()),
                ('net_price', models.FloatField()),
            ],
        ),
    ]
