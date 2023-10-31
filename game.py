import sys
# import time
import pygame as pg


WIDTH = 1200  # ゲームウィンドウの幅
HEIGHT = 675  # ゲームウィンドウの高さ

class mro():
    """
    ゲームキャラクター（マリオ）に関するクラス
    """
    key_lst= {  # 押下キーと移動量の辞書
        pg.K_j: (0, +1),
        pg.K_LEFT: (-1, 0),
        pg.K_RIGHT: (+1, 0),
    }

    def __init__(self, mro: int, xy: tuple[int, int]):
        """
        マリオ画像Surfaceを生成する
        引数1 mro：マリオ画像ファイル名の番号
        引数2 xy：マリオ画像の位置座標タプル
        """
        super().__init__()
        mro = pg.image.load("ex05/fig/mario_4.png") #デフォルトのマリオ画像
        mro1 = pg.image.load("ex05/fig/mario_6.png") #歩くマリオ画像
        mro1_1 = pg.transform.rotozoom(mro1, 10, 1.0) #回転した歩くマリオ画像
        mro1_2 = pg.transform.flip(mro1, True, False) #左右反転
        mro2 = pg.image.load("ex05/fig/mario_3.png") #ジャンプするマリオ画像
        #mro_rct = mro.get_rect()
        #mro_rct.center = 200, 100
        #screen.blit
        key_lst = pg.key.get_pressed()
        j_time = 0
        if key_lst[pg.K_j]: #jキーが押されたら
            mro2.move_ip((0, +1)) #ジャンプするマリオ画像を上に１動かす
            while True:
                j_time += 1
                if j_time > 3: #もし3秒ジャンプしたら
                    break
            #while True:
            #    mro2.move_ip((0, +1))

        elif key_lst[pg.K_LEFT]: #左矢印が押されたら
            mro1_2.move_ip((-1, 0))
        elif key_lst[pg.K_RIGHT]: #右矢印が押されたら
            mro1.move_ip((+1, 0))


def main():
    pg.display.set_caption("タイトル")
    screen = pg.display.set_mode((WIDTH,HEIGHT))
    back = pg.image.load("ex05/haikei.png")
    while True:
        screen.blit(back,[0,0])
        pg.display.update()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
    

