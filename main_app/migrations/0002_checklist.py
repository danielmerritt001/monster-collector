# Generated by Django 4.2.1 on 2023-05-31 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('task', models.CharField(choices=[('C', 'Spook the Children'), ('A', 'Avoid Capture'), ('S', 'Setup the Sequel')], default='C', max_length=1)),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.monster')),
            ],
        ),
    ]