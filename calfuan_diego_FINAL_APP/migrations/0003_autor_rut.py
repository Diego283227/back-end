# Generated by Django 4.2.8 on 2023-12-20 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calfuan_diego_FINAL_APP', '0002_rename_nombre_autor_nombres'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='rut',
            field=models.CharField(default='1234', max_length=10),
            preserve_default=False,
        ),
    ]