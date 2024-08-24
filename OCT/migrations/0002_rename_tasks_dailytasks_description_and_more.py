# Generated by Django 4.2.5 on 2023-09-23 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('OCT', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailytasks',
            old_name='tasks',
            new_name='description',
        ),
        migrations.AddField(
            model_name='monthlytasks',
            name='description',
            field=models.TextField(default='asd'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dailytasks',
            name='goal_related_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goal_related_to', to='OCT.monthlytasks'),
        ),
        migrations.AlterField(
            model_name='oct',
            name='daily_tasks',
            field=models.ManyToManyField(null=True, to='OCT.dailytasks'),
        ),
        migrations.AlterField(
            model_name='oct',
            name='monthly_tasks',
            field=models.ManyToManyField(null=True, to='OCT.monthlytasks'),
        ),
        migrations.AlterField(
            model_name='oct',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='octuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
