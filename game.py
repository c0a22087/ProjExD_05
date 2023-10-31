import sys
# import time
import pygame as pg


WIDTH = 1600  # ゲームウィンドウの幅
HEIGHT = 900  # ゲームウィンドウの高さ

class GameOver:
    # プレイヤーと敵が接触したら終わり（現時点は自己申告）
    def touch_enemy(screen):
        font = pg.font.SysFont("hgp創英角ﾎﾟｯﾌﾟ体", 80)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                txt = font.render("GameOver", True, (255, 255, 255))
                screen.blit(txt, [250, 250])
        pg.display.update()

    # 時間切れで終わり
    # 範囲外にキャラクターが出て終わり


def main():
    pg.display.set_caption("タイトル")
    screen = pg.display.set_mode((800,600))
    back = pg.image.load("ex05/haikei.png")
    screen.blit(back,[0,0])
    while True:
        GameOver.touch_enemy(screen)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
    

