# Generated by Django 2.2 on 2021-04-24 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='tenant_node',
        ),
        migrations.DeleteModel(
            name='ClientNode',
        ),
    ]
