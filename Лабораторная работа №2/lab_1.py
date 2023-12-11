money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 1  # количество месяцев, которое можно прожить
money_capital += salary
money_capital -= spend

while money_capital - spend >= 0:
    money_capital += salary
    money_capital -= spend
    spend *= (1 + increase)
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
