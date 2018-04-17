from xml.etree import ElementTree as ET
import pandas as pd


class Facturas:

    Conceptos=None
    check = 0
    Comprobante=None
    NumTemp=None

    def indent(self, elem, level=0):
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def buildFactura(self,num, InvoiceNo, CustomerID, Description, StockCode, Quantity, InvoiceDate, UnitPrice):

        if self.check != InvoiceNo:

            if self.Comprobante is not None:
                self.indent(self.Comprobante)
                tree = ET.ElementTree(self.Comprobante)
                tree.write(f"/home/javier/facturas/factura{self.NumTemp}.xml", xml_declaration=True, encoding='utf-8',method="xml")

            self.Comprobante = ET.Element("cfdi:Comprobante")
            self.Comprobante.set("xmlns:cfdi", "http://www.sat.gob.mx/cfd/3")
            self.Comprobante.set("xmlns:tfd", "http://www.sat.gob.mx/TimbreFiscalDigital")
            self.Comprobante.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
            self.Comprobante.set("xsi:schemaLocation",
                            "http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv32.xsd")
            self.Comprobante.set("serie", "F")
            self.Comprobante.set("version", "3.2")
            self.Comprobante.set("folio", f"{InvoiceNo}")
            self.Comprobante.set("fecha","2016-07-04T10:05:41" )#f"{InvoiceDate}")
            self.Comprobante.set("sello",
                            "IV5qspgHRnyIh7jOoJ9uMJMbGydYejBXH43IIUCYbbfXfKr8Xuw/IGE7RAecJMIrs27HbPWrv9+1lW/iP2ZYj/dfKek5S9M9+eL9xhZMotAEsaizWBJmt7lSMVxPQm3kuklnP57I7FzE+0R8Gfx5xw0KvHWSh45SsA6MJzRq8dY=")
            self.Comprobante.set("tipoDeComprobante", "ingreso")
            self.Comprobante.set("formaDePago", "Pago en una sola exhibición")
            self.Comprobante.set("noCertificado", "00001000000305104410")
            self.Comprobante.set("certificado",
                            "MIIEgTCCA2mgAwIBAgIUMDAwMDEwMDAwMDAzMDUxMDQ0MTAwDQYJKoZIhvcNAQEFBQAwggGKMTgwNgYDVQQDDC9BLkMuIGRlbCBTZXJ2aWNpbyBkZSBBZG1pbmlzdHJhY2nDs24gVHJpYnV0YXJpYTEvMC0GA1UECgwmU2VydmljaW8gZGUgQWRtaW5pc3RyYWNpw7NuIFRyaWJ1dGFyaWExODA2BgNVBAsML0FkbWluaXN0cmFjacOzbiBkZSBTZWd1cmlkYWQgZGUgbGEgSW5mb3JtYWNpw7NuMR8wHQYJKoZIhvcNAQkBFhBhY29kc0BzYXQuZ29iLm14MSYwJAYDVQQJDB1Bdi4gSGlkYWxnbyA3NywgQ29sLiBHdWVycmVybzEOMAwGA1UEEQwFMDYzMDAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBEaXN0cml0byBGZWRlcmFsMRQwEgYDVQQHDAtDdWF1aHTDqW1vYzEVMBMGA1UELRMMU0FUOTcwNzAxTk4zMTUwMwYJKoZIhvcNAQkCDCZSZXNwb25zYWJsZTogQ2xhdWRpYSBDb3ZhcnJ1YmlhcyBPY2hvYTAeFw0xNDA5MTIxOTE2MzBaFw0xODA5MTIxOTE2MzBaMIHNMSswKQYDVQQDEyJBTEJFUlRPIEZSQU5DSVNDTyBQQVNBUkFOIEZJR1VFUk9BMSswKQYDVQQpEyJBTEJFUlRPIEZSQU5DSVNDTyBQQVNBUkFOIEZJR1VFUk9BMSswKQYDVQQKEyJBTEJFUlRPIEZSQU5DSVNDTyBQQVNBUkFOIEZJR1VFUk9BMRYwFAYDVQQtEw1QQUZBODIxMDA1SU44MRswGQYDVQQFExJQQUZBODIxMDA1SE1DU0dMMDMxDzANBgNVBAsTBnVuaWRhZDCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAhg68ZOyj2vxfp2D9phYNlaxTLI0vyx4Qn7k82CFrRZ1nJKWSl+3+o8aZzsdr0pTdwdM4DMquQtj8pgsaUqdKpRn2qYFjj+gAMR9Bet1h08122xIex1wp4OWeKpo5W9HSrWulC/de2lMC1OqxG/3c1BbJ1OnsamFPx/DgAdPNpa0CAwEAAaMdMBswDAYDVR0TAQH/BAIwADALBgNVHQ8EBAMCBsAwDQYJKoZIhvcNAQEFBQADggEBAEyMt38i5pX168IFCNY0aLOeM06HMimq+aeZlcYKxqjtE02tg3FnxJVKsfaotDUhlqG+WDgUQ2Xw2U355t5craVHONrU9efu6mZ0x1IZ3YTcZlmgylyToruoHZd4vACzoDqwZ9/tg2U5LK0g8rNiVSH8jo3G9F4dzYGXHaRnnOz2yXP5wkTSON0SnFPwb7e5vewGgXbT0DNFL7lk9dI3peXpaGevOLRrQ0f0+4KReAH27Tq3rbUzXQnzQHmnmJjbOY18ari7DD9/HwfdNa9PRcotLgcMvTeZRlzT/OY2xD1PhVWmbmym2S8uLhODckRvqSti7iaWl3/oYHFvLYot00c=")
            self.Comprobante.set("condicionesDePago", "Contado")
            self.Comprobante.set("subTotal", "4052.00")
            self.Comprobante.set("descuento", "0.00")
            self.Comprobante.set("TipoCambio", "1.0000")
            self.Comprobante.set("Moneda", "MXN")
            self.Comprobante.set("total", "4700.32")
            self.Comprobante.set("metodoDePago", "No identificado")
            self.Comprobante.set("LugarExpedicion", "Azcapotzalco, D.F.")

            Emisor = self.objectItem(self.Comprobante, "cfdi:Emisor", "rfc:::PAFA821005IN8",
                                "nombre:::ALBERTO FRANCISCO PASARAN FIGUEROA")
            DomicilioFiscal = self.objectItem(Emisor, "cfdi:DomicilioFiscal", "calle:::AURORA", "noExterior:::6 BIS",
                                         "colonia:::Santa Ines", "localidad:::México", "municipio:::Azcapotzalco",
                                         "estado:::D.F.", "pais:::Mexico", "codigoPostal:::02140")
            ExpedidoEn = self.objectItem(Emisor, "cfdi:ExpedidoEn", "calle:::AURORA", "noExterior:::6 BIS",
                                    "colonia:::Santa Ines", "municipio:::Azcapotzalco", "estado:::D.F.",
                                    "pais:::Mexico", "codigoPostal:::02140")
            RegimenFiscal = self.objectItem(Emisor, "cfdi:RegimenFiscal", "Regimen:::Regímen de Incorporación Fiscal")
            Receptor = self.objectItem(self.Comprobante, "cfdi:Receptor", f"rfc:::{CustomerID}",
                                  "nombre:::ANUNCIOS PREMIUM ESPECTACULARES S.A.DE C.V")
            Domicilio = self.objectItem(Receptor, "cfdi:Domicilio", "calle:::SANTO DOMINGO", "noExterior:::139",
                                   "municipio:::Azcapotzalco", "pais:::Mexico", "codigoPostal:::02760")

            Impuestos = self.objectItem(self.Comprobante, "cfdi:Impuestos", "totalImpuestosTrasladados:::648.32")
            Traslados = self.objectItem(Impuestos, "cfdi:Traslados")
            Traslado = self.objectItem(Traslados, "cfdi:Traslado", "impuesto:::IVA", "tasa:::16", "importe:::648.32")

            Complemento = self.objectItem(self.Comprobante, "cfdi:Complemento")
            TimbreFiscalDigital = self.objectItem(Complemento, "tfd:TimbreFiscalDigital",
                                             "xmlns:tfd:::http://www.sat.gob.mx/TimbreFiscalDigital",
                                             "xsi:schemaLocation:::http://www.sat.gob.mx/TimbreFiscalDigital http://www.sat.gob.mx/TimbreFiscalDigital/TimbreFiscalDigital.xsd",
                                             "version:::1.0", "UUID:::2DF1D377-AE53-4B0B-A5ED-78D3AE2FB0C1",
                                             "FechaTimbrado:::2016-07-04T10:20:41",
                                             "selloCFD:::IV5qspgHRnyIh7jOoJ9uMJMbGydYejBXH43IIUCYbbfXfKr8Xuw/IGE7RAecJMIrs27HbPWrv9+1lW/iP2ZYj/dfKek5S9M9+eL9xhZMotAEsaizWBJmt7lSMVxPQm3kuklnP57I7FzE+0R8Gfx5xw0KvHWSh45SsA6MJzRq8dY=",
                                             "noCertificadoSAT:::00001000000301100488",
                                             "selloSAT:::hohI1dFe5VFjazd6OLdZII8zlgMxFuXXWQNZGCz+1wCYU3TT1Yz7DdNgO6kvV7Vh1mFnTs+ZOk33JQ0sMDqnsDv+5RHrhXvHZDUErWgo0xsnr3guJcCov/v8EN5051qWj8m2K8A45qFjkfiLvCXF38jYwPosF0OrIXXzoxaNFjI=")

            self.Conceptos = self.objectItem(self.Comprobante, "cfdi:Conceptos")

            Concepto = self.objectItem(self.Conceptos, "cfdi:Concepto", f"cantidad:::{Quantity}", f"unidad:::{StockCode}",
                                       f"descripcion:::{Description}", f"valorUnitario:::{UnitPrice}", "importe:::4052.00")
            ComplementoConcepto = self.objectItem(Concepto, "cfdi:ComplementoConcepto")


            self.check=InvoiceNo
            self.NumTemp=num

        else:
            Concepto = self.objectItem(self.Conceptos, "cfdi:Concepto", f"cantidad:::{Quantity}", f"unidad:::{StockCode}",
                                       f"descripcion:::{Description}", f"valorUnitario:::{UnitPrice}", "importe:::4052.00")
            ComplementoConcepto = self.objectItem(Concepto, "cfdi:ComplementoConcepto")


    def objectItem(self,parent, title, *args):
        val = ET.SubElement(parent, title)
        if len(args) > 0:
            for item in args:
                data = item.split(":::")
                val.set(data[0], data[1])
        return val

    def read_Csv(self,file_Path):
        global Conceptos
        global Concepto
        global ComprobanteTemp

        data = pd.read_csv(file_Path, sep=',', encoding="ISO-8859-1")

        for index, row in data.iterrows():
            InvoiceNo = str(row["InvoiceNo"])
            StockCode = row["StockCode"]
            Description = row["Description"]
            Quantity = row["Quantity"]
            InvoiceDate = row["InvoiceDate"]
            UnitPrice = row["UnitPrice"]
            CustomerID = str(row["CustomerID"])
            CID = ("111111", CustomerID)[CustomerID != "nan"]
            cid=CID[:5]
            #print(InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, cid)
            self.buildFactura(InvoiceNo, str(InvoiceNo), cid, Description, StockCode, Quantity, InvoiceDate,UnitPrice)


file = "data.csv"
factura=Facturas()
factura.read_Csv(file)

