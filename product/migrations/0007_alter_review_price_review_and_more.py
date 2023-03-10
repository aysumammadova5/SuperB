# Generated by Django 4.1.2 on 2023-01-30 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_review_price_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='price_review',
            field=models.IntegerField(choices=[(1, '20'), (4, '80'), (2, '40'), (3, '60'), (5, '100')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='quality_review',
            field=models.IntegerField(choices=[(1, '20'), (4, '80'), (2, '40'), (3, '60'), (5, '100')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='value_review',
            field=models.IntegerField(choices=[(1, '20'), (4, '80'), (2, '40'), (3, '60'), (5, '100')]),
        ),
    ]
