import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Определение размеров окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Создание окна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Catch The Cat !')


class Game():
    def __init__(self):
        self.score = 0
        self.lifes = 3


# Класс для статических изображений наследуется от основного окна
class StaticImage(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, sizex, sizey):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()  # Загрузка изображения с прозрачностью
        self.image = pygame.transform.scale(self.image, (sizex, sizey))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Cat(pygame.sprite.Sprite):
    def __init__(self, image_path, track, catch_pos):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.track = track
        self.rect = self.image.get_rect()
        self.pos = 0
        self.catch_pos = catch_pos
        self.rect.x, self.rect.y = track[self.pos]

    def next_pos(self):
        if self.pos + 1 < len(self.track):
            self.pos += 1
            self.rect.x, self.rect.y = self.track[self.pos]
        else:
            if hero.pos == self.catch_pos:
                game.score += 1
            else:
                game.lifes -= 1
            dynamic_group.remove(self)


class Hero(StaticImage):
    def __init__(self, image_path, x, y, sizex, sizey):
        super().__init__(image_path, x, y, sizex, sizey)
        self.pos = 1

    def change_pos(self, event):
        size = self.image.get_size()
        if event.key == pygame.K_UP:
            self.image = pygame.image.load('../dynamic/1.png').convert_alpha()
            self.pos = 1
        elif event.key == pygame.K_DOWN:
            self.image = pygame.image.load('../dynamic/3.png').convert_alpha()
            self.pos = 3
        elif event.key == pygame.K_LEFT:
            self.image = pygame.image.load('../dynamic/2.png').convert_alpha()
            self.pos = 2
        elif event.key == pygame.K_RIGHT:
            self.image = pygame.image.load('../dynamic/4.png').convert_alpha()
            self.pos = 4
        self.image = pygame.transform.scale(self.image, size)


# Создание группы спрайтов для статичных обьектов
static_group = pygame.sprite.Group()
# Создание группы спрайтов для динамичных обьектов
dynamic_group = pygame.sprite.Group()
game = Game()
# Размер статичных спрайтов
SIZE_X = 300
SIZE_Y = 150

# Загрузка изображений для треков и создание наборов точек для перемещений
left_rail_up = StaticImage('../static/1.png', 0,
                           WINDOW_HEIGHT * 0.2, SIZE_X, SIZE_Y)
left_rail_up_tr = []

right_rail_up = StaticImage('../static/2.png', WINDOW_WIDTH - SIZE_X,
                            WINDOW_HEIGHT * 0.2, SIZE_X, SIZE_Y)
right_rail_up_tr = []

left_rail_low = StaticImage('../static/3.png', 0,
                            WINDOW_HEIGHT - SIZE_Y, SIZE_X, SIZE_Y)
left_rail_low_tr = [(x, WINDOW_HEIGHT - SIZE_Y) for x in range(0, 300, 50)]

right_rail_low = StaticImage('../static/3.png', WINDOW_WIDTH - SIZE_X,
                             WINDOW_HEIGHT - SIZE_Y, SIZE_X, SIZE_Y)

right_rail_low_tr = []

# Добавление направляющих в группу спрайтов
for elem in (left_rail_up, right_rail_up, left_rail_low, right_rail_low):
    static_group.add(elem)

# Размер героя
HERO_HEIGHT = 400
HERO_WIDTH = 200

# Загрузка изображений
hero = Hero('../dynamic/1.png', (WINDOW_WIDTH - HERO_WIDTH) // 2,
            WINDOW_HEIGHT - HERO_HEIGHT, HERO_WIDTH, HERO_HEIGHT)

cat = Cat('../dynamic/cat.png', left_rail_low_tr, 2)
dynamic_group.add(cat)

background = pygame.image.load(f"../static/bg.jpg")
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Установка таймера анимации и генерации

animation_timer = pygame.time.get_ticks()
generation_timer = pygame.time.get_ticks()
# Установка шрифта
font = pygame.font.SysFont(None, 48)

# Начальное значение счета
score = 0

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
        elif event.type == pygame.KEYDOWN:
            hero.change_pos(event)
    if pygame.time.get_ticks() - generation_timer > (random.choice[1000, 2000, 3000, 4000]):
        pass # Не забудь написать код
    if pygame.time.get_ticks() - animation_timer > 1000:
        for elem in dynamic_group:
            elem.next_pos()
        animation_timer = pygame.time.get_ticks()
    # Очистка экрана
    screen.blit(background, (0, 0))
    screen.blit(hero.image, (hero.rect.x, hero.rect.y))
    # Отображение треков
    static_group.draw(screen)
    # Отображение двигающихся обьектов
    dynamic_group.draw(screen)
    # Отрисовка счета
    score_text = font.render(f'Score: {game.score}', True, 'BLACK')
    screen.blit(score_text, (10, 10))
    # Обновление экрана
    pygame.display.flip()
# Завершение работы Pygame
pygame.quit()
sys.exit()
