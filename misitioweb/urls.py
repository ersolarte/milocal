"""misitioweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from milocal.views import IndexView

urlpatterns = [
    
    #URL que me permite entrar al administrador de mis sitios web
    url(r'^admin/', include(admin.site.urls)),    

    #login facebook,twitter
    url('',include('social.apps.django_app.urls', namespace='social')),        
    url(r'^$', IndexView.as_view()),
    url(r'^salir/$', 'milocal.views.salir'),
    
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
    url(r'^ejecutarV/(?P<pk>\d+)/$','milocal.views.ejecutarV'),
    #URL que entra al index del mi sitio web    
    url(r'^principal','milocal.views.main'),
]
