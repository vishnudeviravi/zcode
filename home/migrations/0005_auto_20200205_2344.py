# Generated by Django 3.0.3 on 2020-02-05 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200205_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtags',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.Product')),
                ('hashtags1', models.TextField(blank=True)),
                ('hashtags2', models.TextField(blank=True)),
                ('hashtags3', models.TextField(blank=True)),
                ('hashtags4', models.TextField(blank=True)),
                ('hashtags5', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='hashtags1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='hashtags2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='hashtags3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='hashtags4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='hashtags5',
        ),
    ]
