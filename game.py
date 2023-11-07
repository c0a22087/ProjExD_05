import sys
import time
import pygame as pg


WIDTH = 1600  # ゲームウィンドウの幅
HEIGHT = 900  # ゲームウィンドウの高さ

#　ゴール機能
class Goal_m(pg.sprite.Sprite):

    """
    ゴールに関するクラス
    """

    def __init__(self):
                
        # ゴールを表示
            # screen = pg.display.set_mode((800, 900)) #画面の大きさ
            goal_img = pg.image.load("ex05/goal.png")
            goal2_img = pg.image.load("ex05/goal_txt.jpeg")
            self.goal_img = pg.transform.scale(goal_img, (250, 500)) #画像の大きさ
            # enn = pg.Surface((20, 20))

    def update(self,screen):
            screen.blit(self.goal_img, [500, 100])

        #キャラがゴールする
        


def main():
    pg.display.set_caption("タイトル")
    screen = pg.display.set_mode((800,600))
    back = pg.image.load("ex05/haikei.png")
    clock = pg.time.Clock() #時間を表す
    goal = None
    tmr = 0 
    while True:
        key_lst = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
        screen.blit(back,[0,0])
    

        tmr += 1
        if tmr == 60:
            goal = Goal_m()

        if goal is not None:
            goal.update(screen)
        clock.tick(60) #時間を更新 
        pg.display.update()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
