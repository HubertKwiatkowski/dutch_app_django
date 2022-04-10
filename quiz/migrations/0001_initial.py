# Generated by Django 4.0.3 on 2022-04-10 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polish', models.CharField(max_length=50)),
                ('dutch', models.CharField(max_length=50)),
                ('het_article', models.BooleanField(default=False)),
                ('de_article', models.BooleanField(default=False)),
                ('favourite', models.BooleanField(default=False)),
            ],
        ),
    ]