# Числа
# Процентная ставка по вкладу составляет percent процентов годовых, которые прибавляются к сумме вклада. Вклад
# составляет depositrubles рублей depositpennies копеек. Определите размер вклада через год. Программа должна вывести
# result величину вклада через год в рублях. Часть копеек отбрасывается.
#
# Пример входных данных:
# percent = 12, deposit_rubles = 123451, deposit_pennies = 41.
#
# Пример выходных данных:
# result = 138265'.

#percent - процент
#deposit_rubles - вклад в рублях
#deposit_pennies - вклад в копейках
moneybefore = 100 * deposit_rubles + deposit_pennies
result = int(moneybefore * (100 + percent) / 100) // 100
print(result)
#
# Обратная связь с человеком
# Оценщик присвоил 2,50/2,50 очков.