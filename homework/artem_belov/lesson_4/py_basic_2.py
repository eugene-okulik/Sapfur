my_dict = dict()
my_dict['tuple'] = (3, 4, 8.11, 'text', 'text')
my_dict['list'] = [56, 42, 102, 63, 69]
my_dict['dict'] = {'num1': 1, 'num2': 2, 'num3': 3, 'num4': 4, 'num5': 5}
my_dict['set'] = {2, 3, 5, 8, 9}
last_tuple = my_dict['tuple'][-1]
print('Последний элемент ключа tuple: ', last_tuple)
my_dict['list'].append('list_new')
my_dict['list'].pop(1)
my_dict['dict'][('i am a tuple',)] = 'value'
my_dict['dict'].pop('num1')
my_dict['set'].add('new_set')
my_dict['set'].pop()
print(my_dict)
