# Generated by Django 2.2.15 on 2020-10-07 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0064_swimlane'),
        ('userstories', '0019_userstory_from_task_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='swimlane',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_stories', to='projects.Swimlane', verbose_name='swimlane'),
        ),
    ]