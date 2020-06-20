# Generated by Django 3.0.7 on 2020-06-20 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200620_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='FigurativePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('figurative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Figurative')),
            ],
        ),
    ]
