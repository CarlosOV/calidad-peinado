from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken.views import obtain_auth_token
import settings
from peinados.views import *
import debug_toolbar




# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'peluquerias', PeluqueriaViewSet)
router.register(r'sucursales', SucursalViewSet)
router.register(r'peinados', PeinadoViewSet)
router.register(r'tamanos-cabello', TamanoCabelloViewSet)
router.register(r'rostro', RostroViewSet)
router.register(r'ocasiones', OcasionViewSet)
router.register(r'tipos-cabello', TipoCabelloViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'calidad_peinado.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/v1/', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^accounts/', include('authtools.urls')),
]

urlpatterns += [
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^__debug__/', include(debug_toolbar.urls)),
]