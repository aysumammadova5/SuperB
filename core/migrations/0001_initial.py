# Generated by Django 4.1.1 on 2023-01-23 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('company', models.CharField(max_length=100, verbose_name='Company')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('address', models.TextField(verbose_name='Address')),
                ('comment', models.TextField(verbose_name='Comment')),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
    ]
