# Generated by Django 4.0.5 on 2022-08-03 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajeria', '0003_alter_mensaje_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
