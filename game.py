import sys
import time
import pygame as pg


WIDTH = 1800  #1800 ゲームウィンドウの幅
HEIGHT = 900  #900 ゲームウィンドウの高さ
earth = HEIGHT*3//4 #地面の高さ
square = 55 #ブロックの大きさ


class Stage:
    """
    ステージ作成を行う
    """
    def __init__(self,x,y,speed):
        """
        ブロックの大きさ変更
        引数x,yはブロックの初期位置を表す
        """
        self.image=pg.transform.rotozoom(pg.image.load("ex05/brock1.jpg"),0,0.08)
        self.rect=self.image.get_rect()
        self.rect.topleft=(square*x,earth+square*y)
        self.speed=speed

        # # ブロックの画像の大きさの確認用
        # self.image_width, self.image_height = self.image.get_size()
        # print(f"画像の幅: {self.image_width}, 画像の高さ: {self.image_height}")

    
    def update(self):
        self.rect.x-=self.speed

    def OffScreen(self):
        return self.rect.right<=0
    
    def get_top(self):
        return self.rect.top
            

    def draw(self,screen):
        screen.blit(self.image,self.rect.topleft)

class mario():
    """
    ゲームキャラクター（マリオ）に関するクラス
    """
    key_ls= {  # 押下キーと移動量の辞書
        pg.K_LEFT: (-7, 0),
        pg.K_RIGHT: (+7, 0),
        }

    def __init__(self):
        """
        マリオ画像Surfaceを生成する
        引数1 mro：マリオ画像ファイル名の番号
        引数2 xy：マリオ画像の位置座標タプル
        """
        self.mro = pg.image.load("ex05/fig/mario_4.png") #デフォルトのマリオ画像
        self.mro = pg.transform.rotozoom(self.mro, 0, 0.2)
        # self.mro1_2 = pg.transform.flip(self.mro, True, False) #左右反転
        # self.mro1_2_rct = self.mro1_2.get_rect()
        # self.mro1_2_rct.center =[100, earth]
        self.whidth,self.height=self.mro.get_size()
        self.gravity=2
        self.x=10*square
        self.y=earth-square*5
        self.velocity=0
        self.velocity_x=0
        self.jump_strength=-36
        self.on_ground=False
        self.on_head=False
        self.on_right=False
        self.on_left=False
        self.mro_rct = self.mro.get_rect()


    def move(self,speed):
        keys=pg.key.get_pressed()
        if self.on_ground==True:
            self.velocity=(-(self.gravity+3))
            if keys[pg.K_j]:
                self.velocity=self.jump_strength
        
        if self.on_head==True:
            self.velocity=5
        
        if self.on_left==True:
            if keys[pg.K_LEFT]:
                self.velocity_x=(self.key_ls[pg.K_LEFT][0])*-1
        if self.on_right==True:
            if keys[pg.K_RIGHT]:
                self.velocity_x=(self.key_ls[pg.K_RIGHT][0])*-1

        self.velocity+=self.gravity
        self.y+=self.velocity
        self.velocity_x-=speed
        self.x+=self.velocity_x
        self.mro_rct.x=self.x
        self.mro_rct.y=self.y
        self.velocity_x=0


    def update(self, screen: pg.Surface):
        """
        マリオの操作
        """
        screen.blit(self.mro,self.mro_rct)

#　ゴール機能
class Goal_m(pg.sprite.Sprite):

    """
    ゴールに関するクラス
    """


        # key_lst= {  # 押下キーと移動量の辞書
        # pg.K_j: (0, +1),
        # pg.K_LEFT: (-1, 0),
        # pg.K_RIGHT: (+1, 0),
        # }
        # j_u = 4
        # if self.key_ls[pg.K_j]: #jキーが押されたら
        #     # self.mro.change_img(self.mro2, screen)
        #     self.mro.move_ip((0, j_u)) #ジャンプするマリオ画像を上に4動かす
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

"""
HEAD
"""

        

