# Generated by Django 4.1.2 on 2023-02-01 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_review_price_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='price_review',
            field=models.IntegerField(choices=[(3, '60'), (4, '80'), (1, '20'), (5, '100'), (2, '40')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='quality_review',
            field=models.IntegerField(choices=[(3, '60'), (4, '80'), (1, '20'), (5, '100'), (2, '40')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='value_review',
            field=models.IntegerField(choices=[(3, '60'), (4, '80'), (1, '20'), (5, '100'), (2, '40')]),
        ),
    ]