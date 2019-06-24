class Settings():
    """存储外星人入侵的所有类"""

    def __init__ (self):
        #def后面要有一个空格 不然会报错
        self.screen_width=1000
        self.screen_height=600
        self.bg_color=(230,230,230)

        # 飞船设置
        self.ship_speed_factor=1.5
        self.ship_limit=3
        # 子弹设置
        self.bullet_speed_factor=3
        self.bullet_width=3
        self.bullet_height=5
        self.bullet_color=60,60,60
        self.bullets_allowed=3

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed=50
        #fleet_direction为1表示右移 -1表示左移
        self.fleet_direction=1
