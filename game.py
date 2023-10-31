import sys
from typing import Any
import time
import pygame as pg
from pygame.sprite import AbstractGroup


WIDTH = 1000  #1800 ゲームウィンドウの幅
HEIGHT = 500  #900 ゲームウィンドウの高さ

class Stage:
    """
    ステージ作成を行う
    """
    def __init__(self,x,y):
        """
        ブロックの大きさ変更
        引数x,yはブロックの初期位置を表す
        """
        self.image=pg.transform.rotozoom(pg.image.load("ex05/brock.jpg"),0,0.1)
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.speed=2

        #ブロックの画像の大きさの確認用
        self.image_width, self.image_height = self.image.get_size()
        print(f"画像の幅: {self.image_width}, 画像の高さ: {self.image_height}")

    
    def update(self):
        self.rect.x-=self.speed
        if self.rect.right<=0:
            self.rect.x=WIDTH

    def draw(self,screen):
        screen.blit(self.image,self.rect.topleft)
        




def main():
    pg.display.set_caption("タイトル")
    screen = pg.display.set_mode((WIDTH,HEIGHT))

    """
    良輔
    """
    clock=pg.time.Clock()

    pg.init()
    screen=pg.display.set_mode((WIDTH,HEIGHT))
    x=WIDTH
    y=HEIGHT*3//4
    #ブロックの初期位置
    positions=[
        (0,HEIGHT*3//4),
        (70,HEIGHT*3//4)
    ]
    
    scrollers=[]
    for i in range(len(positions)):
        x,y=positions[i]
        scroller=Stage(x,y)
        scrollers.append(scroller)

    # while True:
    for i in range(1000):
        pg.display.update()
        scroller.update()
        screen.fill((0,0,255))

        scroller.draw(screen)

        pg.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
    

