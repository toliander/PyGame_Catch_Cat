import pygame
import sys
import os
import subprocess

# Инициализация Pygame
pygame.init()

# Если вызвали из другой папки меняем рабочую директорию
current_dir = os.getcwd()
new_dir = '../../score_board/files'
os.chdir(new_dir)


class Button(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, sizex, sizey):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (sizex, sizey))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Определение размеров окна
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
# Размер кнопок
SIZE_X = 200
SIZE_Y = 200

# Создание окна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Score')

with open('results.txt', 'r') as file:
    scores = sorted([int(x) for x in file], reverse=True)

# Задаем шрифт
font = pygame.font.SysFont('arial', 32)

# Создание группы спрайтов для кнопок
button_group = pygame.sprite.Group()
back_button = Button('../static/back_button.png', WINDOW_WIDTH - SIZE_X, WINDOW_HEIGHT - SIZE_Y, SIZE_X, SIZE_Y)
# Добавление кнопок в группу спрайтов
for elem in (back_button,):
    button_group.add(elem)

# Основной цикл программы
running = True
exxit = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if back_button.rect.collidepoint(mouse_pos):
                running = False
                pygame.quit()
                subprocess.call(['python', "../../start_window/files/start_window.py"])
                exxit = True
    if not exxit:
        # Очистка экрана
        background = pygame.image.load(f"../../game_window/static/bg.jpg")
        background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
        screen.blit(background, (0, 0))

        for i in range(10):
            if i < len(scores):
                score_text = font.render(f'{i + 1} - {scores[i]}', True, 'BLACK')
            else:
                score_text = font.render(f'{i + 1} - ', True, 'BLACK')
            screen.blit(score_text, (WINDOW_WIDTH // 2 - 50, 50 * i + 50))

        # Отображение кнопок
        button_group.draw(screen)

        # Обновление экрана
        pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()
