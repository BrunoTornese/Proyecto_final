# Generated by Django 4.0.5 on 2022-08-03 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajeria', '0004_alter_mensaje_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
