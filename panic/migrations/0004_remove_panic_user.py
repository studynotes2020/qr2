# Generated by Django 4.2.1 on 2023-05-31 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panic', '0003_remove_panic_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panic',
            name='user',
        ),
    ]
