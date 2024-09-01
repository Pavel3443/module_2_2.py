first = int(input('ведите first число: '))
second = int(input('ведите second число: '))
third = int(input('ведите third число: '))
if first == second and second == third and first == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)