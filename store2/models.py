from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.
class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    # A Slug is basically a short label for something, containing 
    # only letters, numbers, underscores or hyphens. They’re generally used in URLs
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def get_url(self):
        # If you need to use something similar to the url template tag in your code, 
        # Django provides the following function:
        # reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)
        return reverse('product_detail',args=[self.category.slug,self.slug])

    # Importance of __str__ function and where does it reflect
    # https://stackoverflow.com/questions/45483417/what-is-doing-str-function-in-django?newreg=d02149502ede493abc6c2e2464a73989
    def __str__(self):
        return self.product_name


class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(
        max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value
