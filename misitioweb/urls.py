from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from milocal.views import IndexView

# UNDERNEATH your urlpatterns definition, add the following two lines:

urlpatterns = [
    
    #URL que me permite entrar al administrador de mis sitios web
    url(r'^admin/', include(admin.site.urls)),    

    #login facebook,twitter
    url('',include('social.apps.django_app.urls', namespace='social')),        
    url(r'^$', IndexView.as_view()),
    url(r'^salir/$', 'milocal.views.salir'),


    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{
            'document_root': settings.MEDIA_ROOT
        }),
    
    # URLs para Productos	
    url(r'^add/$','milocal.views.add'),
    url(r'^adicionarproducto/$','milocal.views.adicionarproducto'),
    url(r'^update/(?P<pk>\d+)/$','milocal.views.update'),
    url(r'^modificarproducto/(?P<pk>\d+)/$','milocal.views.modificarproducto'),    
    url(r'^eliminar/(?P<pk>\d+)/$','milocal.views.eliminar'),
    url(r'^detalle/(?P<pk>\d+)/$','milocal.views.detalle'),    
    
    # URLs para Marcas
    url(r'^addmarca/$','milocal.views.addmarca'),
    url(r'^adicionarmarca/$','milocal.views.adicionarmarca'),
    url(r'^updatemarca/(?P<pk>\d+)/$','milocal.views.updatemarca'),
    url(r'^modificarmarca/(?P<pk>\d+)/$','milocal.views.modificarmarca'),    
    url(r'^eliminarmarca/(?P<pk>\d+)/$','milocal.views.eliminarmarca'),

    # URLs para Ventas
    url(r'^venta/(?P<pk>\d+)/$','milocal.views.venta'),    
    url(r'^ejecutarV/(?P<pk>\d)/$','milocal.views.ejecutarV'),
    url(r'^listventas/$','milocal.views.listventas'),
    #URL que entra al index del mi sitio web    
    url(r'^principal','milocal.views.main'),
]