from django.urls import path
from .views import home, profile, RegisterView, userfixopage, criacaopage, image_upload, image_list,projetos
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('userfixo/', userfixopage, name='userfixo'),
    path('criacao', image_upload, name='image_upload'),
    path('list/', image_list, name='image_list'),
    path('projetos/', projetos, name='projetos')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
