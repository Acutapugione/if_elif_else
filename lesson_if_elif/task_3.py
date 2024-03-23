# # Дмитрий Дементеев, [23.03.24 18:07]
# # 1) Користувач вводить число, 
# # ви перевіряєте парність і повідомляєте користувача
# number = int(input("Enter the number to check on:\t"))
# print("Парне" if number % 2 == 0 else "Непарне")

# # Дмитрий Дементеев, [23.03.24 18:09]
# # 2) Є список чисел, якщо в цьому списку є від'ємне число вивести список, якщо немає вивести "В списку немає від'ємних чисел"
# # def negative(x)->bool:
# #     return x < 0

# negative = lambda x : x < 0
# lst = [1, 2, 3, -4, 5, 6]
# print(lst if len(list(filter(negative, lst)))>0 else "В списку немає від'ємних чисел")
# # Дмитрий Дементеев, [23.03.24 18:11]
# # 3) Користувач вводить дані про студента та його оцінку за екзамен, якщо оцінка вища за 79.5 балів то екзамен пройдено успішно. Повідомити про успішність студента користувачеві.
# student_name = input(f"Enter student name:\t")

# number = float(input(f"Enter the mark for {student_name} exam:\t")) 

# verdict = "succed" if number > 79.5 else "failed"

# print(f"{student_name} {verdict} the exam with {number} mark." )


# 4*) FizzBuzz: користувач вводить число від 0 до 100, 
# якщо число ділиться на 3 без остачі - друкуємо "Fizz", 
# якщо число ділиться на 5 без остачі - "Buzz", 
# якщо обидві умови правдиві - "FizzBuzz"
# якщо число не в межах заданих від 0 до 100 вивести "BadFizz"
# number = int(input("Введіть число від 0 до 100:\t"))
# if number < 0 or number > 100: print("BadFizz")
# elif number % 3 == 0 or number % 5 == 0:
#     if number % 3 == 0 and number % 5 == 0: print("FizzBuzz")
#     elif number % 3 == 0: print("Fizz")
#     else: print("BadFizz")