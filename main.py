import sys
import random
import pygame as pg

WITDH = 1600
HEIGHT = 900


class Enemy(pg.sprite.Sprite):
    """
    道中の障害物(サカバンバスピス)に関するクラス
    """

    def __init__(self):
        super().__init__()
        self.image = pg.transform.rotozoom(pg.image.load("ex05/images/ojama.png"), 0, 0.5)   # 障害物の画像読み込み
        self.rect = self.image.get_rect()
        self.rect.center = WITDH / 4 * 3, HEIGHT / 4
        self.vy = +50
        self.ay = +3
        self.vx = 0


    def update(self):
        """
        お魚が地面ではねるところ
        地面の座標(マージ前は750と仮定)に到達するまで等加速し、地面で速度を反転

        """
        if self.rect.centery >= 750:
            self.vy = -60
            self.vx = random.randint(-5, 5) * 5#
        self.vy += self.ay
        #self.rect.centerx = Character.calc_mv()   スクロールに合わせたx座標の移動(マージ後に調整)
        if (self.rect.left < 0) or (self.rect.right > WITDH):#
            self.vx *= -1#
        self.rect.centerx += self.vx#
        self.rect.centery += self.vy
        




def main():
    pg.display.set_caption("学長が転んだ")
    screen = pg.display.set_mode((WITDH, HEIGHT))
    bg_image = pg.transform.rotozoom(pg.image.load("ex05/images/sky_img.png"), 0, 1.35)

    emys = pg.sprite.Group()
        emys.add(Enemy())

    tmr = 0
    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_image, [0, 0])
        
           
        emys.update()
        emys.draw(screen)
        pg.display.update()
        tmr += 1
        clock.tick(50)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
