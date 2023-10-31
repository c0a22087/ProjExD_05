import sys
# import time
import pygame as pg


WIDTH = 1600  # ゲームウィンドウの幅
HEIGHT = 900  # ゲームウィンドウの高さ


class Tekimod:
    def __init__(self):
        #キラーの初期設定
        self.kira_img=pg.image.load("ex05/fig/kira.jpg")
        self.kira_img=pg.transform.rotozoom(self.kira_img,0,0.1)
        self.kira_rct=self.kira_img.get_rect()
        self.kira_rct.center=[1600,600]
        self.kira_x=-1
        self.kira_y=0
        #ボム兵
        self.bomu_img=pg.image.load("ex05/fig/bom.jpg")
        self.bomu_img=pg.transform.rotozoom(self.bomu_img,0,0.3)
        self.bomu_rct=self.bomu_img.get_rect()
        self.bomu_rct.center=[800,0]
        self.bomu_x=0
        self.bomu_y=+1

    def update(self, screen: pg.Surface):
        #キラー
        self.kira_rct.move_ip(self.kira_x,self.kira_y)
        screen.blit(self.kira_img,self.kira_rct)
        #ボムー
        self.bomu_rct.move_ip(self.bomu_x,self.bomu_y)
        screen.blit(self.bomu_img,self.bomu_rct)




def main():
    pg.display.set_caption("タイトル")
    screen = pg.display.set_mode((1600,900))
    teki=Tekimod()

    tmr=0
    clock=pg.time.Clock()

    back = pg.image.load("ex05/fig/pg_bg.jpg")
    while True:
        # for event in pg.event.get():
        #     if event.type == pg.QUIT: 
        #         return
       
        screen.blit(back,[0,0])
        teki.update(screen)
        
    
        
        pg.display.update()
       
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
    

