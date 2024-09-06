name = input('Введите ваше имя: ')
password = input('Введите ваш пароль: ')
password_confirm = input('Повторите ваш пароль: ')
if password == password_confirm:
    print('Вы успешно зарегистрировались')
    print('Здравствуйте', name)
else:
    print('Пароли не совпадают')