import uuid
from django.db import models
from stdimage import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    created_at = models.DateField('Created at', auto_now_add=True)
    modified_at = models.DateField('Created at', auto_now=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Engine'),
        ('lni-stats-up', 'Graphic'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket'),
    )

    service = models.CharField('Service', max_length=100)
    description = models.TextField('Description', max_length=200)
    icon = models.CharField('Icon', max_length=100, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service


class Job(Base):
    job = models.CharField('Job', max_length=100)

    class Meta:
        verbose_name = 'Job'    
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return self.job


class Team(Base):
    name = models.CharField('Name', max_length=100)
    job = models.ForeignKey('app.Job', verbose_name='Job',
                                                on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=100)
    image = StdImageField('Image', upload_to=get_file_path, variations={
                'thumbnail': {"width": 480, "height": 480, "crop": True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Team'    
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name
    


 