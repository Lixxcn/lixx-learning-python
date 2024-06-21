import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai) -> None:
        """初始化飞船并设置其初始位置"""
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()
        self.settings = ai.settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # 每艘飞船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标识调整飞船的位置"""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
