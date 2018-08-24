# Generated by Django 2.0.6 on 2018-08-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='Enter Descriptio')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(default='generic_product.png', upload_to='product_images')),
            ],
        ),
    ]
