from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class CatMod(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Ссылка')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория модификаторов'
        verbose_name_plural = 'Категории модификаторов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(CatMod, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('catalog:product_list_by_category', args=[self.slug])


class Modificators(models.Model):
    category = models.ForeignKey(CatMod, on_delete=models.CASCADE, verbose_name='Категория модификаторов')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена')
    available = models.BooleanField(verbose_name='Наличие')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Модификатор'
        verbose_name_plural = 'Модификаторы'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Modificators, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('catalog:product_detail', args=[self.id, self.slug])


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Ссылка')
    range = models.CharField(max_length=200, db_index=True, verbose_name='Место в списке')

    class Meta:
        ordering = ('range',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('catalog:product_list_by_category', args=[self.slug])


Size = (
    ('См.', 'См.'), ('Кг.', 'Кг.'), ('л', 'л'), ('Мл.', 'Мл.'), ('Мг.', 'Мг.'), ('г', 'г'), ('Шт.', 'Шт.'),
)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', blank=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена')
    available = models.BooleanField(verbose_name='Наличие')
    Size_choice = models.CharField(choices=Size, max_length=250, blank=True, unique=False, verbose_name='Выбор величины')
    size = models.CharField(max_length=200, blank=True, unique=False, verbose_name='Размер')
    modifier_groups = models.ManyToManyField(CatMod, verbose_name='Модификаторы', blank=True)
    range = models.CharField(max_length=200, db_index=True, verbose_name='Место в списке')

    class Meta:
        ordering = ('range',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('catalog:product_detail', args=[self.id, self.slug])
