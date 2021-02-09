# _*_coding:utf-8_*_

#加载模块
try:
    from pyhelper import *
except ImportError as err:
    print("无法加载模块... %s" % err)
    exit()

def main():
    #初始化
    pygame.init()
    init_clock = pygame.time.Clock()
    screen_size = (720, 405)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Test")

    #背景
    background = pygame.transform.smoothscale(Tools.load_png('background_1.jpg')[0], screen_size)

    #文本
    font_big = pygame.font.Font("data\\沐瑶软笔手写体(Muyao-Softbrush).ttf", 52)
    font_small = pygame.font.Font("data\\沐瑶软笔手写体(Muyao-Softbrush).ttf", 32)
    text_1 = font_big.render("车  万  憨  批  传", 1, (10, 10, 10))
    text_2 = font_small.render("(点击屏幕开始游戏)", 1, (10, 10, 10))
    textpos = text_1.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos = textpos.move(0, 50)
    background.blit(text_1, textpos)
    textpos.centerx = background.get_rect().centerx
    textpos = textpos.move(20, 100)
    background.blit(text_2, textpos)

    #blit
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #break
    break_1 = False

    #Stage_1： 
    while True:
        #event
        for event in pygame.event.get():
            if event.type == QUIT:    #退出
                exit()
            elif event.type == KEYDOWN:
                if event.key == 27:
                    exit()
            elif event.type == MOUSEBUTTONDOWN:
                print(0)
                break_1 = True
                print(2)

        #检测是否退出
        if break_1:
            break

        #System
        screen.blit(background, (0, 0))
        pygame.display.flip()
        init_clock.tick_busy_loop(60)


    print("Thank you!")

if __name__ == '__main__':
    main()