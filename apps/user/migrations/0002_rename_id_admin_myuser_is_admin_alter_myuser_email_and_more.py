# Generated by Django 5.0.1 on 2024-02-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='id_admin',
            new_name='is_admin',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_Seller',
            field=models.BooleanField(),
        ),
    ]
