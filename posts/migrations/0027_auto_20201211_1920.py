# Generated by Django 3.0.5 on 2020-12-12 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0026_auto_20201211_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(1, 'Used - Like New'), (4, 'Used - Not Usable'), (0, 'Brand New'), (2, 'Used - Good'), (3, 'Used - Poor Condidtion')], default=4),
        ),
    ]