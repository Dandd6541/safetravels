# Generated by Django 4.1 on 2022-08-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_trip_cityfrom'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('relation', models.CharField(choices=[('F', 'Family'), ('FR', 'Friends'), ('S', 'Spouse'), ('SO', 'Significant Other'), ('O', 'Other')], default='Family', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='peoples',
            field=models.ManyToManyField(to='main_app.people'),
        ),
    ]
