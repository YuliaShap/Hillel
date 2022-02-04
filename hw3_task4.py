days, hours = map(int, input("Введите количество земных дней, количество часов: ").split(", "))
sol = (days + hours / 24) * 1.02595675
print("Количество солов: ", round(sol, 2))
