# Generated by Django 4.2.3 on 2023-08-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("subjects", "0001_initial"),
        ("courses", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="subjects",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="courses",
                to="subjects.subject",
                verbose_name="Предметы",
            ),
        ),
    ]
