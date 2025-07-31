# ScriptsContabilidad

PROYECTO PERSONAL QUE CONSTARA DE MULTIPLES SCRIPTS FUNCIONES, Y PROGRAMAS COMBINADOS DE VARIAS LIBREARIAS DE PYTHON PARA FACILITAR EL TRABAJO CONTABLE USANDO SOFTWARE COMO CONTPAQI Y EL LLEVAR LA CONTABILIDAD, ASI COMO FUNCIONES COMO COMPARAR TABLAS Y PDF Y ACELERAR PROCESOS DE IDENTIFICACION Y BUSQUEDA DE ELEMENOTS FALTANTES O DE POLIZAS SIN REGISTRAR.


COMO EJECUTAR

clona el repositorio en tu carpeta donde lo guardaras

Crear el entorno virutal para ejecutarlo
    python -m venv .venv
    source .venv/bin/activate

Descargas los requirements
    pip install requirements.txt

Ejemplo del menu en consola
'''
~ Seleccione que quiere hacer ~
- Convertir Estado de Cuenta PDF a Excel
- Buscar Movimientos Faltantes
- Exportar Templates Excel
'''

las 3 primeras funciones que se haran seran las bases de este programa para ser util 
- Convertir Estado de Cuenta PDF a Excel esta hecho para sacar excel en formato correcto y util de informacion valiosa del pdf de los bancos BBVA, Banamex, Banorte y Banregio.

- Buscar Movimientos Faltantes, usando los excel anteriores y el excel proveniente de contpaqi se puede hacer una busqueda rapida y marcar las filas de movimientos faltantes del estado de cuenta o marcar las cosas sin identificar del contpaqi

- Descargara un Templates que cree previamente en excel para el proceso de agregar el folio fiscal y en la creacion de documentos como DIOT, IVA Acreditable y otros mas. El template tendra una hoja con una explicacion de que que se necesita modificar y mover para usar el template de forma eficiente.


