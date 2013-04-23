maintenance
===========

Aplicacion Para requistro de mantenimientos en veiculos de Empresa
INSTALACION

1) Instalar python y Agregar en variables de entorno 
  a) Instalar Python 2.7.3 de la pagina http://www.python.org/download/ 
  b) Agregar en variables de entorno de python EN PATH DE VARIABLES DE ENTORNO DE WINDWOS ";C:\Python27;C:\Python27\Lib;C:\Python27\DLLs;C:\Python27\Lib\lib-tk;C:\Python27\Scripts;"

2) Instalar setuptools-0.6c11.win32-py2.7 de la pagina https://pypi.python.org/pypi/setuptools

3) 
  a)Descargar pip de https://pypi.python.org/pypi/pip 
  b)descomprimir y Copiar carpeta de pip-1.3 a escritorio 
  c)copiar ruta de carpeta donde este el archivo manage.py ejemplo:
      "C:\Users\Admin\Desktop\pip-1.3\" 
    poneer en CMD   
      1) "cd C:\Users\Admin\Desktop\pip-1.3\"
      2)"python setup.py install"
    
4) copiar carpeta k19 a unidad c:
 entrar a carpeta donde se encuentre archivo manage.py ejemplo "C:\k19\maintenance\" 
  poneer en CMD   
  1)"cd C:\k19\maintenance\"
  2)"pip install requirements.txt"
  3)"python manage.py runserver 192.168.1.252:8000" <- la ip que tenga la maquina y el puerto donde se desee coorer la aplicacion

5)de la carpeta C:\k19\Iniciar Servidor\ copiar acceso directo de archivo IniciarS * si es nesesario cambiar ruta y direcion ip de archivo iniciarservidor de la misma carpeta

6)listo entrar a la ip 192.168.1.252:8000 para comprobar que funciona




