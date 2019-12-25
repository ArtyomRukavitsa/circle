import os
import random

import pygame

pygame.init()
pygame.mixer.pre_init(frequency=88000, size=-16, channels=2, buffer=512)
pygame.mixer.init()



size = WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode(size)
screen_rect = (0, 0, WIDTH, HEIGHT)
clock = pygame.time.Clock()
GRAVITY = 1

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    #image = image.convert_alpha()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image

# для отслеживания улетевших частиц
# удобно использовать пересечение прямоугольников


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    fire = [load_image("star.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = GRAVITY

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()

def start_screen():
    intro_text = "Happy New Year"

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.SysFont("Verdana", 40, False, True)

    string_rendered = font.render(intro_text, 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 50
    intro_rect.x = 50
    screen.blit(string_rendered, intro_rect)




all_sprites = pygame.sprite.Group()



file = 'data/happy.mp3'
pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.mixer.init()
pygame.mixer.music.load(file)

clock = pygame.time.Clock()
def create_particles(position):
    # количество создаваемых частиц
    particle_count = 120
    # возможные скорости
    numbers = range(-15, 16)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # создаём частицы по щелчку мыши
            create_particles(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pygame.mixer.music.play()

    all_sprites.update()
    start_screen()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
