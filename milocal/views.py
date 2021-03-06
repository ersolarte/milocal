from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from django.http import HttpResponseRedirect

import time
from calendar import month_name
from milocal.models import Producto, Marca, Venta

from django.forms import ModelForm
from django.core.context_processors import csrf

#para el login esta importacion
from django.views.generic import TemplateView


class IndexView(TemplateView):	
	template_name = 'index.html'
		
class FormularioProducto(ModelForm):
	class Meta:
		model = Producto	
		exclude = ["id"]	
		
class FormularioMarca(ModelForm):
	class Meta:
		model = Marca	
		exclude = ["id"]	

class FormularioVenta(ModelForm):
	class Meta:
		model = Venta	
		exclude = ["id"]	

def main(request):
	producto = Producto.objects.all().order_by("-id")#rescata todos los datos de la tablas y ordena por fecha
	marca = Marca.objects.all()
	return render_to_response("principal.html",dict(marca=marca,producto=producto,user=request.user))

## ----------------- PRODUCTOS -----------------------------
def add(request):
	p=dict(form=FormularioProducto(), user=request.user)
	p.update(csrf(request))
	return render_to_response("addproducto.html",p)

def adicionarproducto(request):		
	if request.method == 'POST':
		form= FormularioProducto(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("milocal.views.main"))	
		else:
			form = FormularioProducto()
			return HttpResponseRedirect(reverse("milocal.views.add"))

def update(request,pk):	
	producto= Producto.objects.get(pk=int(pk))	
	p=dict(user=request.user,producto=producto, form=FormularioProducto(instance=producto))	
	p.update(csrf(request))
	return render_to_response("updateproducto.html",p)

def modificarproducto(request,pk):		
	if request.method == 'POST':
		prodmodificado = Producto.objects.get(pk=int(pk))	
		producto= FormularioProducto(request.POST, request.FILES,instance=prodmodificado)
		
		if producto.is_valid():
			producto.save()
			return HttpResponseRedirect(reverse("milocal.views.main"))
		else:			
			p=dict(user=request.user,producto=prodmodificado, form=FormularioProducto(instance=prodmodificado))
			p.update(csrf(request))
			return render_to_response("updateproducto.html",p)

def eliminar(request,pk):	
	producto= Producto.objects.get(pk=int(pk))	
	
	#bandera= Venta.objects.filter(idproducto=producto)

	#if bandera:
	#	return HttpResponseRedirect(reverse("milocal.views.main"))
	#else:	
	producto.delete()
	return HttpResponseRedirect(reverse("milocal.views.main"))


def detalle(request,pk):	
	idproducto= Producto.objects.get(pk=int(pk))
	pk_marca=idproducto.idmarca_id
	marca= Marca.objects.get(pk=int(pk_marca))	
	p=dict(user=request.user,producto=idproducto, marca=marca,form=FormularioProducto(instance=idproducto))
	p.update(csrf(request))
	return render_to_response("detalle.html",p)
## ----------------- MARCAS------------------------------

def addmarca(request):
	marcas = Marca.objects.all()
	p= dict(form=FormularioMarca(),marcas=marcas, user=request.user)
	p.update(csrf(request))
	return render_to_response("addmarca.html",p)

def adicionarmarca(request):
	if request.method == 'POST':
		form= FormularioMarca(request.POST)
		if form.is_valid():
			form.save() 				 			 		
	else:
		form = FormularioMarca()
	return HttpResponseRedirect(reverse("milocal.views.addmarca"))

def updatemarca(request,pk):
	marca= Marca.objects.get(pk=int(pk))	
	p=dict(user=request.user,marca=marca, form=FormularioMarca(instance=marca))	
	p.update(csrf(request))
	return render_to_response("updatemarca.html",p)

def modificarmarca(request,pk):
	if request.method == 'POST':
		marca_mod = Marca.objects.get(pk=int(pk))	
		marca= FormularioMarca(request.POST,instance=marca_mod)
		
		if marca.is_valid():
			marca.save()
			return HttpResponseRedirect(reverse("milocal.views.addmarca"))
		else:			
			p=dict(marca=marca_mod, form=FormularioMarca(instance=marca_mod))
			p.update(csrf(request))
			return render_to_response("updatemarca.html",p)

def eliminarmarca(request,pk):
	marca= Marca.objects.get(pk=int(pk))
	
	bandera= Producto.objects.filter(idmarca=pk)

	if bandera:
		return HttpResponseRedirect(reverse("milocal.views.addmarca"))
	else:	
		marca.delete()	
		return HttpResponseRedirect(reverse("milocal.views.addmarca"))
## ----------------- VENTA ------------------------------

def venta(request, pk):	
	producto = Producto.objects.get(pk=int(pk))	
	pk_marca=producto.idmarca_id
	marca= Marca.objects.get(pk=int(pk_marca))	
	p= dict(producto= producto, marca=marca, form=FormularioVenta(), user=request.user)
	p.update(csrf(request))
	return render_to_response("venta.html",p)

def ejecutarV(request, pk):	
	
	p=request.POST	
	producto = Producto.objects.get(pk=int(pk))		
	
	miventa = Venta()
	fv=FormularioVenta(instance=miventa)

	fv.fields['idcliente'].required= False
	fv.fields['nombrecliente'].required= False
	fv.fields['cantidad'].required= False
	fv.fields['valor_a_pagar'].required= False	

	miventa= fv.save(commit= False)
	
	miventa.idcliente=p["idcliente"]
	miventa.nombrecliente=p["nombrecliente"]
	miventa.cantidad=p["cantidad"]
	miventa.valor_a_pagar=p["total"]
	miventa.idproducto= producto

	miventa.save()
	return HttpResponseRedirect(reverse("milocal.views.main"))

def listventas(request):
	venta = Venta.objects.all()
	producto = Producto.objects.all()
	return render_to_response("listventas.html",dict(venta=venta,producto=producto,user=request.user))
		
## ----------------- SALIR ------------------------------
def salir(request):
	logout(request)
	return redirect('/')