#项目开始
#引入的包/库
import json

import pygame
from pygame.locals import *
import linecache
import random
import time
import math
import sys
import os
import string


class theme(pygame.sprite.Sprite):

    def __init__(self, c, d, speed=5, height=20):
        pygame.sprite.Sprite.__init__(self)
        # 4/13 12：50 state：基本完成   plan 完善
        # self.image = pygame.Surface((c, d))
        font1 = pygame.font.Font("font/simhei.ttf", 20).render("print(hello world)", False, black, blue)
        font2 = pygame.font.Font("font/simhei.ttf", 20).render("while 循环条件:", False, black, red)
        font3 = pygame.font.Font("font/simhei.ttf", 20).render("if 判断条件: ", False, black, yellow)
        font4 = pygame.font.Font("font/simhei.ttf", 20).render("a, b = b, a + b: ", False, black, green)
        font5 = pygame.font.Font("font/simhei.ttf", 20).render("input('请输入')", False, black, pink)
        list1 = [font1, font2, font3, font4, font5]
        self.image = random.choice(list1)

        # self.image.fill(black)
        # self.image = pygame.transform.rotate(self.image, 45)
        self.rect = self.image.get_rect()
        self.rect.x = screen_w
        self.rect.bottom = screen_h
        self.speed = speed
        self.height = height

    def update(self, *args):
        self.rect.centerx -= 2
        # print(self.rect.centerx)


class player(pygame.sprite.Sprite):
    # rect1 = 1
    # global state
    def __init__(self):
        # global rect1
        super().__init__()
        # self.playerSpeed = speed
        # pass
        self.image = game3_hero_img
        # self.image = pygame.Surface((10, 10))
        # pygame.draw.circle()
        # pygame.draw.circle(self.image, (255, 255, 0), (5, 5), 5)
        self.rect = self.image.get_rect()

        # self.rect.x = i
        # if
        self.rect.bottom = screen_h

        # return self.rect

    def update(self, speed1, jumpSpeed=2, jumpHeight=80):
        self.rect.x += speed1
        print("speed1", speed1)
        global state
        if state == "jump":

            self.rect.bottom -= 2
        if self.rect.bottom == screen_h-jumpHeight:
            state = "down"
        if state == "down" and state != "stop":
            self.rect.bottom += 2
        if self.rect.bottom == screen_h:
            state = "stop"
        print(self.rect)
        surface.blit(self.image, self.rect)
        # print(self.rect)

#功能：传入一个rect和一个功能函数名，使点击这个rect时可以用这个功能
def button(click_rect, value):
    global game3_jump_state
    global game_pass_state
    global index_view_state
    global game1_difficulty_level
    global game2_difficulty_level
    global game3_difficulty_level
    global restart_state
    global choose_close_state
    global game1_Taying_Training_state
    global game2_find_mother_state
    global make_big_state
    global difficulty_level_size1
    global difficulty_level_size2
    global difficulty_level_size3

    global difficulty_level_size
    global read_key_state
    global game4_eat_star_state
    global start_time1
    global music_state
    global state111
    if event.type == MOUSEBUTTONDOWN:

        if event.button == 1 and pygame.mouse.get_pos()[0] >= click_rect.x and pygame.mouse.get_pos()[0] <= click_rect.right and pygame.mouse.get_pos()[1] >= click_rect.y and pygame.mouse.get_pos()[1] <= click_rect.bottom :
            if value == choose_close:
                choose_close_state = 1
                index_view_state = 0
            if value == game1_Taying_Training:
                restart_state = 0
                start_time1 = None
                game1_Taying_Training_state = 1
                read_key_state = 1
                choose_close_state = 0
            if value == game2_find_mother:
                game1_Taying_Training_state = 0
                read_key_state = 0
                game2_find_mother_state = 1
                choose_close_state = 0
            if value == game3_jump:
                game3_jump_state = 1
                game2_find_mother_state = 0
                choose_close_state = 0
            if value == game4_eat_star:
                game4_eat_star_state = 1
                game3_jump_state = 0
                choose_close_state = 0
            if value == a:
                music_state = -1
            if value == make_big and click_rect == index_a:
                difficulty_level_size1 = 50

            if value == make_big and click_rect == index_b:
                difficulty_level_size2 = 50
                game1_difficulty_level = 40
                game2_difficulty_level = 3
                game3_difficulty_level = 30
            if value == make_big and click_rect == index_c:
                difficulty_level_size3 = 50
                game1_difficulty_level = 20
                game2_difficulty_level = 5
                game3_difficulty_level = 50



            game_pass_state = 0
    return value
