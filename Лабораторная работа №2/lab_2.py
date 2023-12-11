salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for _ in range(months):
    need_money -= salary
    need_money += spend
    spend *= (1 + increase)


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(need_money, 2))
