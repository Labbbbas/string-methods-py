# 17./ 18./ 19. isalpha(), isnumeric(), isalnum()

s = 'python'
print(s.isalpha(), s.isnumeric(), s.isalnum())

s = '123'
print(s.isalpha(), s.isnumeric(), s.isalnum())

s = 'python123'
print(s.isalpha(), s.isnumeric(), s.isalnum())

# Si le pones un símbolo no alfabético ni numérico como -
# s.alnum() devuelve False, ya no True
s = 'python-123'
print(s.isalpha(), s.isnumeric(), s.isalnum())