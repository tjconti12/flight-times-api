# Generated by Django 4.0.2 on 2022-02-15 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='city',
            field=models.CharField(default='Florida', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airport',
            name='state',
            field=models.CharField(default='Florida', max_length=20),
            preserve_default=False,
        ),
    ]
