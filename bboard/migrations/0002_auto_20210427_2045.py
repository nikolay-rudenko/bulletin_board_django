# Generated by Django 3.2 on 2021-04-27 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='bb',
            options={'ordering': ['-published'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='bb',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.rubric', verbose_name='Category'),
        ),
    ]
