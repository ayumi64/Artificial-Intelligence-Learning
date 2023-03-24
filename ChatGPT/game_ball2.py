import pygame
import sys

# 定义常量
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BALL_SPEED = 5

# 初始化 Pygame
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("打砖块小游戏")

# 创建小球对象


class Ball:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def collide_with_wall(self, width, height):
        if self.x - self.radius < 0 or self.x + self.radius > width:
            self.speed_x = -self.speed_x
        if self.y - self.radius < 0:
            self.speed_y = -self.speed_y
        if self.y + self.radius > height:
            return True
        return False

    def collide_with_brick(self, brick):
        self.speed_y = -self.speed_y
        if self.x < brick.x:
            self.speed_x = -self.speed_x
            self.x = brick.x - self.radius
        elif self.x > brick.x + brick.width:
            self.speed_x = -self.speed_x
            self.x = brick.x + brick.width + self.radius
        elif self.y < brick.y:
            self.speed_y = -self.speed_y
            self.y = brick.y - self.radius
        else:
            self.speed_y = -self.speed_y
            self.y = brick.y + brick.height + self.radius

# 创建砖块对象


class Brick:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color,
                         (self.x, self.y, self.width, self.height))

# 创建挡板对象


class Paddle:
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color,
                         (self.x, self.y, self.width, self.height))

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def collide_with_ball(self, ball):
        if ball.y + ball.radius > self.y and \
           ball.y + ball.radius < self.y + self.height and \
           ball.x > self.x and \
           ball.x < self.x + self.width:
            ball.speed_y = -ball.speed_y

# 创建小球对象


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.color = GREEN
        self.speed_x = random.choice([-4, -3, 3, 4])
        self.speed_y = -4

    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # 检测小球是否撞到边界
        if self.x < self.radius or self.x > WINDOW_WIDTH - self.radius:
            self.speed_x = -self.speed_x

        if self.y < self.radius:
            self.speed_y = -self.speed_y
        elif self.y > WINDOW_HEIGHT:
            return False
        return True


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
