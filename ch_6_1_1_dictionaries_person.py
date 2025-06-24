
favourite_numbers = {'person_a': [1,2,3],
                     'person_b': [4,5,6],
                    }

value = favourite_numbers['person_a']

print(value)
str_num = ''
i=0
for person, numbers in favourite_numbers.items():
    print(person)
    for num in numbers:
        if i==0: str_num=str_num + str(num)
        else: str_num=str_num + ', ' + str(num)
        i=i+1
    print(str_num)
    str_num=''
    i=0;

print(favourite_numbers.keys())