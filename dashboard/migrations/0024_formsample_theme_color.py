# Generated by Django 4.2.5 on 2023-11-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_remove_userform_descrition_alter_userform_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsample',
            name='theme_color',
            field=models.CharField(max_length=50, null=True),
        ),
    ]