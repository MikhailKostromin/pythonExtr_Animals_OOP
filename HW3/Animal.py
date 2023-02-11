class Animal:
    def __init__(self, name, feature, element, red_book, avr_life, speed, earth):
        self.name = name
        self.feature = feature
        self.element = element
        self.red_book = red_book
        self.avr_life = avr_life
        self.speed = speed
        self.earth = earth

    def show_info(self):
        print(f'==================================================\n'
              f'Название: {self.name}\n'
              f'Особенность: {self.feature}\n'
              f'Стихия:{self.element}\n'
              f'Присутствует в Красной книге: {self.red_book}\n'
              f'Cредняя продолжительность жизни: {self.avr_life}\n'
              f'Скорость: {self.speed} км/час')

    def definition(self):
        if self.element == 'Земля':
            print('У животного должны быть ЛАПЫ')
        elif self.element == 'Воздух':
            print('У животного должны быть КРЫЛЬЯ')
        elif self.element == 'Вода':
            print('У животного должны быть ЖАБРЫ или ПЛАВНИКИ')

    def rare(self):
        if self.red_book == 'Да':
            print(f'{self.name} - животное редкое или на грани вымирании ')
        else:
            print(f'{self.name} - животное НЕ редкое ')

    def age(self):
        if self.avr_life > 100:
            print(f'{self.name}-долгожитель')
        elif 100 > self.avr_life > 30:
            print(f'{self.name}  живет не долго')
        elif self.avr_life < 5:
            print(f'{self.name} живет мало')


    def world_travel(self):
        return print(f'Время Кругосвеетного путешествия '
                     f'составит: {self.earth / self.speed} часов')


eagle = Animal('Орёл', 'Крылья', 'Воздух', 'Нет', 40, 320, 40000)
eagle.show_info()
eagle.definition()
eagle.rare()
eagle.age()
eagle.world_travel()

whale = Animal('Гренландский кит', 'Плавники', 'Вода', 'Да', 200, 50, 40000)
whale.show_info()
whale.definition()
whale.rare()
whale.age()
whale.world_travel()

hamster = Animal('Хомяк', 'Лапы', 'Земля', 'Нет', 3, 5, 40000)
hamster.show_info()
hamster.definition()
hamster.rare()
hamster.age()
hamster.world_travel()
