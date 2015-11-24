from django.db import models

# Create your models here.

class Marca(models.Model):
	nombre  = models.CharField (max_length=100)	
	
	def __str__(self):
		return str("%s" %(self.nombre))

class Producto(models.Model):
	idmarca		= models.ForeignKey(Marca)
	referencia  = models.CharField (max_length=100)	
	precio      = models.FloatField()
	cantidad    = models.IntegerField(default=0)

	estado = (
        ('SI', 'SI'),
        ('NO', 'NO'),        
    )

	disponible  = models.CharField(max_length=2, choices=estado)
	descripcion = models.TextField()
	descuento   = models.IntegerField(default=0)
	imagen 		= models.ImageField(upload_to='photos')

	def __str__(self):
		return str("( %s ) %s --- VALOR: %0.f" %(self.referencia,self.descripcion[:60],self.precio))

class Venta(models.Model):
	idcliente   	= models.IntegerField(default=0)
	nombrecliente	= models.CharField (max_length=100)	
	idproducto		= models.ForeignKey(Producto)	
	cantidad    	= models.IntegerField(default=0)
	valor_a_pagar 	= models.FloatField()


