# Gestion de organigrama

Desarrollo de examen técnico

![alt text](images/image.png "Vista previa")

Consiste en gestionar areas de un organigrama:

1. Leer el codigo de area
2. Leer el nombre del area
3. Cantidad de personas del area
4. Leer el codigo del nodo padre si corresponde
5. permitir agregar, borrar, imprimir

# Clases

### Organigrama

````python
# imprimir organigrama
def render():
    pass


# agregar area al objeto asignado
def add_area(area, area_parent=None):
    pass


# borrar area
def delete_area(area):
    pass
````

### Area

````python
# info del area padre
def get_parent():
    pass


# info de areas hijas
def get_childs():
    pass


# imprimir jerarquia
def render():
    pass
````
