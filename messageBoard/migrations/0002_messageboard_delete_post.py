# Generated by Django 4.1.3 on 2022-11-02 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageBoard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
