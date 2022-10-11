# 31. zfill()

s = '42'.zfill(5)
print(s)

s = '-42'.zfill(5)
print(s)

s = '+42'.zfill(5)
print(s)

# Te regresa un string según el lenght que le des, en este caso 5
# Y si faltan caractéres, te agrega ceros a la izquierda
# Pero si hay símbolos + -, los pones primero y luego los ceros