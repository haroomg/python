import datetime
# from datetime import datetime

fechaActual = datetime.datetime.now() # Obtenemos la fecha y hora actual
print(fechaActual)

fecha = datetime.datetime(2021,11, 5, 5, 55, 33) # de esta forma podemos obtener una fecha personalizada
print(fecha)

fechaActual2 = datetime.datetime.strftime(fechaActual,'%d/%m/%Y %H:%M:%S') # Formateamos la fecha  a un string
print(fechaActual2)

fechaActual3 = datetime.datetime.strftime(fechaActual,'%B %d %Y %H:%M:%S') # Formateamos la fecha  a un string
print(fechaActual3)


# pasamos una fecha de texto a un objeto datetime
fechaTexto = 'Dec 06 2020 12:56:11'

fechaActual4 = datetime.datetime.strptime(fechaTexto, '%b %d %Y %H:%M:%S')
print(fechaActual4)

dia = datetime.datetime.strftime(fechaActual, '%d') # nos muestra el dia actual
print(dia)

dia = int(datetime.datetime.strftime(fechaActual, '%d')) # la fecha actual la podemos transformar a un dato entero
print(dia)

horaActual = datetime.datetime.strftime(fechaActual, '%H:%M:%S') # nos muestra la hora actual
print(horaActual)


# podemos sumar o restar fechas ya sea una fecha actual, pasada o futura
fechaPasada = datetime.datetime(2020, 10, 23)
diferencia = fechaActual - fechaPasada

print(diferencia) # nos duevuelve los dias y hora de diferencia
print(diferencia.days) # nos duevuelve los dias diferencia
print(diferencia.total_seconds()) # nos duevuelve los segundos de diferencia


dia_delta = datetime.timedelta(days=5) 
fechaInicial = datetime.date.today()
print(fechaInicial)

fechaFutura = fechaInicial + dia_delta # sumamos 5 dias a la fecha actual
print(fechaFutura)


fecha = datetime.datetime.now().isoformat() # nos devuelve la fecha actual en formato iso
print(fecha)