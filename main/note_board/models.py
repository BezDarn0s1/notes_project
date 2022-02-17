from django.db import models


from django.db import models


class Topic(models.Model):

    Note_topic = models.CharField(max_length=20, verbose_name='Тема заметки')
    description = models.TextField(blank=True, max_length=256, verbose_name='Описание темы', default='Без темы')
    slug = models.SlugField(max_length=256, unique=True)

    class Meta:
        ordering = ('Note_topic',)
        verbose_name = 'Тема заметки'
        verbose_name_plural = 'Темы заметок'

    def __str__(self):
        return self.Note_topic


class Record(models.Model):

    slug = models.SlugField(max_length=256, unique=True)
    Note_topic = models.ForeignKey(Topic, on_delete=models.CASCADE,verbose_name='Тема заметки')
    title = models.CharField(max_length=20, verbose_name='Название заметки')
    #ecord_id = models.
    note_field = models.TextField(blank=False, verbose_name='Содержание заметки')
    pub_date = models.DateTimeField(verbose_name='Дата публикации')
    #user_name = 


    class Meta:

        ordering = ('pub_date',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Заметки'
        verbose_name_plural = 'Заметка'

    def __str__(self):
        return self.title

