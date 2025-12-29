from django.db import models


class ProgrammingLanguage(models.Model):
    # Поля из задания
    name = models.CharField(max_length=100, verbose_name="Название языка")
    description = models.TextField(verbose_name="Описание")
    year_created = models.IntegerField(verbose_name="Год создания")
    main_usage = models.TextField(verbose_name="Основная сфера применения")
    logo = models.ImageField(upload_to='language_logos/', verbose_name="Логотип")

    # Дополнительное поле для популярных языков
    is_popular = models.BooleanField(default=False, verbose_name="Популярный язык")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Язык программирования"
        verbose_name_plural = "Языки программирования"