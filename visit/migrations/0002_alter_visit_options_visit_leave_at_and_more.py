# Generated by Django 4.2.1 on 2023-05-23 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visit',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='visit',
            name='leave_at',
            field=models.DateTimeField(null=True, verbose_name='Leave at'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='visit_at',
            field=models.DateTimeField(verbose_name='Visit at'),
        ),
    ]