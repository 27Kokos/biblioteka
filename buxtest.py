sotrudniki = []
admin_password = 'adminΩ'

def add_employee():
    print("\nВвод нового сотрудника ")
    fio = input("ФИО: ")
    dni = int(input("Количество рабочих дней: "))
    chasy = float(input("Количество часов: "))
    stavka = float(input("Ставка в час: "))
    zp = chasy * stavka
    sotrudniki.append([fio, dni, chasy, stavka, zp])
    print(f"Зарплата: {zp}")
    print("Сотрудник добавлен!")

while True:
    print("1. Добавить сотрудника и посчитать зарплату (Только администратор)")
    print("2. Показать список всех сотрудников")
    print("3. Показать статистику (средние значения)")
    print("4. Кредитный калькулятор")
    print("5. Расчёт минимального срока кредита")
    print("6. Выйти")
    
    vybor = input("Ваш выбор: ")
    
    if vybor == "1":
        password = print("Введите пароль администратора: ")
        if password != admin_password:
            print("Доступ запрещён!")
        else:
            add_employee()
    
    elif vybor == "2":
        if len(sotrudniki) == 0:
            print("\nСписок пуст!")
        else:
            print("\nВсе сотрудники ")
            for i, zap in enumerate(sotrudniki, 1):
                print(f"\nСотрудник №{i}:")
                print(f"  ФИО: {zap[0]}")
                print(f"  Рабочих дней: {zap[1]}")
                print(f"  Отработанных часов: {zap[2]}")
                print(f"  Ставка в час: {zap[3]} руб./час")
                print(f"  Зарплата: {zap[4]:.2f} руб.")
    
    elif vybor == "3":
        if len(sotrudniki) == 0:
            print("\nНет данных для статистики! Список пуст.")
        else:
            sum_dni = 0
            sum_chasy = 0
            sum_zp = 0
            for zap in sotrudniki:
                sum_dni += zap[1]
                sum_chasy += zap[2]
                sum_zp += zap[4]
            
            kolvo = len(sotrudniki)
            sred_dni = sum_dni / kolvo
            sred_chasy = sum_chasy / kolvo
            sred_zp = sum_zp / kolvo
            
            print(f"Всего сотрудников: {kolvo}")
            print(f"Среднее количество рабочих дней: {sred_dni:.1f}")
            print(f"Среднее количество отработанных часов: {sred_chasy:.1f}")
            print(f"Средняя заработная плата: {sred_zp:.2f} руб.")
    
    elif vybor == "4":
        print("\nКредитный калькулятор")
        summa = float(input("Сумма кредита: "))
        procent_god = float(input("Годовая процентная ставка (в процентах): "))
        let = float(input("Срок кредита (в годах): "))
        
        procent_mes = procent_god / 100 / 12  
        mesyacev = let * 12                   

        if procent_mes == 0:
            platezh = summa / mesyacev
        else:
            koef = (1 + procent_mes) ** mesyacev
            platezh = summa * procent_mes * koef / (koef - 1)
        
        print(f"\nЕжемесячный платёж: {platezh:.2f}\n")
    
    elif vybor == "5":
        print("\nРасчёт минимального срока кредита")
        try:
            amount = float(input("Сумма кредита: "))
            annual_rate = float(input("Годовая процентная ставка (%): "))
            monthly_profit = float(input("Ежемесячная прибыль компании: "))
            spend_percent = float(input("Процент прибыли на погашение (%): "))
        except ValueError:
            print("Ошибка: введите корректные числа.\n")
            continue
        payment = monthly_profit * (spend_percent / 100)
        if payment <= 0:
            print("Ошибка: платёж должен быть положительным.\n")
            continue
        monthly_rate = annual_rate / 100 / 12
        debt = amount
        months = 0
        max_months = 1200  
        
        while debt > 0 and months < max_months:
            months += 1
            debt = debt * (1 + monthly_rate)  
            if debt <= payment:
                debt = 0  
            else:
                debt -= payment
        if debt > 0:
            print(f"За {max_months} месяцев кредит не погашен. Увеличьте платёж или срок.\n")
        else:
            print(f"\nМинимальный срок погашения: {months} месяцев")
            years = months // 12
            rest_months = months % 12
            if years > 0:
                print(f"Это составляет {years} лет и {rest_months} месяцев.\n")
            else:
                print(f"Это составляет {rest_months} месяцев.\n")
    elif vybor == "6":
        print("До свидания!")
        break
    
    else:
        print("Неправильный выбор! Введите число от 1 до 6.")