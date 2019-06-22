class Settings():
    """存储外星人入侵的所有类"""

    def __init__ (self):
        #def后面要有一个空格 不然会报错
        self.screen_width=1000
        self.screen_height=600
        self.bg_color=(230,230,230)
        self.ship_speed_factor=1.5

        # 子弹设置
        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=5
        self.bullet_color=60,60,60
        self.bullets_allowed=3