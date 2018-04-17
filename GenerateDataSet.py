from xml.etree import ElementTree as ET
import pandas as pd


def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def buildFactura(num,InvoiceNo,CustomerID,Description,StockCode,Quantity,InvoiceDate,UnitPrice):

    factura = ET.Element("cfdi:Comprobante")
    factura.set("xmlns:cfdi","http://www.sat.gob.mx/cfd/3")
    factura.set("xmlns:tfd","http://www.sat.gob.mx/TimbreFiscalDigital")
    factura.set("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
    factura.set("xsi:schemaLocation"," http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv32.xsd ")
    factura.set("serie","F")
    factura.set("version","3.2")
    factura.set("folio",f"{InvoiceNo}")
    factura.set("fecha",f"{InvoiceDate}")
    factura.set("sello","ey4npwEGHOHOB0T1Sy5zlaEZZxwnXJdUg9PpcNXPxH+d41iaUidbj9gWXugdUhhv+gsB3h6b1LbjKpfvqaBjGDdNuc4R6nVV0Qodqo9pJvA7jGH0lCaY/WgDWhahv1knfyeAoGDqqzFDQtX4mdnTy2b8wJ+HEOHoKg+VF6dNw4M=")
    factura.set("tipoDeComprobante","ingreso")
    factura.set("formaDePago","Pago en una sola exhibición")
    factura.set("noCertificado","00001000000305104410")
    factura.set("certificado","MIIEgTCCA2mgAwIBAgIUMDAwMDEwMDAwMDAzMDUxMDQ0MTAwDQYJKoZIhvcNAQEFBQAwggGKMTgwNgYDVQQDDC9BLkMuIGRlbCBTZXJ2aWNpbyBkZSBBZG1pbmlzdHJhY2nDs24gVHJpYnV0YXJpYTEvMC0GA1UECgwmU2VydmljaW8gZGUgQWRtaW5pc3RyYWNpw7NuIFRyaWJ1dGFyaWExODA2BgNVBAsML0FkbWluaXN0cmFjacOzbiBkZSBTZWd1cmlkYWQgZGUgbGEgSW5mb3JtYWNpw7NuMR8wHQYJKoZIhvcNAQkBFhBhY29kc0BzYXQuZ29iLm14MSYwJAYDVQQJDB1Bdi4gSGlkYWxnbyA3NywgQ29sLiBHdWVycmVybzEOMAwGA1UEEQwFMDYzMDAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBEaXN0cml0byBGZWRlcmFsMRQwEgYDVQQHDAtDdWF1aHTDqW1vYzEVMBMGA1UELRMMU0FUOTcwNzAxTk4zMTUwMwYJKoZIhvcNAQkCDCZSZXNwb25zYWJsZTogQ2xhdWRpYSBDb3ZhcnJ1YmlhcyBPY2hvYTAeFw0xNDA5MTIxOTE2MzBaFw0xODA5MTIxOTE2MzBaMIHNMSswKQYDVQQDEyJBTEJFUlRPIEZSQU5DSVNDTyBQQVNBUkFOIEZJR1VFUk9BMSswKQYDVQQpEyJBTEJFUlRPIEZSQU5DSVNDTyBQQVNBUkFOIEZJR1VFUk9BMSswKQYDVQQKEyJBTEJFUlRPIEZSQU5DSVNDTyBQQVNBUkFOIEZJR1VFUk9BMRYwFAYDVQQtEw1QQUZBODIxMDA1SU44MRswGQYDVQQFExJQQUZBODIxMDA1SE1DU0dMMDMxDzANBgNVBAsTBnVuaWRhZDCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAhg68ZOyj2vxfp2D9phYNlaxTLI0vyx4Qn7k82CFrRZ1nJKWSl+3+o8aZzsdr0pTdwdM4DMquQtj8pgsaUqdKpRn2qYFjj+gAMR9Bet1h08122xIex1wp4OWeKpo5W9HSrWulC/de2lMC1OqxG/3c1BbJ1OnsamFPx/DgAdPNpa0CAwEAAaMdMBswDAYDVR0TAQH/BAIwADALBgNVHQ8EBAMCBsAwDQYJKoZIhvcNAQEFBQADggEBAEyMt38i5pX168IFCNY0aLOeM06HMimq+aeZlcYKxqjtE02tg3FnxJVKsfaotDUhlqG+WDgUQ2Xw2U355t5craVHONrU9efu6mZ0x1IZ3YTcZlmgylyToruoHZd4vACzoDqwZ9/tg2U5LK0g8rNiVSH8jo3G9F4dzYGXHaRnnOz2yXP5wkTSON0SnFPwb7e5vewGgXbT0DNFL7lk9dI3peXpaGevOLRrQ0f0+4KReAH27Tq3rbUzXQnzQHmnmJjbOY18ari7DD9/HwfdNa9PRcotLgcMvTeZRlzT/OY2xD1PhVWmbmym2S8uLhODckRvqSti7iaWl3/oYHFvLYot00c=")
    factura.set("condicionesDePago","Contado")
    factura.set("subTotal","1227.60")
    factura.set("descuento","0.00")
    factura.set("TipoCambio","1.0000")
    factura.set("Moneda","MXN")
    factura.set("total","1424.02")
    factura.set("metodoDePago","No identificado")
    factura.set("LugarExpedicion","Azcapotzalco, D.F.")

    Emisor=objectItem(factura,"cfdi:Emisor","rfc:::PAFA821005IN8","nombre:::ALBERTO FRANCISCO PASARAN FIGUEROA")
    DomicilioFiscal=objectItem(Emisor,"cfdi:DomicilioFiscal","calle:::AURORA","noExterior:::6 BIS","colonia:::Santa Ines","localidad:::México","municipio:::Azcapotzalco","estado:::D.F.","pais:::Mexico","codigoPostal:::02140")
    ExpedidoEn=objectItem(Emisor,"cfdi:ExpedidoEn","calle:::AURORA","noExterior:::6 BIS","colonia:::Santa Ines","municipio:::Azcapotzalco","estado:::D.F.","pais:::Mexico","codigoPostal:::02140")
    RegimenFiscal=objectItem(Emisor,"cfdi:RegimenFiscal","Regimen:::Regímen de Incorporación Fiscal")

    Receptor=objectItem(factura,"cfdi:Receptor",f"rfc:::{CustomerID}","nombre:::ANUNCIOS PREMIUM ESPECTACULARES S.A.DE C.V")
    Domicilio=objectItem(Receptor,"cfdi:Domicilio","calle:::SANTO DOMINGO","noExterior:::139","municipio:::Azcapotzalco","pais:::Mexico","codigoPostal:::02760")

    Conceptos=objectItem(factura,"cfdi:Conceptos")
    Concepto=objectItem(Conceptos,"cfdi:Concepto",f"cantidad:::{Quantity}","unidad:::SOLDADURA",f"descripcion:::{Description}",f"valorUnitario:::{UnitPrice}","importe:::1227.60")
    ComplementoConcepto=objectItem(Concepto,"cfdi:ComplementoConcepto")

    Impuestos=objectItem(factura,"cfdi:Impuestos","totalImpuestosTrasladados:::196.42")
    Traslados=objectItem(Impuestos,"cfdi:Traslados")
    Traslado=objectItem(Traslados,"cfdi:Traslado","impuesto:::IVA","tasa:::16","importe:::196.42")

    Complemento=objectItem(factura,"cfdi:Complemento")
    TimbreFiscalDigital=objectItem(Complemento,"tfd:TimbreFiscalDigital","xmlns:tfd:http://www.sat.gob.mx/TimbreFiscalDigital","xsi:schemaLocation:http://www.sat.gob.mx/TimbreFiscalDigital http://www.sat.gob.mx/TimbreFiscalDigital/TimbreFiscalDigital.xsd","version:1.0","UUID:::E033B66E-34D5-4A81-835D-75562160AF38","FechaTimbrado:::2016-07-04T10:08:28","selloCFD:::ey4npwEGHOHOB0T1Sy5zlaEZZxwnXJdUg9PpcNXPxH+d41iaUidbj9gWXugdUhhv+gsB3h6b1LbjKpfvqaBjGDdNuc4R6nVV0Qodqo9pJvA7jGH0lCaY/WgDWhahv1knfyeAoGDqqzFDQtX4mdnTy2b8wJ+HEOHoKg+VF6dNw4M=","noCertificadoSAT:::00001000000301100488","selloSAT:::PonjV5Ob/sA+w8XP5xOa2Y6hB5GQRDAtCpEBaNlaovSLuV7kR3wue5wnYS/QOee/ANzohuEgFZAKxbAtzMCkWC4c8EY2GA8eu1qNp0rdq4ADJc9EYYIvnzwMbfLNMFK7hgvgXt1PU5MKDT0c9YTsBCqspbHJoHMYF206TO7MoGk=")
    indent(factura)

    tree = ET.ElementTree(factura)

    tree.write(f"/home/javier/facturas/factura{num}.xml", xml_declaration=True, encoding='utf-8', method="xml")


def objectItem(parent, title, *args):
    val = ET.SubElement(parent, title)
    if len(args) > 0:
        for item in args:
            data = item.split(":::")
            val.set(data[0], data[1])
    return val


def read_Csv(file_Path):
    data = pd.read_csv(file_Path, sep=',',encoding = "ISO-8859-1")

    for index, row in data.iterrows():
                    InvoiceNo = str(row["InvoiceNo"])
                    StockCode = row["StockCode"]
                    Description = row["Description"]
                    Quantity = row["Quantity"]
                    InvoiceDate = row["InvoiceDate"]
                    UnitPrice = row["UnitPrice"]
                    CustomerID = str(row["CustomerID"])
                    CID=("111111",CustomerID)[CustomerID!="nan"]
                    #print(CID)
                    print(InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CID)
                    buildFactura(InvoiceNo,str(InvoiceNo),str(CustomerID),Description,StockCode,Quantity,InvoiceDate,UnitPrice)


if __name__ == "__main__":
    _file="/home/javier/PycharmProjects/DataSetFacturas/data.csv"
    read_Csv(_file)
