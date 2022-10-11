# 9. split()

s = 'string methods in python'.split(' ')
print(s) # Divide el string cada espacio (en este caso), devolviendo un array

s2 = 'string methods in python'.split(' ', maxsplit=1)
print(s2) # Lo mismo de arriba, pero estableces el máximo de splits que pueden ocurrir


#  10. rsplit()

s = 'string methods in python'.rsplit(' ', maxsplit=1)

print(s)

# Es lo mismo que split(), pero corta de derecha a izquierda