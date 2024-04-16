import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))        #サイズを(800,600)にする
    clock  = pg.time.Clock()                        
    bg_img = pg.image.load("fig/pg_bg.jpg")         #背景画像の選択
    bg_img2 = pg.transform.flip(bg_img,True,False)
    bg_x = 0

    kt_img = pg.image.load("fig/3.png")             #こうかとんの画像のロード
    kt_img = pg.transform.flip(kt_img,True,False)    #画像の反転
    kt_rct = kt_img.get_rect()                      #こうかとんのrectを設定
    kt_rct.center=300,200                           #中心点を初期位置に設定
    

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return        
        
        key_lst=pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            kt_rct.move_ip( 0, -1 )
        elif key_lst[pg.K_DOWN]:
            kt_rct.move_ip( 0, 1 )
        elif key_lst[pg.K_RIGHT]:
            kt_rct.move_ip( 1, 0 )
        elif key_lst[pg.K_LEFT]:
            kt_rct.move_ip( -1 , 0 )
        screen.blit(bg_img, [bg_x, 0])              #背景の場所設定
        screen.blit(bg_img2,[bg_x+1600,0])          #反転した背景の場所設定
        screen.blit(bg_img,[bg_x+3200,0])           #3枚目の背景の場所設定
        screen.blit(kt_img,kt_rct)                  #こうかとんの場所指定
        pg.display.update()                         #表示
        print(bg_x)
        bg_x -= 1                                   #背景のX座標を1ずつ増加
        if(bg_x<=-3200):                             #背景のX座標が1600以上の場合
            bg_x=0                                  #背景のX座標をリセットする
        tmr += 1                                    
        clock.tick(200)                             #FPSを200に設定


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()