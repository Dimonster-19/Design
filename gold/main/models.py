from django.db import models


class Project(models.Model):
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('URL', unique=True)
    description = models.TextField('Описание')
    cover = models.ImageField('Обложка', upload_to='projects/')
    client = models.CharField('Клиент', max_length=100)
    year = models.PositiveIntegerField('Год')
    is_featured = models.BooleanField('В избранном', default=False)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='project_images/')
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Изображение проекта'
        verbose_name_plural = 'Изображения проектов'