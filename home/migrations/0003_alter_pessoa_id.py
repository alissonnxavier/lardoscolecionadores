# Generated by Django 4.0.5 on 2022-07-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_pessoa_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
