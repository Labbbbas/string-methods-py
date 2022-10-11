# 21. find()

s = 'Machine Learning'
idx = s.find('a')

print(idx)
print(s[idx:])

# Ignora la primera ocurrencia y va a la segunda
s = 'Machine Learning'
idx = s.find('a', 2)

print(idx)
print(s[idx:])


# 22. rfind()
# Es lo mismo que find(), pero toma como primer match
# de derecha a izquierda

s = 'Machine Learning'
idx = s.rfind('a')

print(idx)
print(s[idx:])