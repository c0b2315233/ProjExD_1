import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))        #サイズを(800,600)にする
    clock  = pg.time.Clock()                        
    bg_img = pg.image.load("fig/pg_bg.jpg")         #背景画像の選択

    kt_img = pg.image.load("fig/3.png")             #こうかとんの画像のロード
    kt_img =pg.transform.flip(kt_img,True,False)    #画像の反転

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return        

        screen.blit(bg_img, [0, 0])                 #背景の場所設定
        screen.blit(kt_img,[300,200])               #こうかとんの場所指定
        pg.display.update()                         #表示
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()