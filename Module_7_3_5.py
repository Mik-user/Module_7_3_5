team1_num = 8
team2_num = 6
team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'

# Использование %

print('В команде %s участников: %s!'% (team1_name,team1_num))
print('Итого сегодня в командах участников: %s и %s!'%(team1_num,team2_num))

# Использование format()

score_2 = 45
team1_time = 10872.2
team2_time = 10871.1

print('Команда {} решила задач: {}!'.format(team2_name,score_2))
print('{0} решили {1} задачи за {2} c!'.format(team2_name,score_2,team1_time))

score_1 = 47
time_avg =(team1_time+team2_time)/(score_2+score_1)

# Использование f строки
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print(f'Победа команды {team1_name}!')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_name:
    print(f'Победа команды {team2_name}!')
else:
    print('Ничья!')

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Сегодня было решено {score_1+score_2} задач, в среднем по {time_avg} секунды на задачу!')