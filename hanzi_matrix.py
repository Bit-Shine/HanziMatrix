import pygame
import random
import sys

# 初始化 Pygame
pygame.init()

# 设置屏幕大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('汉字 Matrix')

# 定义颜色
black = (0, 0, 0)
chinese_red = (238, 44, 44)

# 定义字体和字符集
font_size = 40  # 增大字体大小
# 使用 simhei 字体以支持中文字符
try:
    font = pygame.font.Font("simhei.ttf", font_size)
except FileNotFoundError:
    print("警告: simhei.ttf 字体文件未找到，将使用默认字体。")
    font = pygame.font.Font(None, font_size)

# 更丰富的汉字字符集
characters = '的了一是不了人我在有他这们要我们得上国了出一天行来用会发中作可和地主第一子了大来年月日把了手一水二心火木口门土山石田风花雪月春夏秋冬'

# 创建字符列表
class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(3, 8)  # 调整字符速度范围
        self.character = random.choice(characters)

    def draw(self):
        text_surface = font.render(self.character, True, chinese_red)
        screen.blit(text_surface, (self.x, self.y))

    def move(self):
        self.y += self.speed
        if self.y > screen_height:
            self.y = -font_size
            self.x = random.randint(0, screen_width - font_size)
            self.character = random.choice(characters)

# 初始化字符列表
num_characters = 300  # 增加字符数量
character_list = [Character(random.randint(0, screen_width - font_size), random.randint(-screen_height, screen_height)) for _ in range(num_characters)]

# 主循环
running = True
clock = pygame.time.Clock()

try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(black)

        for character in character_list:
            character.draw()
            character.move()

        pygame.display.flip()
        clock.tick(30)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    pygame.quit()
    input("Press Enter to exit...")  # 添加等待用户输入的语句