class Tekimod:
    
    def __init__(self):
        #キラーの初期設定
        
        self.kira_img=pg.image.load("ex05/fig/kira1.1.png")
        self.kira_img=pg.transform.rotozoom(self.kira_img,0,0.2)
        self.kira_rct=self.kira_img.get_rect()
        self.kira_rct.center=[1600,400]
        self.kira_x=-5
        self.kira_y=0
        #ボム兵  self.image = tools.load_image("data", "rabipple.png", -1)

        self.bomu_img=pg.image.load("ex05/fig/bomu1.1.png")
        self.bomu_img=pg.transform.rotozoom(self.bomu_img,0,2)
        self.bomu_rct=self.bomu_img.get_rect()
        self.bomu_rct.center=[WIDTH,HEIGHT//2]
        self.bomu_x=-1
        self.bomu_y=+5

        #クリボー
        self.kuribo_img=pg.image.load("ex05/fig/kuribo1.1.png")
        self.kuribo_img=pg.transform.rotozoom(self.kuribo_img,0,2)
        self.kuribo_rct=self.kuribo_img.get_rect()
        self.kuribo_rct.center=[1500,600]
        self.kuribo_x=-3
        self.kuribo_y=1

        #パックン
        self.pakkun_img=pg.image.load("ex05/fig/pakkun1.1.png")
        self.pakkun_img=pg.transform.rotozoom(self.pakkun_img,0,2)
        self.pakkun_rct=self.pakkun_img.get_rect()
        self.pakkun_rct.center=[33*square+25,earth-square+20]
        self.pakkun_x=-1


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
        self.pakkun_rct.move_ip(self.pakkun_x,0)
        screen.blit(self.pakkun_img,self.pakkun_rct)
"""
敵mob
"""
def check_collision(mob,stage):
    hanntei=[]
    if mob.colliderect(stage):
        if mob.top<stage.top and mob.bottom>stage.top:
            hanntei.append(1)
        if mob.bottom > stage.bottom and mob.top < stage.bottom and mob.top>stage.center[1]:
            hanntei.append(2)
        if mob.topleft[0] < stage.right and mob.topright[0] > stage.right:
            hanntei.append(3)
        if mob.topright[0] > stage.left and mob.topleft[0] < stage.left:
            hanntei.append(4)

    return hanntei
        #super().__init__()
    

    def __init__(self):
                
        # ゴールを表示
            # screen = pg.display.set_mode((800, 900)) #画面の大きさ
            goal_img = pg.image.load("ex05/goal.png")
            goal2_img = pg.image.load("ex05/goal_txt.jpeg") #時間があったら
            self.goal_img = pg.transform.scale(goal_img, (250, 500)) #画像の大きさ
            # enn = pg.Surface((20, 20))

    def update(self,screen):
            screen.blit(self.goal_img, [500, 100])

        #キャラがゴールする
        


def main():
    pg.display.set_caption("タイトル")

    screen = pg.display.set_mode((WIDTH,HEIGHT))
    # back = pg.image.load("ex05/haikei.png")
    #back = pg.image.load("ex04/fig/pg_bg.jpg")
    # mrio = pg.sprite.Group()
    teki=Tekimod()
    ma=mario()
    clock = pg.time.Clock()

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


        

        # mrio.update(screen)
        # mo.update(screen)
        # pg.display.update()
        # screen.blit(back,[0,0])
        # clock.tick(50)

    # screen = pg.display.set_mode((WIDTH,HEIGHT))

    """
    良輔
    """
    clock=pg.time.Clock()

    pg.init()
    screen=pg.display.set_mode((WIDTH,HEIGHT))
    x=WIDTH
    y=earth
    #ブロックの初期位置
    positions=[
        #地面1番目
        (0,0),(1,0),(2,0),(3,0),(4,0),(5,0),
        (6,0),(7,0),(8,0),(9,0),(10,0),(11,0),
        (12,0),(13,0),(14,0),(15,0),(16,0),(17,0),
        (18,0),(19,0),(20,0),(21,0),(22,0),(23,0),
        (24,0),(25,0),(26,0),(27,0),(28,0),(29,0),
        (30,0),(31,0),(32,0),(33,0),(34,0),(35,0),
        (36,0),(37,0),(38,0),(39,0),(40,0),(41,0),
        (42,0),(43,0),(44,0),(45,0),(46,0),(47,0),
        #(48,0),(49,0),(50,0),(51,0),(52,0),(53,0),
        (54,0),(55,0),(56,0),(57,0),(58,0),(59,0),
        (60,0),(61,0),(62,0),(63,0),(64,0),(65,0),
        (66,0),(67,0),(68,0),(69,0),(70,0),(71,0),
        (72,0),(73,0),(74,0),(75,0),(76,0),(77,0),
        (78,0),(79,0),(80,0),(81,0),(82,0),(83,0),

        (97,0),(98,0),(99,0),(100,0),(101,0),(102,0),
        (103,0),(104,0),(105,0),(106,0),(107,0),(108,0),
        (109,0),(110,0),(111,0),(112,0),(113,0),(114,0),
        (115,0),(116,0),(117,0),(118,0),(119,0),(120,0),
        (121,0),(122,0),(123,0),(124,0),(125,0),(126,0),
        (127,0),(128,0),(129,0),(130,0),(131,0),(132,0),



        #地面2番目
        (0,+1),(1,+1),(2,+1),(3,+1),(4,+1),(5,+1),
        (6,+1),(7,+1),(8,+1),(9,+1),(10,+1),(11,+1),
        (12,+1),(13,+1),(14,+1),(15,+1),(16,+1),(17,+1),
        (18,+1),(19,+1),(20,+1),(21,+1),(22,+1),(23,+1),
        (24,+1),(25,+1),(26,+1),(27,+1),(28,+1),(29,+1),
        (30,+1),(31,+1),(32,+1),(33,+1),(34,+1),(35,+1),
        (36,+1),(37,+1),(38,+1),(39,+1),(40,+1),(41,+1),
        (42,+1),(43,+1),(44,+1),(45,+1),(46,+1),(47,+1),
        #(48,+1),(49,+1),(50,+1),(51,+1),(52,+1),(53,+1),
        (54,+1),(55,+1),(56,+1),(57,+1),(58,+1),(59,+1),
        (60,+1),(61,+1),(62,+1),(63,+1),(64,+1),(65,+1),
        (66,+1),(67,+1),(68,+1),(69,+1),(70,+1),(71,+1),
        (72,+1),(73,+1),(74,+1),(75,+1),(76,+1),(77,+1),
        (78,+1),(79,+1),(80,+1),(81,+1),(82,+1),(83,+1),

        (97,+1),(98,+1),(99,+1),(100,+1),(101,+1),(102,+1),
        (103,+1),(104,+1),(105,+1),(106,+1),(107,+1),(108,+1),
        (109,+1),(110,+1),(111,+1),(112,+1),(113,+1),(114,+1),
        (115,+1),(116,+1),(117,+1),(118,+1),(119,+1),(120,+1),
        (121,+1),(122,+1),(123,+1),(124,+1),(125,+1),(126,+1),
        (127,+1),(128,+1),(129,+1),(130,+1),(131,+1),(132,+1),


        #地面3番目
        (0,+2),(1,+2),(2,+2),(3,+2),(4,+2),(5,+2),
        (6,+2),(7,+2),(8,+2),(9,+2),(10,+2),(11,+2),
        (12,+2),(13,+2),(14,+2),(15,+2),(16,+2),(17,+2),
        (18,+2),(19,+2),(20,+2),(21,+2),(22,+2),(23,+2),
        (24,+2),(25,+2),(26,+2),(27,+2),(28,+2),(29,+2),
        (30,+2),(31,+2),(32,+2),(33,+2),(34,+2),(35,+2),
        (36,+2),(37,+2),(38,+2),(39,+2),(40,+2),(41,+2),
        (42,+2),(43,+2),(44,+2),(45,+2),(46,+2),(47,+2),
        #(48,+2),(49,+2),(50,+2),(51,+2),(52,+2),(53,+2),
        (54,+2),(55,+2),(56,+2),(57,+2),(58,+2),(59,+2),
        (60,+2),(61,+2),(62,+2),(63,+2),(64,+2),(65,+2),
        (66,+2),(67,+2),(68,+2),(69,+2),(70,+2),(71,+2),
        (72,+2),(73,+2),(74,+2),(75,+2),(76,+2),(77,+2),
        (78,+2),(79,+2),(80,+2),(81,+2),(82,+2),(83,+2),

        (97,+2),(98,+2),(99,+2),(100,+2),(101,+2),(102,+2),
        (103,+2),(104,+2),(105,+2),(106,+2),(107,+2),(108,+2),
        (109,+2),(110,+2),(111,+2),(112,+2),(113,+2),(114,+2),
        (115,+2),(116,+2),(117,+2),(118,+2),(119,+2),(120,+2),
        (121,+2),(122,+2),(123,+2),(124,+2),(125,+2),(126,+2),
        (127,+2),(128,+2),(129,+2),(130,+2),(131,+2),(132,+2),

        #地面
        (0,+3),(1,+3),(2,+3),(3,+3),(4,+3),(5,+3),
        (6,+3),(7,+3),(8,+3),(9,+3),(10,+3),(11,+3),
        (12,+3),(13,+3),(14,+3),(15,+3),(16,+3),(17,+3),
        (18,+3),(19,+3),(20,+3),(21,+3),(22,+3),(23,+3),
        (24,+3),(25,+3),(26,+3),(27,+3),(28,+3),(29,+3),
        (30,+3),(31,+3),(32,+3),(33,+3),(34,+3),(35,+3),
        (36,+3),(37,+3),(38,+3),(39,+3),(40,+3),(41,+3),
        (42,+3),(43,+3),(44,+3),(45,+3),(46,+3),(47,+3),
        #(48,+3),(49,+3),(50,+3),(51,+3),(52,+3),(53,+3),
        (54,+3),(55,+3),(56,+3),(57,+3),(58,+3),(59,+3),
        (60,+3),(61,+3),(62,+3),(63,+3),(64,+3),(65,+3),
        (66,+3),(67,+3),(68,+3),(69,+3),(70,+3),(71,+3),
        (72,+3),(73,+3),(74,+3),(75,+3),(76,+3),(77,+3),
        (78,+3),(79,+3),(80,+3),(81,+3),(82,+3),(83,+3),

        (97,+3),(98,+3),(99,+3),(100,+3),(101,+3),(102,+3),
        (103,+3),(104,+3),(105,+3),(106,+3),(107,+3),(108,+3),
        (109,+3),(110,+3),(111,+3),(112,+3),(113,+3),(114,+3),
        (115,+3),(116,+3),(117,+3),(118,+3),(119,+3),(120,+3),
        (121,+3),(122,+3),(123,+3),(124,+3),(125,+3),(126,+3),
        (127,+3),(128,+3),(129,+3),(130,+3),(131,+3),(132,+3),
        #その他
        
                                (20,-4),
                                (21,-4),
                                (22,-4),
        
        (30,-1),
        (31,-1),(31,-2),
        (32,-1),(32,-2),(32,-3),

        (34,-1),(34,-2),(34,-3),
        (35,-1),(35,-2),
        (36,-1),
        
                                    (38,-5),
                                    (39,-5),
                                    
                                            (42,-6),
                                            (43,-6),

                                            (49,-6),
                                            (50,-6),
                                            (51,-6),

        (58,-1),(58,-2),(58,-3),(58,-4),
        (59,-1),(59,-2),(59,-3),(59,-4),
        (60,-1),
        (61,-1),
        (62,-1),
        (63,-1),(63,-2),(63,-3),(63,-4),
        (64,-1),(64,-2),(64,-3),(64,-4),
        (65,-1),
        (66,-1),
        
        
                                (69,-4),
        
        
                                        (72,-5),
        
        
                                                (75,-6),
        
        
        
                                        (79,-5),(79,-6),
        (80,-1),(80,-2),(80,-3),(80,-4),(80,-5),(80,-6),
        (81,-1),(81,-2),(81,-3),(81,-4),(81,-5),(81,-6),
        (82,-1),(82,-2),(82,-3),(82,-4),(82,-5),(82,-6),
        (83,-1),(83,-2),(83,-3),(83,-4),(83,-5),(83,-6),
        (84,-1),
        


        (88,-1),
        (89,-1),




        (97,-1),
        (98,-1),
        



        (103,-1),
        (104,-1),(104,-2),
        (105,-1),(105,-2),(105,-3),
        (106,-1),(106,-2),(106,-3),(106,-4),
        (107,-1),(107,-2),(107,-3),(107,-4),(107,-5),
        (108,-1),(108,-2),(108,-3),(108,-4),(108,-5),(108,-6),
        (109,-1),(109,-2),(109,-3),(109,-4),(109,-5),(109,-6),(109,-7),
        (110,-1),(110,-2),(110,-3),(110,-4),(110,-5),(110,-6),(110,-7),(110,-8)
    ]

    speed=1
    scrollers=[]
    for i in range(len(positions)):
        x,y=positions[i]
        scroller=Stage(x,y,speed)
        scrollers.append(scroller)


    start_time=pg.time.get_ticks()

    while True:
    # for i in range(1000):
        for event in pg.event.get():
            if event.type==pg.KEYDOWN and event.key==pg.K_SPACE:
                return
        screen.fill((0,0,255))#背景仮

        # screen.blit(mo.mro,(100,100))
        now_time=pg.time.get_ticks()
        
        # print(now_time) #時間確認用
        if now_time-start_time>=95000:
            for scroller in scrollers:
                scroller.speed=0
        

        for scroller in scrollers:
            scroller.update()

        #画面外の時オブジェクト削除
        scrollers=[scroller for scroller in scrollers if not scroller.OffScreen()]

        teki.bomu_y=+5
        teki.kuribo_y=+5

        ma.on_ground=False
        ma.on_head=False
        ma.on_left=False
        ma.on_right=False
        for i in range(len(scrollers)):
            if 1 in check_collision(teki.bomu_rct,scrollers[i].rect):
                teki.bomu_y=0
                teki.bomu_x=-2
            if 1 in check_collision(teki.kuribo_rct,scrollers[i].rect):
                teki.kuribo_y=0
                teki.kuribo_x=-2
            if 1 in check_collision(ma.mro_rct,scrollers[i].rect):
                ma.on_ground=True
            if 2 in check_collision(ma.mro_rct,scrollers[i].rect):
                ma.on_head=True
            if 3 in check_collision(ma.mro_rct,scrollers[i].rect):
                ma.on_left=True
            if 4 in check_collision(ma.mro_rct,scrollers[i].rect):
                ma.on_right=True

        key_lst = pg.key.get_pressed()
        for key, mv in ma.key_ls.items():
            if key_lst[key]:
                ma.x += mv[0]
        # print(mro_mv)
            # if check_collision(teki.bomu_rct,scrollers[i].rect)==2:
            #     teki.bomu_x*=-1
            #     teki.bomu_y=teki.bomu_y
            # if check_collision(teki.kuribo_rct,scrollers[i].rect)==2:
            #     teki.kuribo_x*=-1
            #     teki.kuribo_y=teki.kuribo_y

        #teki=Tekimod()
        ma.move(speed)

        for scroller in scrollers:
            scroller.draw(screen)
        
        ma.update(screen)
        teki.update(screen)#敵mobを追加
        pg.display.flip()
        clock.tick(60)
        # clock.tick(1000)


    # 敵mob

    # tmr=0
    # clock=pg.time.Clock()

    # back = pg.image.load("ex05/fig/pg_bg.jpg")
   
        # for event in pg.event.get():
        #     if event.type == pg.QUIT: 
        #         return
       
        
        #teki.update(screen)#敵mobを追加
        
        
    
        
        pg.display.update()
       
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
