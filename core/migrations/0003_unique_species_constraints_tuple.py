# Generated by Django 2.1.7 on 2019-03-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0002_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organism',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='taxonomicspecies',
            name='name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='taxonomicsubspecies',
            name='name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterUniqueTogether(
            name='taxonomicspecies',
            unique_together={('taxonomic_genus', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='taxonomicsubspecies',
            unique_together={('taxonomic_species', 'name')},
        ),
    ]
