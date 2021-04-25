from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Product')
    content = models.TextField(null=True, blank=True,
                               verbose_name='Description')
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'
        ordering = ['-published']

    def __str__(self):
        return self.title

