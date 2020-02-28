
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
# ???

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


from collections import Counter 

first_name_values = []

for student in students:
  name_student = student['first_name']
  first_name_values.append(name_student)

quantity_students = Counter(first_name_values)

for i in quantity_students:
  print(f'{i} : {quantity_students[i]}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# ???

# Пример вывода:
# Самое частое имя среди учеников: Маша

from collections import Counter

students_name = []

for student in students:
  name = student['first_name']
  students_name.append(name)

counts_name = Counter(students_name).most_common(1)
popular_name = counts_name[0]
print(f'Самое частое имя среди учеников: {popular_name[0]}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# ???

# # Пример вывода:
# # Самое частое имя в классе 1: Вася
# # Самое частое имя в классе 2: Маша


def most_popular_name(class_students):
  student_names = []
  for student in class_students:
      student_name = student['first_name']
      student_names.append(student_name)
  names_counter = Counter(student_names)
  return names_counter.most_common(1)[0][0]



for ind, people in enumerate(school_students):
  name = most_popular_name(people)
  print(f'Самое часто встречающееся имя в {ind + 1} классе: {name}')
  