from django.db import models
from django.conf import settings


class CouseManger(models.Manager):

    """Cria um custom manager com um metodo search
       que fará uma consulta na tabela de cursos.
       Utilizando o obejato Q do pacote models
    """

    def search(self, query):

        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query)
        )


class Course(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Chave')
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre o Curso', blank=True)
    start_date = models.DateField(
        'Data de Início', null=True, blank=True)
    image = models.ImageField(
        upload_to='courses/images', verbose_name='Imagem',
        null=True, blank=True)
    create_at = models.DateTimeField(
        'Criado em', auto_now_add=True)
    update_at = models.DateTimeField(
        'Atuazaliado em', auto_now=True)

    objects = CouseManger()

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('courses:details', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']


class Enrollment(models.Model):
    # Classe para inscrição no curso
    STATUS_CHOICES = (
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (3, 'Cancelado'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Usuário',
        related_name='enrollments'
    )
    course = models.ForeignKey(
        Course, verbose_name='Curso',
        related_name='enrollments'
    )
    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES,
        default=0, blank=True
    )
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atuazaliado em', auto_now=True)

    def active(self):
        self.status = 1
        self.save()

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"
        unique_together = (('user', 'course'),)
