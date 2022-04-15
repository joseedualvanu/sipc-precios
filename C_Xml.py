def xml(nombre_log,nombre_xml,lista_declarar):
    archivo_log = open(nombre_log, 'a')
    archivo_log.write('3- Modulo C_Xml\n')
    archivo_log.close()

    from lxml import etree
    from datetime import date

    First_Line = True
    file = open(nombre_xml,'w')

    # Encabezado del XML
    file.write('\n'
       '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:int="http://interfaces.ws.sipc.bullseye.com.uy/">\n'
       "    <soapenv:Header/>\n"
       "    <soapenv:Body>\n"
       "        <int:declararPrecios>\n")

    # Loop en el XML con los datos
    for index, row in lista_declarar.iterrows():
         # Salteo primera linea
        if First_Line:
            First_Line = False
            continue

        file.write("           <precios>\n")
        file.write("               <codigo_establecimiento>"+str(row['COD_ESTABLECIMIENTO'])+"</codigo_establecimiento>\n")
        file.write("               <codigo_barra>"+str(row['COD_BARRA'])+"</codigo_barra>\n")
        file.write("               <oferta>"+str(row['OFERTA'])+"</oferta>\n")
        file.write("               <precio>"+str(row['PRECIO'])+"</precio>\n")
        file.write("               <fecha>"+str(date.today())+"</fecha>\n")
        file.write("           </precios>\n")

    # Final del XML
    file.write(
    "        </int:declararPrecios>\n"
    "    </soapenv:Body>\n"
    "</soapenv:Envelope>\n")

    file.close()

    # Cargo el XML generado
    tree = etree.parse(nombre_xml)
    # Lo paso a un string para cargarlo en el SOAP
    xml_str = etree.tostring(tree, encoding='utf8', method='xml')

    return xml_str