# 使一个对象可以被拖拽
def drag(obj1, start_rect):
    global drag_state
    global drag_pos
    # global start_rect
    if event.type == MOUSEBUTTONDOWN and event.button == 1 and pygame.mouse.get_pos()[0] >= start_rect.x and pygame.mouse.get_pos()[0] <= start_rect.right and pygame.mouse.get_pos()[1] >= start_rect.y and pygame.mouse.get_pos()[1] <= start_rect.bottom:

        drag_state = 1
    if event.type == MOUSEBUTTONUP and event.button == 1:
        drag_state = 0
    if drag_state == 1:
        start_rect.x = pygame.mouse.get_pos()[0]
        start_rect.y = pygame.mouse.get_pos()[1]
        drag_pos = pygame.mouse.get_pos()
    if drag_state == 0 and drag_pos != None:
        start_rect.x = drag_pos[0]
        start_rect.y = drag_pos[1]

    # print(pygame.mouse.get_rel(), "移动")
    # print(start_rect, "开始rect")
    surface.blit(obj1, start_rect)
    # print(start_rect)

    # return start_rect

# 得到一个文本的rect和font
def get_text_rectandfont(text2, size2, color, rect2, background=None):
    global text_font_rect
    text_font1 = pygame.font.Font("font/simhei.ttf", size2)
    text_font = text_font1.render(text2, False, color, background)
    text_font_rect = text_font.get_rect()
    text_font_rect.centerx = rect2.centerx
    text_font_rect.centery = rect2.centery
    surface.blit(text_font, text_font_rect)
    return text_font_rect,  text_font

# 时间计数器
def timer(start_time):
    global time1
    end_time = time.time()
    time1 = end_time - start_time
    return math.ceil(time1)

def game_pass():
    global game_pass_state
    if game_pass_state == 1:
        pass_img = pygame.image.load("img/pass.jpg")
        surface.blit(pass_img, (0, 0))
        # text("通过", [screen_w // 2 - 50, 0], 100, False, blue)
        next = text("下一章", [screen_w - 200, screen_h - 200], 50, False, green)
        return next
def game_restart():
    if restart_state == 1:
        restart_img = pygame.image.load('img/restart.png')
        surface.blit(restart_img, (0, 0))
# 提示
def hint(hint1):
    hint_img = pygame.image.load("img/hint.png")
    # hint_img.fill(0, 0, 0)
    hint_rect = hint_img.get_rect()
    hint_rect.right = screen_w
    hint_font = pygame.font.Font("font/simhei.ttf", 20).render(hint1, False, (255, 0, 0))
    hint_font_rect = hint_font.get_rect()
    hint_font_rect.centerx = hint_rect.centerx
    hint_font_rect.centery = hint_rect.centery

    surface.blit(hint_img, hint_rect)
    surface.blit(hint_font, hint_font_rect)

def text(text1, pos1, size1, ifunderline=False, color=(0, 0, 0), background=None, if_drag_sign=None):
    global sign1
    text_font1 = pygame.font.Font("font/simhei.ttf", size1)
    text_font1.set_underline(ifunderline)
    text_font = text_font1.render(text1, False, color, background)
    text_font_rect = text_font.get_rect()
    # if sign1 == 1:
    text_font_rect.x = pos1[0]
    text_font_rect.y = pos1[1]
    surface.blit(text_font, text_font_rect)
        # sign1 = 0

    # drag(text_font, text_font_rect)


    # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa4/2 16:28
    if if_drag_sign == None:
        return text_font_rect
    if if_drag_sign == True:
        return text_font, text_font_rect


def make_big():
    pass

