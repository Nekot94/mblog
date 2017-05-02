from django.db import models
from django.core.urlresolvers import reverse


def upload_location(instance, filename):
    return "%s/%s" %(instance.id,filename)

class Posts(models.Model):
    title = models.CharField("Заголовок", max_length=120)
    content = models.TextField("Содержимое")
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    timestamp = models.DateTimeField("Создана", auto_now=False, auto_now_add=True)
    updated = models.DateTimeField("Обновлена", auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-timestamp","-updated"]
