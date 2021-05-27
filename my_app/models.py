from django.db import models
from django.shortcuts import reverse


# Create your models here.

CATEGORY_CHOICES = (
    ('C1', 'New'),
    ('C2', 'Best'),
    ('C3', 'Category 3')
)


LABEL_CHOICES = (
    ('L1', 'primary'),
    ('L2', 'secondary'),
    ('L3', 'danger')
)


class Product(models.Model):
    title = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)
    slug = models.SlugField()
    description = models.TextField()
    sub_description = models.TextField()
    image = models.ImageField(upload_to='my_app', null=True, blank=True)

    def get_absolute_url(self):
        return reverse("my_app:product-detail", kwargs={
            'slug': self.slug
        })

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.title



class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='my_app', null=True, blank=True)

    def __str__(self):
        return self.product.title

    @property
    def imageURL(self):
        try:
            url = self.images.url
        except:
            url = ''
        return url
