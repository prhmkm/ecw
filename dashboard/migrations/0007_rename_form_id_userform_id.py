# Generated by Django 4.2.5 on 2023-10-30 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_formtransition_form_formtransition_receiver_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userform',
            old_name='form_id',
            new_name='id',
        ),
    ]
