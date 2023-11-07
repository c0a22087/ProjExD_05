import sys
# import time
import pygame as pg


WIDTH = 1600  # ゲームウィンドウの幅
HEIGHT = 900  # ゲームウィンドウの高さ


class Tekimod:
    
    def __init__(self):
        #キラーの初期設定
        
        self.kira_img=pg.image.load("ex05/fig/kira1.1.png")
        self.kira_img=pg.transform.rotozoom(self.kira_img,0,0.2)
        self.kira_rct=self.kira_img.get_rect()
        self.kira_rct.center=[1600,400]
        self.kira_x=-2
        self.kira_y=0
        #ボム兵  self.image = tools.load_image("data", "rabipple.png", -1)

        self.bomu_img=pg.image.load("ex05/fig/bomu1.1.png")
        self.bomu_img=pg.transform.rotozoom(self.bomu_img,0,2)
        self.bomu_rct=self.bomu_img.get_rect()
        self.bomu_rct.center=[800,0]
        self.bomu_x=-1
        self.bomu_y=+3

        #クリボー
        self.kuribo_img=pg.image.load("ex05/fig/kuribo1.1.png")
        self.kuribo_img=pg.transform.rotozoom(self.kuribo_img,0,2)
        self.kuribo_rct=self.kuribo_img.get_rect()
        self.kuribo_rct.center=[1500,600]
        self.kuribo_x=-1
        self.kuribo_y=1

        #パックン
        self.pakkun_img=pg.image.load("ex05/fig/pakkun1.1.png")
        self.pakkun_img=pg.transform.rotozoom(self.pakkun_img,0,2)
        self.pakkun_rct=self.pakkun_img.get_rect()
        self.pakkun_rct.center=[1200,600]
        


    def update(self, screen: pg.Surface):
        #キラー
        self.kira_rct.move_ip(self.kira_x,self.kira_y)
        screen.blit(self.kira_img,self.kira_rct)
        #ボムー
        self.bomu_rct.move_ip(self.bomu_x,self.bomu_y)
        screen.blit(self.bomu_img,self.bomu_rct)
        #クリボー
        self.kuribo_rct.move_ip(self.kuribo_x,self.kuribo_y)
        screen.blit(self.kuribo_img,self.kuribo_rct)
        #パックン
        screen.blit(self.pakkun_img,self.pakkun_rct)




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
        teki.update(screen)#敵mobを追加
        
        
    
        
        pg.display.update()
       
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()


#mobの背景をなくす
#画面外に出たら消す
#複数mobが生成されるようにする。
    

