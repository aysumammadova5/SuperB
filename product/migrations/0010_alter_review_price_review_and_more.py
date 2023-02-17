# Generated by Django 4.1.2 on 2023-01-30 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_review_price_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='price_review',
            field=models.IntegerField(choices=[(5, '100'), (3, '60'), (2, '40'), (1, '20'), (4, '80')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='quality_review',
            field=models.IntegerField(choices=[(5, '100'), (3, '60'), (2, '40'), (1, '20'), (4, '80')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='value_review',
            field=models.IntegerField(choices=[(5, '100'), (3, '60'), (2, '40'), (1, '20'), (4, '80')]),
        ),
    ]
