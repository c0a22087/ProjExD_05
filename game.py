#import random
import sys
#import time
import pygame as pg


WIDTH = 1600  # ゲームウィンドウの幅
HEIGHT = 900  # ゲームウィンドウの高さ
earth = HEIGHT*3//4 #地面の高さ

class mario():
    """
    ゲームキャラクター（マリオ）に関するクラス
    """
    key_ls= {  # 押下キーと移動量の辞書
        pg.K_j: (0, -6), #
        pg.K_LEFT: (-1, 0),
        pg.K_RIGHT: (+1, 0),
        }

    def __init__(self):
        """
        マリオ画像Surfaceを生成する
        引数1 mro：マリオ画像ファイル名の番号
        引数2 xy：マリオ画像の位置座標タプル
        """

        #super().__init__()
        self.mro = pg.image.load("ex05/fig/mario_4_1.png") #デフォルトのマリオ画像
        self.mro = pg.transform.rotozoom(self.mro, 0, 0.4)
        # self.mro1 = pg.image.load("ex05/fig/mario_6.png") #歩くマリオ画像
        # self.mro1_1 = pg.transform.rotozoom(self.mro1, 10, 1.0) #回転した歩くマリオ画像
        # self.mro1_2 = pg.transform.flip(self.mro1, True, False) #左右反転
        # self.mro2 = pg.image.load("ex05/fig/mario_3.png") #ジャンプするマリオ画像
        self.mro_rct = self.mro.get_rect()
        # self.mro1_rct = self.mro1.get_rect()
        # self.mro1_1_rct = self.mro1_1.get_rect()
        # self.mro1_2_rct = self.mro1_2.get_rect()
        # self.mro2_rct = self.mro2.get_rect()
        self.mro_rct.center =[400, earth]
        # self.mro1_rct.center =[100, earth]
        # self.mro1_1_rct.center =[100, earth]
        # self.mro1_2_rct.center =[100, earth]
        # self.mro2_rct.center =[100, earth]
        # key_lst = pg.key.get_pressed()

    def update(self, screen: pg.Surface):
        """
        マリオの操作
        """
        # key_lst= {  # 押下キーと移動量の辞書
        # pg.K_j: (0, +1),
        # pg.K_LEFT: (-1, 0),
        # pg.K_RIGHT: (+1, 0),
        # }
        screen.blit(self.mro, self.mro_rct)
        # j_u = 4
        # if self.key_ls[pg.K_j]: #jキーが押されたら
        #     #self.mro.change_img(self.mro2, screen)
        #     #self.mro2.move_ip((0, j_u)) #ジャンプするマリオ画像を上に4動かす
        #     self.mro_rct.move_ip(0, j_u)
        # #self.mro.change_img(self.mro2, screen)
        # #self.mro2.move_ip((0, -j_u)) #ジャンプするマリオ画像を下に4動かす
        # self.mro_rct.move_ip(0, -j_u)

        # if not self.key_ls[pg.K_LEFT]: #左矢印が押されたら
        #     #self.mro.change_img(self.mro1_2, screen)
        #     #self.mro1_2.move_ip((-1, 0))
        #     #screen.blit(self.mro1_2, self.mro1_2_rct)
        #     self.mro_rct.move_ip(-1, -10)
        #     screen.blit(self.mro, self.mro_rct)
        # if not self.key_ls[pg.K_RIGHT]: #右矢印が押されたら
        #     #self.mro.change_img(self.mro1, screen)
        #     #self.mro1.move_ip((+1, 0))
        #     #screen.blit(self.mro1, self.mro1_rct)
        #     self.mro_rct.move_ip(+1, 0)
        #     screen.blit(self.mro, self.mro_rct)


def main():
    pg.display.set_caption("タイトル")
    screen = pg.display.set_mode((WIDTH,HEIGHT))
    #back = pg.image.load("ex05/haikei.png")
    back = pg.image.load("ex04/fig/pg_bg.jpg")
    mrio = pg.sprite.Group()
    mo = mario()
    clock = pg.time.Clock()
    key_ls= {  # 押下キーと移動量の辞書
        pg.K_j: (0, -6), #
        pg.K_LEFT: (-1, 0),
        pg.K_RIGHT: (+1, 0),
        }
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(mo.mro,(0,0))
        key_lst = pg.key.get_pressed()
        mro_mv = [0,1] #
        for key, mv in key_ls.items():
            if key_lst[key]:
                mro_mv[0] += mv[0]
                mro_mv[1] += mv[1]
        mo.mro_rct.move_ip(mro_mv[0], mro_mv[1])
        screen.blit(mo.mro, mo.mro_rct)

        # mrio.update(screen)
        # mo.update(screen)
        pg.display.update()
        screen.blit(back,[0,0])
        # clock.tick(50)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
    

