# Generated by Django 4.1.4 on 2022-12-13 11:07

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('videos', models.FileField(upload_to='youtube/%y', validators=[main.validators.file_size])),
            ],
        ),
    ]
