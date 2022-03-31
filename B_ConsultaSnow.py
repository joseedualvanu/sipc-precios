def consultasnow(nombre_log,file_keyP8):
    archivo_log = open(nombre_log, 'a')
    archivo_log.write('2- Modulo B_ConsultaSnow\n')

    # Liberia para salir del flujo
    import sys
    # Importo el modulo con el envio de mail
    from A_Error_Handling import enviar_mail_error
    # Snowflake
    from snowflake import connector
    # Libreria pandas para pruebas
    import pandas as pd

    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives.asymmetric import dsa
    from cryptography.hazmat.primitives import serialization

    with open(file_keyP8, "rb") as key:
        p_key= serialization.load_pem_private_key(
            key.read(),
            password=None,
            backend=default_backend()
        )

    pkb = p_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption())

    # Realizo la conexion con snowflake
    try:
        conn = connector.connect(
            user='',
            account='',
            private_key= pkb,
            warehouse='',
            database='',
            schema=''
            )
    except:
        print('No se pudo lograr la conexión con Snowflake')
        archivo_log.write('No se pudo lograr la conexión con Snowflake\n')
        archivo_log.write('-------------------------------------\n')
        archivo_log.close()
        enviar_mail_error(nombre_log)
        sys.exit()
    #create cursor
    curs=conn.cursor()
    #execute SQL statement
    try:
        curs.execute('''
        Consulta SQL
      ''')
    except:
        print('Problemas con la ejecución de la consulta SQL')
        archivo_log.write('Problemas con la ejecución de la consulta SQL\n')
        archivo_log.write('-------------------------------------\n')
        archivo_log.close()
        enviar_mail_error(nombre_log)
        sys.exit()

    # Guardo el resultado en un dataframe de pandas
    lista_declarar = curs.fetch_pandas_all()
    print(lista_declarar)
    # Cierro la conexion
    curs.close()

    # # ejemplo para pruebas (Borrar)
    # lista_declarar = pd.DataFrame()
    # lista_declarar['COD_ESTABLECIMIENTO'] = ['DGC9997', 'DGC4737', 'DGC8328', 'DGC1600']
    # lista_declarar['COD_BARRA'] = ['7730213000117', '7730241003920', '7790580660000', '7730377066028']
    # lista_declarar['OFERTA'] = ['FALSE', 'FALSE', 'TRUE', 'FALSE']
    # lista_declarar['PRECIO'] = ['54.0 ', '180.0', '44.0', '55.0']
    # lista_declarar['PRECIOSNIVA'] = ['49.09', '163.63', '40.00', '45.08']

    # El caso que la lista vuelva vacia
    if lista_declarar.empty:
        print('Consulta a Snowflake vacia')
        archivo_log.write('Consulta a Snowflake vacia\n')
        archivo_log.write('-------------------------------------\n')
        archivo_log.close()
        enviar_mail_error(nombre_log)
        sys.exit()

    return lista_declarar
