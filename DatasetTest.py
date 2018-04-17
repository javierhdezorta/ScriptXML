from xml.etree import ElementTree as ET
import pandas as pd
import  random


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


def buildFactura(num, InvoiceNo, CustomerID, InvoiceDate, Operation):
    root = ET.Element("root")
    ET.SubElement(root, "entityId").text = f"{CustomerID}"
    ET.SubElement(root, "entityType").text = "user"
    ET.SubElement(root, "event").text = f"{Operation}"
    ET.SubElement(root, "eventTime").text = f"{InvoiceDate}"
    ET.SubElement(root, "rating").text = "5"
    ET.SubElement(root, "targetEntityId").text = f"{InvoiceNo}"
    ET.SubElement(root, "targetEntityType").text = "item"

    indent(root)
    tree = ET.ElementTree(root)
    tree.write(f"/home/javier/facturas/factura{num}.xml")


def read_Csv(file_Path):
    data = pd.read_csv(file_Path, sep=',', encoding="ISO-8859-1")
    ops=["rate","buy"]

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
        operation=random.choice(ops)

        print(InvoiceNo,InvoiceNo,cid,InvoiceDate,operation)
        buildFactura(InvoiceNo, InvoiceNo, cid, InvoiceDate, operation)


if __name__ == "__main__":
    _file = "data.csv"
    read_Csv(_file)
