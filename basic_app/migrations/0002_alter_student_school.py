# Generated by Django 4.2.5 on 2023-09-22 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(default='FIRST', on_delete=django.db.models.deletion.CASCADE, related_name='students', to='basic_app.school'),
        ),
    ]
