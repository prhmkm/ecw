# Generated by Django 4.2.5 on 2023-09-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_rename_descrition_formsample_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formtransition',
            name='form',
        ),
        migrations.AddField(
            model_name='userform',
            name='transitions',
            field=models.ManyToManyField(to='dashboard.formtransition'),
        ),
    ]
