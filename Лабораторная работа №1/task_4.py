users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
statistic_of_users = {"Общее количество":0,"Уникальные посещения":0}
statistic_of_users["Общее количество"] = len(users)
unique_users = len(set(users)) #кол-во уникальных посещений
statistic_of_users["Уникальные посещения"] = unique_users
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
print(statistic_of_users)