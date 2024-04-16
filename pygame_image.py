import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))        #サイズを(800,600)にする
    clock  = pg.time.Clock()                        
    bg_img = pg.image.load("fig/pg_bg.jpg")         #背景画像の選択
    bg_x = 0

    kt_img = pg.image.load("fig/3.png")             #こうかとんの画像のロード
    kt_img =pg.transform.flip(kt_img,True,False)    #画像の反転

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return        

        screen.blit(bg_img, [bg_x, 0])              #背景の場所設定
        screen.blit(kt_img,[300,200])               #こうかとんの場所指定
        pg.display.update()                         #表示
        print(bg_x)
        bg_x -= 1                                   #背景のX座標を1ずつ増加
        if(bg_x<=-1600):                             #背景のX座標が1600以上の場合
            bg_x=0                                  #背景のX座標をリセットする
        tmr += 1                                    
        clock.tick(200)                             #FPSを200に設定


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()