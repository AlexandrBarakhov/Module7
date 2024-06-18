team1 = 'Мастера кода'  # команда 1
team2 = 'Волшебники данных'  # команда 2
team1_num = 5  # количество участников в команде 1
team2_num = 6  # количество участников в команде 2
score_1 = 40  # количество решенных задач командой 1
score_2 = 42  # количество решенных задач командой 2
team1_time = 1552.512  # количество потраченного времени на решение задач командой 1
team2_time = 2153.31451  # количество потраченного времени на решение задач командой 2
tasks_total = score_1 + score_2  # общее количество решенных задач
# time_avg_1 = team1_time / score_1  # среднее время на задачу для команды 1
# time_avg_2 = team2_time / score_2  # среднее время на задачу для команды 2
time_avg = (team1_time + team2_time) / tasks_total  # среднее время на задачу по двум командам

if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'победа команды ' + team1 + ' !'
elif score_2 > score_1 or score_2 == score_1 and team2_time < team1_time:
    challenge_result = 'победа команды ' + team2 + ' !'
else:
    challenge_result = 'Ничья!'

# Использование %
print("В команде %s участников: %d !" % (team1, team1_num))
print("В команде %s участников: %d !" % (team2, team2_num))
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

# Использование format()
print("Команда {} решила задач: {} !".format(team1, score_1))
print("Команда {} решила задач: {} !".format(team2, score_2))
print("{} решили задачи за {} с !".format(team1, team1_time))
print("{} решили задачи за {} с !".format(team2, team2_time))

# Использование f-строк
print(f"Команды решили {score_1} и {score_2} задач .")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу !")
