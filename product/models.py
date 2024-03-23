import datetime
from django.utils.timezone import now
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User


class TimeStampMixin(models.Model):
    is_deleted      = models.BooleanField (default=False)
    created_at      = models.DateTimeField(auto_now_add=True,null=True)
    updated_at      = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم التصنيف")

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="اسم الوسم")

    def __str__(self):
        return self.name

class Product(TimeStampMixin, models.Model) :
    nameEn = models.CharField(max_length=100,null=True, blank=True, verbose_name="اسم المنتج بالانجليزى")
    nameAr = models.CharField(max_length=100,null=True, blank=True, verbose_name="اسم المنتج بالعربى")
    smallDescription = models.TextField(max_length=1000, null=True, blank=True, verbose_name="وصف قصير")
    longDescription  = models.TextField(max_length=2500, null=True, blank=True, verbose_name="الوصف الكامل")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="التصنيف")
    featured = models.BooleanField(default=False, verbose_name="المنتج المميز")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="الوسوم")
    slug = models.SlugField(max_length=1000, unique=True, null=True, blank=True, verbose_name="اسم المنتج متوافق")
    
    def save(self, *args, **kwargs):
        # Update slug if product name has changed
        if self.pk:
            old_product = Product.objects.get(pk=self.pk)
            if self.nameEn != old_product.nameEn or self.nameAr != old_product.nameAr:
                self.slug = None  # Reset slug to regenerate

        if not self.slug:
            slugEn = slugify(self.nameEn) # type: ignore
            # print(f"\n slug => {slugEn} \n")
            self.slug = slugEn
        super().save(*args, **kwargs)

    def __str__(self):
        return  str(self.nameEn) + " /|\\ " + str(self.nameAr)

class Prices4sizes(TimeStampMixin, models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="prices",verbose_name=("المنتج"))
    img     = models.URLField(null=True, blank=True, verbose_name="رابط الصورة")
    price = models.DecimalField(max_digits=6,decimal_places=2,null=True, blank=True, verbose_name="السعر")
    size  = models.CharField(max_length=15, null=True, blank=True, verbose_name="اكتب المقاس")
    color = models.CharField(max_length=15, null=True, blank=True, verbose_name="اللون")
    weight= models.CharField(max_length=15, null=True, blank=True, verbose_name="الوزن / الحجم")
    stock = models.SmallIntegerField(null=True, blank=True, verbose_name="الكمية المعروضة")

    def __str__(self):
        return f"{self.product.nameAr} ({self.size}, {self.color})"
# rating model 

class Review(TimeStampMixin, models.Model):
    product = models.ForeignKey("product", on_delete=models.CASCADE, related_name="reviews", verbose_name=("المنتج"))
    stars   = models.DecimalField(max_digits=6,decimal_places=2, null=True, blank=True, verbose_name="النجوم")
    text    = models.TextField(max_length=250, null=True, blank=True, verbose_name="اكتب تجربتك مع المنتج")
    user    = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="العميل")

def __str__(self):
        return f"{self.product.nameAr} ({self.stars} stars)"