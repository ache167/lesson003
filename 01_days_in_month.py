# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
while True:
    user_input = input("Введите, пожалуйста, номер месяца (or exit to close): ")
    if user_input.lower() != 'exit':
        try:
            month = int(user_input)
            print('Вы ввели', month)
            if month == 1:
                print("There is", 31, "days in this month")
            elif month == 2:
                print("There is", 28, "days in this month")
            elif month == 3:
                print("There is", 31, "days in this month")
            elif month == 4:
                print("There is", 30, "days in this month")
            elif month == 5:
                print("There is", 31, "days in this month")
            elif month == 6:
                print("There is", 30, "days in this month")
            elif month == 7:
                print("There is", 31, "days in this month")
            elif month == 8:
                print("There is", 31, "days in this month")
            elif month == 9:
                print("There is", 30, "days in this month")
            elif month == 10:
                print("There is", 31, "days in this month")
            elif month == 11:
                print("There is", 30, "days in this month")
            elif month == 12:
                print("There is", 31, "days in this month")
            else:
                print('There is no such month number, please enter 1 - 12')
        except ValueError:
            print("Error, input must be a number.")
    else:
        break
