import pygame
import sys
import os

# Инициализация Pygame
pygame.init()

# Если вызвали из другой папки меняем рабочую директорию
current_dir = os.getcwd()
new_dir = '../../score_board/files'
os.chdir(new_dir)


# Определение размеров окна
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Создание окна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Score')

with open('results.txt', 'r') as file:
    scores = sorted([int(x) for x in file], reverse=True)


# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    background = pygame.image.load(f"../../game_window/static/bg.jpg")
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.blit(background, (0, 0))


    #Задаем шрифт
    font = pygame.font.SysFont('arial', 32)
    for i in range(10):
        if i < len(scores):
            score_text = font.render(f'{i + 1} - {scores[i]}', True, 'BLACK')
        else:
            score_text = font.render(f'{i + 1} - ', True, 'BLACK')
        screen.blit(score_text, (WINDOW_WIDTH // 2 - 50, 50 * i + 50))

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()
