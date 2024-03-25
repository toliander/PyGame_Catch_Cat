import pygame
import sys
import subprocess
import os

# Инициализация Pygame
pygame.init()

# Если вызвали из другой папки меняем рабочую директорию
current_dir = os.getcwd()
new_dir = '../../start_window/files'
os.chdir(new_dir)

# Определение размеров окна
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Создание окна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Main Menu')


# Класс для кнопки
class Button(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, sizex, sizey):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()  # Загрузка изображения с прозрачностью
        self.image = pygame.transform.scale(self.image, (sizex, sizey))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Создание группы спрайтов для кнопок
button_group = pygame.sprite.Group()
# Размер кнопок
SIZE_X = 400
SIZE_Y = 150

# Загрузка изображений для кнопок
start_button = Button('../static/start_game.png', (WINDOW_WIDTH - SIZE_X) // 2, (WINDOW_HEIGHT - SIZE_Y) // 2 - 150,
                      SIZE_X,
                      SIZE_Y)
score_button = Button('../static/score_board.png', (WINDOW_WIDTH - SIZE_X) // 2, (WINDOW_HEIGHT - SIZE_Y) // 2, SIZE_X,
                      SIZE_Y)
exit_button = Button('../static/exit.png', (WINDOW_WIDTH - SIZE_X) // 2, (WINDOW_HEIGHT - SIZE_Y) // 2 + 150, SIZE_X,
                     SIZE_Y)

# Добавление кнопок в группу спрайтов
for elem in (start_button, score_button, exit_button):
    button_group.add(elem)


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
            if exit_button.rect.collidepoint(mouse_pos):  # Если нажали на кнопку выход то выход)
                running = False
                pygame.quit()
            if score_button.rect.collidepoint(mouse_pos):
                running = False
                pygame.quit()
                subprocess.call(['python', "../../score_board/files/score_window.py"])
            if start_button.rect.collidepoint(mouse_pos):
                running = False
                pygame.quit()
                subprocess.call(['python', "../../game_window/files/game_window.py"])

    if running:
        # Очистка экрана
        screen.blit(change_background_color(), (0, 0))

        # Отображение кнопок
        button_group.draw(screen)

        # Обновление экрана
        pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()
