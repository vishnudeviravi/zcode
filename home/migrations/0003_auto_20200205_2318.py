# Generated by Django 3.0.3 on 2020-02-05 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200204_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='hashtags',
        ),
        migrations.AddField(
            model_name='product',
            name='hashtags1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='hashtags2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='hashtags3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='hashtags4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='hashtags5',
            field=models.TextField(blank=True, null=True),
        ),
    ]
