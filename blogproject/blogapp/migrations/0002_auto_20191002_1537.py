# Generated by Django 2.2 on 2019-10-02 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(),
        ),
    ]
