import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置游戏窗口大小
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("打砖块游戏")

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# 定义字体
FONT = pygame.font.SysFont("SimHei", 20)

# 定义砖块的类


class Brick:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = 60
        self.height = 20
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.life = 1

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)

    def hit(self):
        self.life -= 1
        if self.life == 0:
            self.color = BLACK

# 定义小球的类


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 8
        self.color = WHITE
        self.speed_x = random.choice([-4, -3, -2, 2, 3, 4])
        self.speed_y = -3

    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # 小球碰到左右边界反弹
        if self.x - self.radius <= 0 or self.x + self.radius >= WINDOW_WIDTH:
            self.speed_x = -self.speed_x

        # 小球碰到上边界反弹
        if self.y - self.radius <= 0:
            self.speed_y = -self.speed_y

        # 小球碰到下边界，游戏结束
        if self.y + self.radius >= WINDOW_HEIGHT:
            return False

        return True

    def collide_with_paddle(self, paddle):
        if self.x + self.radius >= paddle.x and self.x - self.radius <= paddle.x + paddle.width and self.y + self.radius >= paddle.y:
            self.speed_y = -self.speed_y

    def collide_with_brick(self, brick):
        if brick.rect.collidepoint(self.x, self.y):
            brick.hit()
            if abs(self.speed_x) < 3:
                self.speed_x *= 2
            self.speed_y = -self.speed_y

# 定义挡板的类

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 80
        self.height = 10
        self.color = BLUE
        self.speed = 0

    def draw(self):
        pygame.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.speed

        # 检测挡板是否超出边界
        if self.x < 0:
            self.x = 0
        elif self.x > WINDOW_WIDTH - self.width:
            self.x = WINDOW_WIDTH - self.width

# 游戏循环


def main():
    # 创建游戏窗口
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Breakout Game")

    # 创建游戏对象
    ball = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    paddle = Paddle(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50)
    brick_group = BrickGroup(10, 6)

    # 创建游戏循环
    running = True
    while running:
        # 事件循环
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 游戏逻辑
        ball.move()
        ball.collide_with_wall()
        ball.collide_with_paddle(paddle)
        brick = ball.collide_with_brick(brick_group)
        if brick:
            brick_group.brick_list.remove(brick)

        paddle.move()
        if ball.y > paddle.y:
            running = False

        if len(brick_group.brick_list) == 0:
            running = False

        # 绘制游戏界面
        screen.fill((255, 255, 255))
        ball.draw(screen)
        paddle.draw(screen)
        brick_group.draw(screen)
        pygame.display.update()

    # 退出游戏
    pygame.quit()

if __name__ == '__main__':
    main()
