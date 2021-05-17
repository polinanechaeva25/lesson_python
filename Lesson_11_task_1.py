import re


class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f'{self.date}'

    @classmethod
    def get_data(cls, date):
        pattern = re.compile(r'(\d{2})-(\d{2})-(\d{4})')
        result = pattern.finditer(str(cls(date)))
        result_0 = pattern.match(str(cls(date)))
        try:
            if not result_0:
                raise ValueError('Неверный формат даты')
        except ValueError as err:
            return err
        else:
            for el in result:
                day = int(el.group(1))
                month = int(el.group(2))
                year = int(el.group(3))
            return day, month, year

    @staticmethod
    def check_tr(date_str, date_tpl):
        pattern = re.compile(r'(\d{2})-(\d{2})-(\d{4})')
        result_0 = pattern.match(str(date_str))
        if not result_0:
            return 'Дата должна быть введена в формате дд-мм-гггг'
        else:
            day, month, year = date_tpl
            if not (day in range(1, 31)):
                return 'Неверный формат даты, максимальное количество дней = 31'
            if not (month in range(1, 13)):
                return 'Неверный формат даты, максимальное количество месяцев = 12'
            return 'Дата введена верно'


test_1 = Date('12/13-2021')
print(test_1.get_data(test_1))
print(Date.check_tr(test_1, test_1.get_data(test_1)))
print()

test_2 = Date('21-01-2021')
print(test_2.get_data(test_2))
print(Date.check_tr(test_2, test_2.get_data(test_2)))
