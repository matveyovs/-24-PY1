numbers = [7, 43, 7, 8, 21, None, 99, 123, 55, 69, 11, 24, 87, -8, -38, -92, -45, 62, 53, 5]
numbers[5] = 0  #заменим none на о
# TODO заменить значение пропущенного элемента средним арифметическим
overall = sum(numbers)  #найдем сумму всех чисел
onerall = len(numbers)  #найдем колличество цифр
arifmet = overall / (onerall)  # найдем среднее арифметическое
numbers[5] = arifmet
print("Измененный список:", numbers)