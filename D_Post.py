def post(nombre_log,xml_str):
    archivo_log = open(nombre_log, 'a')
    archivo_log.write('4- Modulo D_Post\n')

    # Liberia para salir del flujo
    import sys
    # Importo el modulo con el envio de mail
    from A_Error_Handling import enviar_mail_error
    # Libreria
    import requests

    import datetime

    # Formato del XML
    headers = {'content-type': 'text/xml'}
    # Servicio para declarar todas las ventas
    URL = ""

    try:
        r = requests.post(url = URL,data=xml_str,headers=headers, timeout = 600)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("Http Error:" + str(errh))
        archivo_log.write("Http Error:" + str(errh)+"\n")
        archivo_log.write('-------------------------------------\n')
        archivo_log.close()
        enviar_mail_error(nombre_log)
        sys.exit()
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:" + str(errc))
        archivo_log.write("Error Connecting:" + str(errc)+'\n')
        archivo_log.write('-------------------------------------\n')
        archivo_log.close()
        enviar_mail_error(nombre_log)
        sys.exit()
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:" + str(errt))
        archivo_log.write("Timeout Error:" + str(errt)+'\n')
        archivo_log.write('-------------------------------------\n')
        archivo_log.close()
        enviar_mail_error(nombre_log)
        sys.exit()
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else" + str(err))
        archivo_log.write("OOps: Something Else" + str(err)+'\n')
        archivo_log.write('-------------------------------------\n')
        archivo_log.close()
        enviar_mail_error(nombre_log)
        sys.exit()

    print(r.reason)
    # print(r.status_code)

    # Escribo resultado del servicio
    archivo_log.write('Respuesta SOAP:\n')
    archivo_log.write(str(r.reason) + ' - ' + str(r.status_code) + '\n')

    # Obtengo fecha y hora de finalizacion
    start_time = datetime.datetime.now()

    hour = start_time.hour
    minute = start_time.minute
    second = start_time.second

    hora = str(hour)+':'+str(minute)+':'+str(second)

    archivo_log.write('Fin\t\t'+ str(hora)+'\n')
    archivo_log.write('-------------------------------------\n')
    archivo_log.close()
    return r
