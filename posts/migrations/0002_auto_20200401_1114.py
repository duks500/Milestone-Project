# Generated by Django 3.0 on 2020-04-01 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(1, 'Used - Like New'), (3, 'Used - Poor Condidtion'), (2, 'Used - Good'), (0, 'Brand New'), (4, 'Used - Not Usable')], default=4),
        ),
    ]