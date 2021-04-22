tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
tutors_1 = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses_1 = ['9А', '7В', '9Б', '9В', '8Б']


def tut_klass(lst_1, lst_2):
    if len(lst_1) > len(lst_2):
        for index in range(len(lst_2)):
            result = lst_1[index], lst_2[index]
            yield result
        for index in range(len(lst_2), len(lst_1)):
            result = lst_1[index], None
            yield result
    else:
        for index in range(len(lst_1)):
            result = lst_1[index], lst_2[index]
            yield result


print(tut_klass(tutors, klasses))
print(tut_klass(tutors_1, klasses_1))
a = tut_klass(tutors, klasses)
for el in a:
    print(el)
print(*a, 'генератор уже истощен')
b = tut_klass(tutors_1, klasses_1)
for el in b:
    print(el)
print(*b, 'генератор уже истощен')
