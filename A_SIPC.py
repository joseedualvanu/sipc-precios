"""
MODULO A
    Description: main module, run other modules

    Args:
		--
    Returns:

    Error:
        --
    Note:
        See https://www.datacamp.com/community/tutorials/docstrings-python
"""

import datetime
# Importo el modulo con el envio de mail ok
from A_Email_ok import enviar_mail_ok
import os
# Library for logging
# log levels: debug(lowest), info, warning, error, critical(highest)
import logging

# Obtengo fecha y hora
start_time = datetime.datetime.now()
day = start_time.day
month = start_time.month
year = start_time.year
hour = start_time.hour
minute = start_time.minute
second = start_time.second

# private key direction
file_keyP8 = ''

# nombres auxiliares
today = str(day)+str(month)+str(year)
hora = str(hour)+':'+str(minute)+':'+str(second)

# direccion y nombres
direction = os.path.dirname(os.path.abspath(__file__))+'/'

# Genero un log de la ejecucion
nombre_log = direction + "Logs/SIPC_precios_" + str(today) + '.log'
nombre_xml = direction + "/Precios/SIPC_precios_"+ str(today) + '.xml'

logging.basicConfig(filename= direction + 'SIPC_Productos.log',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
# logging.disable(logging.debug)
logging.debug('Start of program')

archivo_log = open(nombre_log, 'a')
archivo_log.write('-------------------------------------\n')
archivo_log.write('Comienzo\t'+ str(hora)+'\n')
archivo_log.write('1- Modulo A_SIPC\n')
archivo_log.close()

# Consulta a snowflake para precio venta unit / codigo de barra / suc
from B_ConsultaSnow import consultasnow
(lista_declarar) = consultasnow(nombre_log,file_keyP8)

# Escribo el resultado de la consulta en un xml
from C_Xml import xml
(xml_str) = xml(nombre_log,nombre_xml,lista_declarar)

# Cargo el xml al SOAP de SIPC
from D_Post import post
(r) = post(nombre_log,xml_str)

print(r)

logging.debug('End of program')

# Notificacion por mail OK
# enviar_mail_ok(nombre_log)
