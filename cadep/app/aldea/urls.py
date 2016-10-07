from django.conf.urls import url, include
from app.aldea.views import AldeaList, AldeaCreate, AldeaUpdate, AldeaDelete



urlpatterns = [
    url(r'^nuevo$', AldeaCreate.as_view(), name='aldea_crear'),
    url(r'^listar$', AldeaList.as_view(), name='aldea_listar'),
    url(r'^editar/(?P<pk>\d+)/$', AldeaUpdate.as_view(), name='aldea_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', AldeaDelete.as_view(), name='aldea_eliminar'),

]
