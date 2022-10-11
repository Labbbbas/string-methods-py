# 5. removeprefix()

s = 'Arthur: three!'.lstrip('Arthur: ')
print(s) # Quita TODOS los caracteres que hagan match,
         # como las t y la r

s2 = 'Arthur: three!'.removeprefix('Arthur: ')
print(s2) # Solo quita el segmento que hace match


# 6. removesuffix()

s3 = 'HelloPython'.removesuffix('Python')
print(s3)

# prefix busca de adelante hacia atrás
# suffix busca de atrás para adelante