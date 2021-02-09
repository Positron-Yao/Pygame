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
    background_1 = pygame.transform.smoothscale(Tools.load_png('background_1.png')[0], screen_size)
    background_1_alpha = 10
    background_1.set_alpha(background_1_alpha)

    #文本
    text_1 = pygame.font.Font("data\\沐瑶软笔手写体(Muyao-Softbrush).ttf", 64).render("车  万  憨  批  传", 1, (10, 10, 10))
    text_2 = pygame.font.Font("data\\沐瑶软笔手写体(Muyao-Softbrush).ttf", 32).render("(点击屏幕开始游戏)", 1, (10, 10, 10))

    #break
    break_1 = False

    #----------Stage_1----------
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
                print(1)

        #检测是否退出
        if break_1:
            break

        #::::时间轴::::
        #--background alpha:
        if background_1_alpha < 255:
            background_1_alpha += 1
            background_1.set_alpha( background_1_alpha )

        #System
        screen.blit(background_1, (0, 0))
        screen.blit(text_1, (100, 50))
        screen.blit(text_2, (180, 150))
        pygame.display.update()

        print(init_clock.get_fps())
        init_clock.tick_busy_loop(60)


    print("Thank you!")

if __name__ == '__main__':
    main()