def index_view():
    global music_state
    global index_a
    global index_b
    global index_c
    if index_view_state == 1:

        begin_image = pygame.image.load("img/blackboard.jpg")
        begin_image1 = pygame.transform.scale(begin_image, (screen_w, screen_h))
        begin_image_rect = begin_image1.get_rect()
        surface.blit(begin_image1, begin_image_rect)
        font1 = pygame.font.Font("font/simhei.ttf", 50)
        begin_font = font1.render("让我们开始编程之旅吧！", False, (0, 0, 0))
        text("请选择关卡难度：", (0, 0), 30)
        # dddddddddddddddddddddddddddddddddddddd4/26
        index_a = text("简单", (250, 0), difficulty_level_size1, False, green)
        button(index_a, make_big)()
        index_b = text("一般", (380, 0), difficulty_level_size2, False, blue)
        button(index_b, make_big)()
        index_c = text("复杂", (510, 0), difficulty_level_size3, False, red)
        button(index_c, make_big)()

        text("当前最快通过全部关卡的时间为：{}".format(fastest_time), (0, 60), 20)
        text_font_rect = text("G0", [screen_w // 4, screen_h - 250], 100, False, (0, 0, 0))

        if music_state == 0:
            surface.blit(open_voice_img, (screen_w-50, 0))
        else:
            surface.blit(close_voice_img, (screen_w-50, 0))

        button(pygame.Rect(screen_w-50, 0, 50, 50), a)
        button(text_font_rect, choose_close)
        begin_font_rect = begin_font.get_rect()
        begin_font_rect.centerx = screen_w//2
        begin_font_rect.centery = screen_h//2
        surface.blit(begin_font, begin_font_rect)

def choose_close():
    global index_view_state

    if choose_close_state == 1:
        # surface.blit(choose_back_img, (0, 0))
        x = 0
        for i in range(3):
            for j in range(5):

                try:
                    if game_lock_state_list[x] == 0:
                        surface.fill(red, pygame.Rect(j*screen_w//5, i*screen_h//3, screen_w//5, screen_h//3))
                        text("未通过", (j*screen_w//5, i*screen_h//3), 20)
                    else:

                        surface.fill(blue, pygame.Rect(j*screen_w//5, i*screen_h//3, screen_w//5, screen_h//3))
                        text("已通过", (j*screen_w//5, i*screen_h//3), 20)
                    x += 1
                except IndexError as error:
                    pass
        for i in range(4):
            pygame.draw.line(surface, black, ((i+1)*screen_w//5, 0), ((i+1)*(screen_w//5), screen_h))
        for j in range(3):
            pygame.draw.line(surface, black, (0, j * (screen_h // 3)), (screen_w, j * screen_h // 3))
        get_text_rectandfont("打字练习", 30, black, pygame.Rect(0, 0, screen_w//5, screen_h//3))
        get_text_rectandfont("数据类型练习", 30, black, pygame.Rect(screen_w//5, 0, screen_w//5, screen_h//3))
        get_text_rectandfont("python基本语法", 30, black, pygame.Rect(screen_w//5*2, 0, screen_w//5, screen_h//3))
        get_text_rectandfont("编程实战", 30, black, pygame.Rect(screen_w//5*3, 0, screen_w//5, screen_h//3))
        get_text_rectandfont("敬请期待", 30, black, pygame.Rect(screen_w//5*4, 0, screen_w//5, screen_h//3))




def read_key(ifunderline=False, color=(0, 0, 0)):
    global input_word
    global font1
    global index_view_state
    global read_key_state

    global rect1

    if read_key_state == 1:

        if event.type == KEYDOWN:

            input1 = event.unicode

            input_word += input1
            if event.key == 8:
                input_word = input_word[:-2]
        if event.type == QUIT:
            pygame.quit()
            sys.exit(2)
        font2 = pygame.font.Font("font/arial.ttf", 30)
        font2.set_underline(ifunderline)
        font1 = font2.render(input_word, False, (0, 0, 255))
        rect1 = font1.get_rect()
        rect1.y = 180
        rect1.x = 30

    return font1, rect1




def game1_Taying_Training():

    global start_time1
    global str1
    global index_view_state
    global game1_Taying_Training_state
    global game_lock_state_list
    global choose_close_state
    global read_key_state
    global e, f
    global game_pass_state
    global restart_state
    global input_word
    if game1_Taying_Training_state == 1:

        choose_close_state = 0
        read_key_state = 1
        index_view_state = 0



        #打字小游戏主代码
        if str1 == "":
            english_txt = open("admin/english.txt", "r")
            count = len(english_txt.readlines())
            word = linecache.getline(r"admin/english.txt", random.randint(1, count))
            str1 = word.splitlines()[0]

        # 4/27dddddddddddddddddddddddddddddddddddddddddddddddd
        text(str1, [30, 160], 20, False)
        text("编程先从学会打字开始，请在{}秒内打完下面的一段话".format(game1_difficulty_level), [30, 130], 30, False, red, None, True)


        if start_time1 == None:
            start_time1 = time.time()
        text(str(timer(start_time1)), [screen_w//2, 55], 50, False, red)
        if game1_difficulty_level >= timer(start_time1) and str1 == input_word:
            game_lock_state_list[0] = 1
            surface.fill(white)
            game_pass_state = 1
            button(game_pass(), game2_find_mother)()
        if timer(start_time1) > 60:
            game1_Taying_Training_state = 0
            # print(1111111111111)
            restart_state = 1
            input_word = ''
            # game_restart()


def game2_find_mother():
    global game_lock_state_list
    global random_child
    global state_find_mother
    global score
    global direct
    global dist
    global color_pos
    global game1_Taying_Training_state
    global child_text
    global child_dist
    global game_pass_state
    if game2_find_mother_state == 1:
        state_find_mother = 1

        if event.type == QUIT:
            try:
                sys.exit(1)
            except SystemExit as error:
                with open("admin/record.txt", "w") as fh:
                    print(str(game_lock_state_list), "end")
                    fh.write(str(game_lock_state_list))

            finally:
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                direct = "right"
            if event.key == K_LEFT:
                direct = "left"
            if event.key == K_UP:
                direct = "up"
            if event.key == K_DOWN:
                direct = "down"
        if event.type == KEYUP:
            direct = "stop"
        if direct == "right" and direct != "stop":
            child_dist[0] += 10
        if direct == "left" and direct != "stop":
            child_dist[0] -= 10
        if direct == "up" and direct != "stop":
            child_dist[1] -= 10
        if direct == "down" and direct != "stop":
            child_dist[1] += 10

        mother_text = []
        game2_img = pygame.image.load("img/game2.jpg")
        surface.blit(game2_img, (0, 0))
        text("找妈妈游戏：找到正确的数据类型,得到{}分通过".format(game2_difficulty_level), [0, 0], 30)
        mother = ["<class 'list'>", "<class 'int'>", "<class 'dict'>", "<class 'tuple'>", "<class 'str'>", "<class 'set'>", "<class 'float'>", "<class 'bool'>", "<class 'complex'>", "<class 'type'>", "<class 'NoneType'>"]
        section_mother = []
        for i in range(len(mother)):

            mother_text.append(text(mother[i][8: -2], globals()["mother1_dist" + str(i)], 30, False, black, color_mother[i]))

        index1 = mother.index(str(type(random_child)))
        print(index1, "索引1")
        if random_child == class_child:
            sign = random_child()
        else:
            sign = random_child
        if_collide = text(str(sign), child_dist, 20, False, black, red).collidelist(mother_text)
        print(if_collide, "索引2")
        score_text = "分数：" + str(score)
        text(score_text, [screen_w-200, 0], 40, False, red)

        if if_collide == index1 and direct not in ["", "stop"]:

            score += 1

            direct = ""
            time.sleep(2)
        if if_collide != -1:
            state_find_mother = 0
        if if_collide != index1 and if_collide != -1 and direct not in ["", "stop"]:

            score -= 1


            state_find_mother = 0
            direct = ""
            time.sleep(2)


        if score == game2_difficulty_level:
            surface.fill(white)
            game_lock_state_list[1] = 1
            game_pass_state = 1
            rect2 = game_pass()
            button(rect2, game3_jump)()
def game3_drag():
    pass
def read_terminal():
    global terminal_input
    while terminal_input[-7:-2] != "run()":
        if terminal_input == '':
            terminal_input += input("请在下方输入代码:\n") + "/n"
        else:
            terminal_input += input() + "/n"
        return terminal_input
def game3_jump():
    global game_lock_state_list
    global game3_jump_state
    global state
    if game3_jump_state == 1:
        global direction
        global t
        global tick
        global game_pass_state
        global game3_a
        # print("dddddddddddddddddddddddddddddddd")

        surface.blit(game3_img, (0, 0))
        # surface.fill((195, 195, 195))
        if event.type == KEYDOWN:
            print("keydown")

            if event.key == K_RIGHT and jumpSpeed == 0:
                direction = "right"
            if event.key == K_LEFT and jumpSpeed == 0:
                direction = "left"
            if event.key == K_UP and state == "stop":
                state = "jump"

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                direction = "stop"
            if event.key == K_LEFT:
                direction = "stop"
        #     判断是否点击了重新开始
        # print(direction)
        # print(state, "state")
        if direction == "right" and state == "stop":
            game3_a = 2
        if direction == "left" and state == "stop":
            game3_a = -2
            # if direction == "stop"开启飞天挂
        if direction == "stop" or state != "stop":
            game3_a = 0
        if tick % 360 == 0:
            groups1.add(theme(random.randint(5, 30), random.randint(5, 40)))
        if tick % 60 == 0 and t != game3_difficulty_level:
            t += 1
        groups1.draw(surface)
        groups1.update()
        # print(game3_a, "game3_a")
        player.update(game3_a, jumpSpeed, 200)
        tick += 1
        if pygame.sprite.spritecollide(player, groups1, True) != []:
            # surface.fill(red)
            time.sleep(2)
            t = 0
            # restart()
        text("跳跃游戏：跳过生成的语法块，在玩游戏的过程学习python特有常用语法", (0, 0), 30, False, white)
        # text("学习就是一个闯关的过程，只有坚持才能胜利", (0, 50), 30, False, blue)
        timeSurface = pygame.font.Font("font/simhei.ttf", 50).render("坚持{}秒过关，已经坚持了{}秒".format(game3_difficulty_level, t), False, white)
        timeRect = timeSurface.get_rect()
        timeRect.centerx = 500
        timeRect.centery = 200
        # print(timeRect, "aaaaaaaaaaaaaaaaaaaaa")
        surface.blit(timeSurface, timeRect)
        if t == game3_difficulty_level:
            # t = 0
            # t = 20
            # game3_jump_state = 0
            surface.fill(white)
            game_lock_state_list[2] = 1
            game_pass_state = 1
            game_pass()
            button(game_pass(), game4_eat_star)()
def game4_eat_star():
    global game_lock_state_list
    global game4_eat_star_state
    global rect_game4
    global terminal_input
    global pass_time_time
    global game_pass_state
    global pass_time
    global game4_score
    if game4_eat_star_state == 1:

        global input_direct


        rect2 = pygame.Rect(screen_w-50, 0, 50, 50)

        if game4_score != 1:
            surface.fill(white)
            print(11111111111111111111111111111111111)
            surface.blit(game4_img, (0, 0))
            print(2222222222222222222222222222222222222)
            pygame.draw.rect(surface, pink, rect_game4)
            pygame.draw.rect(surface, pink, rect2)

            text("第四章：代码实战游戏", (100, 100), 30, False, white)
            text("提示：在终端中输入代码，控制player找到相同种类的形状和颜色", (100, 200), 20, False, white)
            text("player代表玩家对象", (100, 300), 20, False, white)
            text("up(),down(),left(),right()代表移动方法", (100, 320), 20, False, white)
            text("run()代表执行代码", (100, 340), 20, False, white)
            text("请利用python循环判断语句来组合代码，并执行来控制player找到同类吧！！", (100, 370), 20, False, white)

            pygame.display.flip()
        # print("222222222222222222")
        while input_direct == '':
            if input_direct == '':
                str1 = read_terminal()
                print("str1:", str1)
                try:
                    str1 = str1[:-7]
                    list1 = str1.split("/n")
                    print(str1)
                    if list1[0] == "while True:" and list1[1] == r"    player.right()":
                        input_direct = "right"
                    if list1[0] == "while True:" and list1[1] == r"    player.left()":
                        input_direct = "left"
                    if list1[0] == "while True:" and list1[1] == r"    player.up()":
                        input_direct = "up"
                    if list1[0] == "while True:" and list1[1] == r"    player.down()":
                        input_direct = "down"

                except Exception:
                    print("运行错误，请检查您的代码")

                    print("请重新编写代码")
                    terminal_input = ''


        pygame.event.post(pygame.event.Event(USEREVENT, {"user_direct": input_direct}))
        if event.type == USEREVENT and event.user_direct == "right":
            rect_game4.x += 2
        if event.type == USEREVENT and event.user_direct == "left":
            rect_game4.x -= 2
        if event.type == USEREVENT and event.user_direct == "down":
            rect_game4.y += 2
        if event.type == USEREVENT and event.user_direct == "up":
            rect_game4.y -= 2
        if rect_game4.colliderect(rect2) and game4_score != 1:
            game4_score += 1
        if game4_score == 1:
            game_lock_state_list[3] = 1

            surface.fill(white)
            # game_pass_state = 1
            # game_pass()
            if pass_time_time == 0:
                pass_time = int(time.time()-start_time)
                pass_time_time += 1
            surface.blit(pass_all_img, (0, 0))
            text("本次通过全部关卡的时间为{}".format(pass_time), (200, 200), 40)

            if pass_time < fastest_time:
                text("恭喜你突破了记录！！！", (200, 250), 50)
                with open('admin/fastest_time.json', 'w') as fd:
                    fd.write(str(pass_time))
            else:
                text("不要灰心，再接再励！！！", (200, 250), 50)
def music():
    global music_state
    if music_state == 1:

        pygame.mixer.init()
        pygame.time.delay(1000)
        pygame.mixer.music.load('music/music.mp3')
        pygame.mixer.music.play(-1)
        music_state = 0
    if music_state == -1:
        pygame.mixer.music.stop()
        # print('jjjjjjjjjjjjjjjjjjjjj')



if __name__ == "__main__":
    start_time = time.time()
    with open("admin/record.txt", "r") as fh1:
        game_lock_state_list = fh1.read()
    print(game_lock_state_list)
    game_lock_state_list = game_lock_state_list.split(",")
    for i in range(len(game_lock_state_list)):
        game_lock_state_list[i] = int(game_lock_state_list[i].strip("[]"))
    print(game_lock_state_list)


    pygame.init()
    screen_w = 1000
    screen_h = 600
    drag_pos = None
    surface = pygame.display.set_mode((screen_w, screen_h))
    start_time1 = None
    index_view_state = 1
    state111 = 0
    pass_time = None
    start_rect = None
    difficulty_level_size = 30
    rect_game4 = pygame.Rect(0, 0, 50, 50)
    game1_Taying_Training_state = 0
    game2_find_mother_state = 0
    choose_close_state = 0
    read_key_state = 0
    game4_score = 0
    drag_state = 0
    game_pass_state = 0
    str1 = ""
    music_state = 1
    input_word = ""
    clock = pygame.time.Clock()
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    purple = (255, 0, 255)
    yellow = (255, 255, 0)
    cyan = (0, 255, 255)
    green = (0, 255, 0)
    pink = (225, 128, 192)
    blue = (0, 0, 255)
    e, f = None, None
    tick = 0
    time1 = 0
    dist = 0
    color_pos = 255
    direct = ""
    a = None
    z = 0
    sign1 = 1
    score = 0
    restart_state = 0
    state_find_mother = 0
    color_mother = []
    font1 = None
    rect1 = None
    difficulty_level_size1 = 30
    difficulty_level_size2 = 30
    difficulty_level_size3 = 30
    terminal_input = ''
    input_direct = ''
    game4_eat_star_state = 0
    # jump_game_init
    groups1 = pygame.sprite.Group()
    # tick = 0
    game4_img = pygame.image.load('img/game4.jpg')
    open_voice_img = pygame.image.load('img/open_voice.jpg')
    close_voice_img = pygame.image.load('img/close_voice.jpg')
    choose_back_img = pygame.image.load('img/choose_back.jpg')
    pass_all_img = pygame.image.load('img/pass_all.jpg')
    game3_hero_img = pygame.image.load('img/game3_hero.png').convert_alpha()
    game3_jump_state = 0
    direction = ""
    if game3_jump_state == 1:
        pygame.key.set_repeat(10, 10)
    game3_a = 0
    t = 0
    ifRange = False
    jumpSpeed = 0
    pass_time_time = 0
    state = ""
    make_big_state = 0
    index_a, index_b, index_c = None, None, None
    player = player()
    game3_time = 0
    game1_difficulty_level = 70
    game2_difficulty_level = 1
    game3_difficulty_level = 15




    for i in range(12):
        color_mother.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        # mother = ["<class 'list'>", "<class 'int'>", "<class 'dict'>", "<class 'tuple'>", "<class 'str'>", "<class 'set'>", "<class 'float'>", "<class 'bool'>", "<class 'complex'>", "<class 'type'>", "<class 'NoneType'>"]

    code_find_mother = """
for i in range(11):
    locals()["mother1_dist"+str(i)] = (random.randint(100, screen_w-100), random.randint(100, screen_h-100))
int_child = random.randint(0, 1000)
float_child = random.uniform(1, 10)
float_child = float("{0:.3f}".format(float_child))
child_dist = [random.randint(100, screen_w-100), random.randint(100, screen_h-100)]
str_child = '"'+"".join(random.sample(string.printable, random.randint(0, 10)))+'"'
list_child = list(str_child[1: 3])
tuple_child = tuple(str_child[1: 3])
dict_child = dict().fromkeys([int_child,float_child], str_child[1:3])
set_child = set(str_child)
bool_child = random.choice([False, True])
class a:
    def __str__(self):
        return "class a:"
class_child = a 
complex_child = complex(round(random.uniform(1, 10), random.randint(0, 3)), round(random.uniform(-9, 10), random.randint(0, 3)))
None_child = None
random_child = random.choice([class_child, int_child, float_child, complex_child, bool_child, None_child, dict_child, tuple_child, set_child, list_child, str_child])
    """
    game3_img = pygame.image.load("img/game3.jpg")
    with open('admin/fastest_time.json', 'r') as fo1:
        fastest_time = int(json.loads(fo1.read()))

        print(fastest_time)
    while True:
        music()

        # print(drag_state, "lalalalaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        surface.fill((255, 255, 255))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                try:
                    sys.exit(1)
                except SystemExit as error:
                    with open("admin/record.txt", "w") as fh:
                        print(str(game_lock_state_list), "end")
                        fh.write(str(game_lock_state_list))

                finally:
                    # time.sleep(2)
                    sys.exit()
            read_key_font, read_key_rect = read_key(True)
        game3_time += 1
        if game1_Taying_Training_state == 1:
            game1_background = pygame.image.load("img/game1.jpg")

            surface.blit(game1_background, (0, 0))

        if read_key_font != None and read_key_state == 1:
            surface.blit(read_key_font, read_key_rect)

        if state_find_mother == 0:
            # print(33)

            exec(code_find_mother)


        print(index_view_state, choose_close_state, game1_Taying_Training_state, read_key_state, game2_find_mother_state,game3_jump_state, game4_eat_star_state, game_pass_state)
        # game4_eat_star()
        index_view()
        choose_close()

        if choose_close_state == 1:

            button(pygame.Rect(0, 0, screen_w // 5, screen_h // 3), game1_Taying_Training)
        if restart_state == 1:
            button(pygame.Rect(400, 300, 100, 50), game1_Taying_Training)
        if choose_close_state == 1 and game_lock_state_list[1] == 1:
            button(pygame.Rect(screen_w // 5, 0, screen_w // 5, screen_h // 3), game2_find_mother)
        if choose_close_state == 1 and game_lock_state_list[2] == 1:
            button(pygame.Rect(screen_w //5*2, 0, screen_w // 5, screen_h // 3), game3_jump)
        if choose_close_state == 1 and game_lock_state_list[3] == 1:
            button(pygame.Rect(screen_w//5*3, 0, screen_w // 5, screen_h // 3), game4_eat_star)
        game_pass()
        game_restart()
        game1_Taying_Training()
        game2_find_mother()
        game3_jump()
        game4_eat_star()
        pygame.display.flip()
        clock.tick(60)







