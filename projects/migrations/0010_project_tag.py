# Generated by Django 4.0.3 on 2022-07-05 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_review_project_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='project_tag', to='projects.tag'),
        ),
    ]
