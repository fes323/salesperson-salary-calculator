import datetime
import sys
from pprint import pprint
import pandas as pd


def main_menu():
    '''
    Функция для главного меню.
    '''
    print('Для старта программы введите: /start\n'
          'Список команд: /help\n')
    user_command = input('Введите команду:\n')

    while True:
        if user_command == '/help':
            print('Список команд:\n'
                   '/start --- запустить программу.\n'
                   '/quit --- выйти из программы')
            user_command = input('Введите команду:\n')
        if user_command == '/quit':
            sys.exit()
        if user_command == '/start':
            salary(SALARY=37_500)
        else:
            print('Что-то пошло не так.\n'
                  'Возвращаемся в главное меню...\n')
            main_menu()


# SALARY=37_500 - это окладная часть за вычетом налога!
def salary(SALARY=37_500):
    '''
    Расчет заработной платы сотрудника
    '''
    print(f'Внимание!!! Оклад (с учетом вычета налога) указан {SALARY}\n')
    user_command = int(input('Введите количество сотрудников для расчета зарплаты: '))

    list_staff_names = []
    list_staff_qualifications = []
    list_staff_number_of_sales = []
    list_staff_salary = []
    list_sum_contract = []

    counter_staff = 0
    for i in range(0, user_command):
        counter_staff += 1
        staff_name = input(f'{counter_staff}. Введите ФИО сотрудника: ')
        list_staff_names.append(staff_name)

        staff_qualification = int(input('Введите процент от продажи сотрудника.\n'
                           '12 --- младший специалист.\n'
                           '15 --- старший специалист.\n'
                           '20 --- эксперт.\n'
                           'Вводить процент необходимо только числом, без знака процента!\n'))
        list_staff_qualifications.append(staff_qualification)

        number_of_sales = int(input('Введите количество продаж: '))
        list_staff_number_of_sales.append(number_of_sales)

        if number_of_sales > 20:
            print('Вы ввели слишком большое количество продаж. Возможно, произошла ошибка.\n'
                  'Начнем с начала...\n')
            salary(SALARY=37_500)
        else:
            amount_of_contract = []
            counter = 0
            for i in range(0, number_of_sales):
                counter += 1
                contract_value = int(input(f'Продажа №{counter}. Введите сумму сделки: '))
                amount_of_contract.append(contract_value)
                if number_of_sales > 1:
                    print(f'Вы добавили {contract_value} к сумме всех сделок.')

            sum_contract = sum(amount_of_contract)
            list_sum_contract.append(sum_contract)
            print(f'Общая сумма реализации: {sum_contract}')
            if number_of_sales > 1:
                if number_of_sales == 2:
                    motivation = 1.2
                if number_of_sales == 3:
                    motivation = 1.3
                if number_of_sales == 4:
                    motivation = 1.4
                if number_of_sales >= 5:
                    motivation = 1.5
                employee_salary = ((sum_contract / 100 * staff_qualification) * motivation)

            if number_of_sales == 1:
                employee_salary = sum_contract / 100 * staff_qualification

            tax_employee_salary = employee_salary * 0.13
            pure_employee_salary = (employee_salary - tax_employee_salary) + SALARY
            print(
                f'Зарплата сотрудника {staff_name}, с учетом вычета 13%, составляет: {round(pure_employee_salary, 2)}\n\n')
            list_staff_salary.append(pure_employee_salary)

            staff_list_dict = {
                'ФИО сотрудника': list_staff_names,
                'Квалификация (процент от сделки)': list_staff_qualifications,
                'Количество продаж': list_staff_number_of_sales,
                'Зарплата': list_staff_salary,
                'Общая сумма реализации': list_sum_contract,
            }

    user_command = input('Хотите экспортировать данные в эксель? Да или Нет (введите ответ): ')
    if user_command == 'Да':
        export_csv(staff_list_dict)
    else:
        print('Возвращаемся в главное меню...\n'
              'Для выхода введите: /quit\n')


def export_csv(staff_list_dict):
    data_date = datetime.date.today()
    print(data_date)
    df = pd.DataFrame(staff_list_dict)
    try:
        df.to_excel(f'./{data_date}_salary.xlsx')
        print('...\n'
              'Экспорт прошел успешно!\n'
              'Файл создан в текущей директории\n'
              'Возвращаемся в главное меню...\n')
    except:
        print('Произошла ошибка\n')
    finally:
        main_menu()


if __name__ == '__main__':
    print('Github: https://github.com/fes323/salesperson-salary-calculator\n'
          'Автор: Maksim Legeyda (fes323)\n')
    main_menu()