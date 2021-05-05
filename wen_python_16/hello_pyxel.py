import pyxel

# создаем класс программы (чертеж)
class App:
    # самая главная команда (конструктор)
    def __init__(self):
        # создаем pyxel-программу
        pyxel.init(160, 160, caption='Hello python v1.0')
        pyxel.run(self.update, self.draw)
    
    # обновление экрана
    def update(self):
        pass
       
    # рисование
    def draw(self):
        txt = list("Brawl Stas $$$")
        x = 60
        for letter in txt:
            # x, y, текст, цвет
            pyxel.text(x, 80, letter, 6)
            x = x + 5
    
# запуск чертежа (объект)
App()
