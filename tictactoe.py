import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        colors = [pygame.Color('red'), pygame.Color('blue')]
        color = colors[1]
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, (255, 255, 255), (self.left + i * self.cell_size,
                    self.top + j * self.cell_size, self.cell_size, self.cell_size), 1)
                if self.board[j][i] == 1:
                    print(self.board[j][i])
                    if color == pygame.Color('red'):
                        x = self.left + i * self.cell_size + self.cell_size // 2
                        y = self.top + j * self.cell_size + self.cell_size // 2
                        pygame.draw.circle(screen, color, (x, y), self.cell_size // 2 - 2, 2)
                    else:
                        x = self.left + i * self.cell_size + 2
                        y = self.top + j * self.cell_size + 2
                        pygame.draw.line(screen, color, (x, y), (x + self.cell_size - 2, y + self.cell_size - 2), 2)
                        pygame.draw.line(screen, color, (x, y + self.cell_size - 4), (x + self.cell_size - 4, y), 2)
                    self.board[j][i] = 2 # нейтральное положение
                    color = pygame.Color('red') if color == pygame.Color('blue') else pygame.Color('blue')

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos[0], mouse_pos[1]
        y_kl = (x - self.left) // self.cell_size
        x_kl = (y - self.top) // self.cell_size
        if (y_kl < 0 or y_kl >= self.width) or (x_kl < 0 or x_kl >= self.height):
            return
        return x_kl, y_kl

    def on_click(self, cell_coords):
        x, y = cell_coords[0], cell_coords[1]
        if self.board[x][y] == 0:
            self.board[x][y] = 1


pygame.init()
size = width, height = 320, 230
screen = pygame.display.set_mode(size)
board = Board(10, 7)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
pygame.quit()
