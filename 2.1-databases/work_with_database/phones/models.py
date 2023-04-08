from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField(max_length=10)
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True, null=False)

    def __str__(self):
        return f' {self.name}, {self.price}, {self.slug}'

