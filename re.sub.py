# 8. re.sub

import re

s = 'string    methods in python'

s2 = s.replace(' ', '-')
print(s2) # Remplaza 4 espacios por 4 guiones

s3 = re.sub('\s+' , '-', s)
print(s3) # Remplaza los espacios por guiones
          # Y si hay más de 1 espacio juntos,
          # borra los sobrantes