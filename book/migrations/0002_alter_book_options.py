# Generated by Django 4.2.3 on 2023-07-11 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('development', 'Permiso como Desarrollador'), ('scrum_master', 'Permiso como Scrum Master'), ('product_owner', 'Permiso como Product Owner')]},
        ),
    ]