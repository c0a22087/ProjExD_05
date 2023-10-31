import sys
# import time
import pygame as pg


WIDTH = 1600  # ゲームウィンドウの幅
HEIGHT = 900  # ゲームウィンドウの高さ






def main():
    pg.display.set_caption("タイトル")
    screen = pg.display.set_mode((800,600))
    back = pg.image.load("ex05/haikei.png")
    while True:
        screen.blit(back,[0,0])
        pg.display.update()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
    

