

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=250,unique='true')
    slug=models.SlugField(max_length=250,unique='true')
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)



class products(models.Model):
    name = models.CharField(max_length=250, unique='true')
    slug = models.SlugField(max_length=250, unique='true')
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField(default=False)
    price=models.IntegerField()
    catog=models.ForeignKey(category,on_delete=models.CASCADE)
    class Meta:
        ordering=('name',)
        verbose_name=('product')
        verbose_name_plural=('products')

    def __str__(self):

        return '{}'.format(self.name)
    def get_url(self):
        return reverse('details',args=[self.catog.slug,self.slug])



# Create your models here.
