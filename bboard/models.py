from django.db import models
from django.forms import ModelForm

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Product')
    content = models.TextField(null=True, blank=True,
                               verbose_name='Description')
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Category')

    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'
        ordering = ['-published']

    def __str__(self):
        return self.title


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        ordering = ['name']


class BdForm(ModelForm):
    class Meta:
        model = Bb
        fields = {'title', 'context', 'price', 'rubric'}
