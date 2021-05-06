import time


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self, color_1, color_2, color_3):
        if color_1 == TrafficLight.__color[0] and color_2 == TrafficLight.__color[1] and color_3 == \
                TrafficLight.__color[2]:
            self.color_1 = color_1
            print(f'{self.color_1}')
            time.sleep(7)
            self.color_2 = color_2
            print(f'{self.color_2}')
            time.sleep(2)
            self.color_3 = color_3
            print(f'{self.color_3}')
            time.sleep(10)
        else:
            msg = 'Цвета указаны неверно'
            raise ValueError(msg)


tl = TrafficLight()
tl.running('красный', 'желтый', 'зеленый')
