# Generated by Django 2.2.4 on 2019-08-12 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20190805_0448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(default='', upload_to='img')),
            ],
        ),
    ]
