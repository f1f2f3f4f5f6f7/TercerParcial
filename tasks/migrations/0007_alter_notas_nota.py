# Generated by Django 4.2.7 on 2023-11-20 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_notas_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notas',
            name='nota',
            field=models.FloatField(),
        ),
    ]
