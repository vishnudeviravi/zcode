# Generated by Django 3.0.3 on 2020-02-06 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200205_2356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AddField(
            model_name='product',
            name='upvote',
            field=models.IntegerField(default=1),
        ),
    ]
