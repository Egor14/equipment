# Generated by Django 2.2 on 2019-04-28 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190428_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.Dealer'),
        ),
    ]
