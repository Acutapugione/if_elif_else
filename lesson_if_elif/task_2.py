#TODO: Створити програму отримує два реальних числа введених користувачем:
# 1) Знаходить середнє значення якщо обидва числа позитивні;
# 2) Знаходить їх мультиплікацію якщо обидва числа негативні;
# 3) Знаходить різницю квадратів якщо тільки одне з чисел негативне ; 

number_1 = float(input("Ввести перше число:"))
number_2 = float(input("Ввести друге число:"))
if number_1 > 0 and number_2 > 0:
    print((number_1 + number_2) /2)
elif number_1 < 0 and number_2 < 0:
    print(number_1 * number_2)
elif number_1 < 0 or number_2 < 0:
    print(number_1 ** 2 - number_2 ** 2)
        

safasf