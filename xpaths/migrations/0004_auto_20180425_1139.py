# Generated by Django 2.0.3 on 2018-04-25 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpaths', '0003_xpathlist_product_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xpathlist',
            name='product_url',
            field=models.CharField(max_length=1000),
        ),
    ]
