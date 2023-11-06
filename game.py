import random
import sys
import time
import pygame as pg


WIDTH = 1800  # ゲームウィンドウの幅
HEIGHT = 900  # ゲームウィンドウの高さ
earth = HEIGHT*3//4 #地面の高さ

class mro():
    """
    ゲームキャラクター（マリオ）に関するクラス
    """
    key_lst= {  # 押下キーと移動量の辞書
        pg.K_j: (0, +1),
        pg.K_LEFT: (-1, 0),
        pg.K_RIGHT: (+1, 0),
        }

    def __init__(self, key_lst):
        """
        マリオ画像Surfaceを生成する
        引数1 mro：マリオ画像ファイル名の番号
        引数2 xy：マリオ画像の位置座標タプル
        """

        super().__init__()
        self.mro = pg.image.load("ex05/fig/mario_4.png") #デフォルトのマリオ画像
        self.mro1 = pg.image.load("ex05/fig/mario_6.png") #歩くマリオ画像
        self.mro1_1 = pg.transform.rotozoom(self.mro1, 10, 1.0) #回転した歩くマリオ画像
        self.mro1_2 = pg.transform.flip(self.mro1, True, False) #左右反転
        self.mro2 = pg.image.load("ex05/fig/mario_3.png") #ジャンプするマリオ画像
        self.mro_rct = self.mro.get_rect()
        self.mro1_rct = self.mro1.get_rect()
        self.mro1_1_rct = self.mro1_1.get_rect()
        self.mro1_2_rct = self.mro1_2.get_rect()
        self.mro2_rct = self.mro2.get_rect()
        self.mro_rct.center =[100, earth]
        self.mro1_rct.center =[100, earth]
        self.mro1_1_rct.center =[100, earth]
        self.mro1_2_rct.center =[100, earth]
        self.mro2_rct.center =[100, earth]
        key_lst = pg.key.get_pressed()

    def update(self, screen: pg.Surface, key_lst):
        """
        マリオの操作
        """
        key_lst= {  # 押下キーと移動量の辞書
        pg.K_j: (0, +1),
        pg.K_LEFT: (-1, 0),
        pg.K_RIGHT: (+1, 0),
        }

        j_time = 0
        if key_lst[pg.K_j]: #jキーが押されたら
            while True:
                j_time += 1
                self.mro2.move_ip((0, j_time)) #ジャンプするマリオ画像を上に１動かす
                if j_time > 3: #もし3秒ジャンプしたら
                    break
            while True:
                j_time -= 1
                self.mro2.move_ip((0, j_time)) #ジャンプするマリオ画像を下に１動かす
                if j_time <= 0: #もし地面に着いたら
                    break

        elif key_lst[pg.K_LEFT]: #左矢印が押されたら
            self.mro1_2.move_ip((-1, 0))
            screen.blit(self.mro1_2, self.mro1_2_rct)
        elif key_lst[pg.K_RIGHT]: #右矢印が押されたら
            self.mro1.move_ip((+1, 0))
            screen.blit(self.mro1, self.mro1_rct)


def main():
    pg.display.set_caption("タイトル")
    screen = pg.display.set_mode((WIDTH,HEIGHT))
    back = pg.image.load("ex05/haikei.png")
    while True:
        screen.blit(back,[0,0])
        mro.update(screen)
        pg.display.update()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
    

