# Generated by Django 2.1.7 on 2019-03-02 18:10

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import core.models.specimen


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set',
                                                  related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission',
                                                            verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'boxes',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45)),
                ('surname', models.CharField(max_length=45)),
                ('organization', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('skype', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'contacts',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=100, null=True)),
                ('year', models.PositiveSmallIntegerField(null=True)),
            ],
            options={
                'db_table': 'organisms',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('mime', models.CharField(max_length=100)),
                ('path', models.ImageField(upload_to='photos')),
                ('happened_at', models.DateTimeField(null=True)),
                ('description', models.TextField(null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'photos',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('description', models.TextField(null=True)),
                ('boxes', models.ManyToManyField(to='core.Box')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Contact')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'rents',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Specimen',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('nickname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[(core.models.specimen.GenderChoice('Male'), 'Male'), (core.models.specimen.GenderChoice('Female'), 'Female')], max_length=10, null=True)),
                ('form', models.CharField(max_length=50)),
                ('notes', models.TextField(null=True)),
                ('dna', models.TextField(null=True)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Box')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('organism', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Organism')),
            ],
            options={
                'db_table': 'specimens',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='TaxonomicClass',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'taxonomic_classes',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='TaxonomicFamily',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'taxonomic_families',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='TaxonomicGenus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('taxonomic_family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TaxonomicFamily')),
            ],
            options={
                'db_table': 'taxonomic_genuses',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='TaxonomicKingdom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'taxonomic_kingdoms',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='TaxonomicOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('taxonomic_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TaxonomicClass')),
            ],
            options={
                'db_table': 'taxonomic_orders',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='TaxonomicPhylum',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('kingdom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TaxonomicKingdom')),
            ],
            options={
                'db_table': 'taxonomic_phylums',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='TaxonomicSpecies',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('taxonomic_genus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TaxonomicGenus')),
            ],
            options={
                'db_table': 'taxonomic_species',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='TaxonomicSubspecies',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('taxonomic_species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TaxonomicSpecies')),
            ],
            options={
                'db_table': 'taxonomic_subspecies',
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='taxonomicfamily',
            name='taxonomic_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TaxonomicOrder'),
        ),
        migrations.AddField(
            model_name='taxonomicclass',
            name='taxonomic_phylum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TaxonomicPhylum'),
        ),
        migrations.AddField(
            model_name='rent',
            name='specimens',
            field=models.ManyToManyField(to='core.Specimen'),
        ),
        migrations.AddField(
            model_name='photo',
            name='specimen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Specimen'),
        ),
        migrations.AddField(
            model_name='organism',
            name='taxonomic_species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TaxonomicSpecies'),
        ),
        migrations.AddField(
            model_name='organism',
            name='taxonomic_subspecies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.TaxonomicSubspecies'),
        ),
    ]
