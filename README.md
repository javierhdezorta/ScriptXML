# ScriptXML


# 1. Tener python 3.6 o Utilizar Anaconda.

Se recomienda utilizar anaconda con python 3.6, instalar :

https://www.anaconda.com/download/#linux


# 2. Descargar e instalar pycharm community:

https://www.jetbrains.com/pycharm/download/#section=linux


# 3. Clonar e importar proyecto a pycharm


# 4. Verificar que el interpreter de python, se este utilizando anaconda python 3.6 o en su caso un  virtualenv de anaconda


# 5. Verificar que los import se encuentre :

```from xml.etree import ElementTree as ET```
```import pandas as pd```


de otro modo instalarlos utilizando anaconda, tipear en consola :

```conda install -c anaconda lxml ```
y

```conda install -c anaconda pandas```


# Cambiar path que se encuentra en GenerateDataSet.py :

cambiar : ```/home/javier/facturas/``` ,  ```tu_path```.

Es la ruta en donde se van a  almacenar las facturas generadas en tu host local.


# 6. Una vez todo correcto ejecutar :

Ejecutar ```GenerateDataSet.py```









