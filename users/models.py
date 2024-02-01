from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

class Project(models.Model):
    title = models.CharField(max_length=255)

    
class Image(models.Model):

    def get_default_project():
        # Lógica para obter ou criar um projeto padrão
        # Este é apenas um exemplo, ajuste conforme necessário
        default_project, created = Project.objects.get_or_create(title='Default Project')
        return default_project.id  # Retorne o ID do projeto padrão

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images', default=get_default_project)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)

    # resizing images
""" def save(self, *args, **kwargs):
        super().save()

        img = image.open(self.projeto.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.projeto.path) """
