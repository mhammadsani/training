# Generated by Django 4.2.5 on 2023-10-10 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_attempter_management', '0006_alter_mark_options_rename_marks_mark_mark'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mark',
            options={'ordering': ['-marks']},
        ),
        migrations.RenameField(
            model_name='mark',
            old_name='mark',
            new_name='marks',
        ),
    ]
