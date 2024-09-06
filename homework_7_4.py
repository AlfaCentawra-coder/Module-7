team1_num = 5
team2_num = 6
print('В команде Мастеры кода %s участников' % team1_num)
print('В команде Волшебники данных %s участников' % team2_num)
print('Итого сегодня в командах по %(team1_num)s, и по %(team2_num)s участников' % {'team1_num': 5, 'team2_num': 6})

score_1 = 40
team1_time = 1552.512
print("Команда Мастеры кода решила {score_1} задачи".format(score_1 = score_1))
print("Мастеры кода решили задачи за {team1_time} с".format(team1_time = str(team1_time)))

score_2 = 42
team2_time = 2153.31451
print("Команда Волшебники данных решила {score_2} задачи".format(score_2 = score_2))
print("Волшебники данных решили задачи за {team2_time} с".format(team2_time = team2_time))

tasks_total = score_1 + score_2
print(f'Колисество решенных задач {tasks_total}')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных'
else:
    result = 'Ничья!'

print(f"Результат битвы: {result}")


time_avg = sum((team2_time, team1_time)) / tasks_total


print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")