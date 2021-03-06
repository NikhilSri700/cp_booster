# Generated by Django 2.2.7 on 2020-07-19 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Div1A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div1B',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div1C',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div1D',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div1E',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div1F',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div1G',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div1H',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div1I',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div1J',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div2A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div2B',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div2C',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div2D',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div2E',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div2F',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div2G',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div2H',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div2I',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Div2J',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contest', models.TextField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submissions', models.IntegerField(default=0)),
            ],
        ),
    ]
