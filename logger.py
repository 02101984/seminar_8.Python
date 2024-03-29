from data_create import input_user_data

def input_data():
    name, surname, phone, address = input_user_data()
    var = int(input(f'\nВ каком формате записать данные? \n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{address}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{address}\n\n'
                    f'Ваш выбор:' ))
    if var ==1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{address}\n\n')
            
    else:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')        
            

def print_data():
    print('1 файл:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))

    print('2 файл:')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(' '.join(data))

    file1 = open('data_first_variant.csv', 'r')
    textfile1 = file1.readlines(24)

    print(' '.join (textfile1))
