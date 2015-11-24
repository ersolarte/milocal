function calculo(cantidad,precio,inputtext){
 
	// Calculo del subtotal
	subtotal = parseFloat(precio)*cantidad;
	inputtext.value=subtotal;
 
        //Calculo del total
	total = eval(totaltext.value);
	totaltext.value = total + subtotal;
}