class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings=ai_settings
        self.reset_stats()
        #游戏刚启动时，处于非活动状态
        self.game_active=False
        # 在任何情况下，都不应该重置最高得分
        self.high_score=0

    def reset_stats(self):
        """初始化在游戏运行时可能变化的统计信息"""
        self.ships_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1
