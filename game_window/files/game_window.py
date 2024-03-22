import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Создание окна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Catch The Cat !')


# Класс для статических изображений наследуется от основного окна
class StaticImage(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, sizex, sizey):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()  # Загрузка изображения с прозрачностью
        self.image = pygame.transform.scale(self.image, (sizex, sizey))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Hero(StaticImage):
    def __init__(self, image_path, x, y, sizex, sizey):
        super().__init__(image_path, x, y, sizex, sizey)
        self.pos = 1

    def change_pos(self):
        pass


# Создание группы спрайтов для статичных обьектов
static_group = pygame.sprite.Group()
# Размер кнопок
SIZE_X = 300
SIZE_Y = 150

# Загрузка изображений для треков

left_rail_up = StaticImage('../static/1.png', 0,
                           WINDOW_HEIGHT * 0.2, SIZE_X, SIZE_Y)
right_rail_up = StaticImage('../static/2.png', WINDOW_WIDTH - SIZE_X,
                            WINDOW_HEIGHT * 0.2, SIZE_X, SIZE_Y)
left_rail_low = StaticImage('../static/3.png', 0,
                            WINDOW_HEIGHT - SIZE_Y, SIZE_X, SIZE_Y)
right_rail_low = StaticImage('../static/3.png', WINDOW_WIDTH - SIZE_X,
                             WINDOW_HEIGHT - SIZE_Y, SIZE_X, SIZE_Y)

# Добавление кнопок в группу спрайтов
for elem in (left_rail_up, right_rail_up, left_rail_low, right_rail_low):
    static_group.add(elem)

# Размер героя
HERO_HEIGHT = 400
HERO_WIDTH = 200

# Загрузка изображения для героя
hero = Hero('../dynamic/base.png', (WINDOW_WIDTH - HERO_WIDTH) // 2,
            WINDOW_HEIGHT - HERO_HEIGHT, HERO_WIDTH, HERO_HEIGHT)

background = pygame.image.load(f"../static/bg.jpg")
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))


# Функция для изменения цвета фона
def change_background_color():
    current_time = pygame.time.get_ticks()  # Получение текущего времени в миллисекундах
    index = (current_time // 500) % 21  # Изменение номера картинки
    background = pygame.image.load(f"../static/anim_background/{index}.png")
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
    return background


# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

    # Очистка экрана
    screen.blit(background, (0, 0))
    screen.blit(hero.image, (hero.rect.x, hero.rect.y))

    # Отображение треков
    static_group.draw(screen)

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()
