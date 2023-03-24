import pygame
import random

# 初始化 Pygame
pygame.init()

# 定义窗口大小和标题
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 800
WINDOW_TITLE = "Plane War"
WINDOW_ICON = pygame.image.load("images/icon.png")
BG_COLOR = (255, 255, 255)

# 创建窗口
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)
pygame.display.set_icon(WINDOW_ICON)

# 加载图像
background_image = pygame.image.load("images/background.png").convert()
player_image = pygame.image.load("images/player.png").convert_alpha()
enemy_image = pygame.image.load("images/enemy.png").convert_alpha()

# 设置字体
font = pygame.font.Font(None, 36)

# 定义常量
PLAYER_SPEED = 5
ENEMY_SPEED = 3
ENEMY_INTERVAL = 50
ENEMY_COUNT = 5

# 定义变量
player_x = WINDOW_WIDTH // 2 - player_image.get_width() // 2
player_y = WINDOW_HEIGHT - player_image.get_height() - 50
player_rect = player_image.get_rect()
player_rect.x = player_x
player_rect.y = player_y
enemy_list = []

# 定义函数


def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    window.blit(text_surface, text_rect)


def spawn_enemy():
    enemy_x = random.randint(0, WINDOW_WIDTH - enemy_image.get_width())
    enemy_y = -enemy_image.get_height()
    enemy_rect = enemy_image.get_rect()
    enemy_rect.x = enemy_x
    enemy_rect.y = enemy_y
    enemy_list.append(enemy_rect)


def move_player(dx, dy):
    global player_x, player_y
    player_x += dx
    player_y += dy
    if player_x < 0:
        player_x = 0
    elif player_x > WINDOW_WIDTH - player_image.get_width():
        player_x = WINDOW_WIDTH - player_image.get_width()
    if player_y < 0:
        player_y = 0
    elif player_y > WINDOW_HEIGHT - player_image.get_height():
        player_y = WINDOW_HEIGHT - player_image.get_height()
    player_rect.x = player_x
    player_rect.y = player_y


def move_enemy():
    global enemy_list
    for enemy_rect in enemy_list:
        enemy_rect.y += ENEMY_SPEED


def detect_collision():
    global enemy_list
    for enemy_rect in enemy_list:
        if enemy_rect.colliderect(player_rect):
            return True
    return False


# 游戏循环
clock = pygame.time.Clock()
score = 0
game_over = False
while not game_over:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_player(0, -PLAYER_SPEED)
            elif event.key == pygame.K_DOWN:
                move_player(0, PLAYER_SPEED)
            elif event.key == pygame.K_LEFT:
                move_player(-PLAYER_SPEED, 0)
            elif event.key == pygame.K_RIGHT:
                move_player(PLAYER_SPEED, 0)

 # 生成敌机
    if len(enemy_list) < max_enemies and time.time() - last_enemy_time > enemy_interval:
        enemy = Enemy(random.randint(0, WIDTH - enemy_width), -
                      enemy_height, enemy_speed)
        enemy_list.append(enemy)
        last_enemy_time = time.time()

    # 更新和绘制敌机
    for enemy in enemy_list:
        enemy.update(dt)
        enemy.draw(screen)

    # 删除超出屏幕的敌机
    enemy_list = [enemy for enemy in enemy_list if enemy.y < HEIGHT]

    # 检测敌机和子弹的碰撞
    for bullet in player.bullet_list:
        for enemy in enemy_list:
            if bullet.collide(enemy):
                enemy_list.remove(enemy)
                player.bullet_list.remove(bullet)
                score += 1
                break
