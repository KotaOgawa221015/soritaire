import random
import tkinter as tk
from functools import partial
from PIL import Image,ImageTk,ImageDraw

#組札の完成形
spade_table = ['♠A','♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠J','♠Q','♠K']
hurt_table = ['♥A','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥J','♥Q','♥K']
dia_table = ['♦A','♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦10','♦J','♦Q','♦K']
club_table = ['♣A','♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣J','♣Q','♣K']
    
class set_game():
    def __init__(self):
        #ターン・山札 初期設定
        self.card_deck_num = 24
        self.deck_count = 0
        self.index_list = []
        self.move_suit_table =[]
        self.under_suit_table = []
        
        #場札に重ねる位置
        self.stucks1_count = 1
        self.stucks2_count = 2
        self.stucks3_count = 3
        self.stucks4_count = 4
        self.stucks5_count = 5
        self.stucks6_count = 6
        self.stucks7_count = 7

        #場札に重なっている枚数のカウント
        self.stucks1_stuck_count = 1
        self.stucks2_stuck_count = 1
        self.stucks3_stuck_count = 1
        self.stucks4_stuck_count = 1
        self.stucks5_stuck_count = 1
        self.stucks6_stuck_count = 1
        self.stucks7_stuck_count = 1

        #場札（裏返し）の格納候補
        self.card_stucks2_seacret_count = 1
        self.card_stucks3_seacret_count = 1
        self.card_stucks4_seacret_count = 1
        self.card_stucks5_seacret_count = 1
        self.card_stucks6_seacret_count = 1
        self.card_stucks7_seacret_count = 1

        #組札に重ねる位置
        self.spade_suit_count = 0
        self.hurt_suit_count = 0
        self.dia_suit_count = 0
        self.club_suit_count = 0

        #場札
        self.card_stucks1 =['*','','','','','','','','','','','','','']
        self.card_stucks2 =['*','*','','','','','','','','','','','','','']
        self.card_stucks3 =['*','*','*','','','','','','','','','','','','','']
        self.card_stucks4 =['*','*','*','*','','','','','','','','','','','','','']
        self.card_stucks5 =['*','*','*','*','*','','','','','','','','','','','','','']
        self.card_stucks6 =['*','*','*','*','*','*','','','','','','','','','','','','']
        self.card_stucks7 =['*','*','*','*','*','*','*','','','','','','','','','','','']

        #組札
        self.spade_suit =['','','','','','','','','','','','','']
        self.hurt_suit =['','','','','','','','','','','','','']
        self.dia_suit =['','','','','','','','','','','','','']
        self.club_suit =['','','','','','','','','','','','','']

        #山札と場札（裏返し）の作成
        self.all_card = spade_table + hurt_table + dia_table + club_table
        self.deck_before_shuffle = random.sample(self.all_card,len(self.all_card))
        self.seacret_card,self.card_deck = self.deck_before_shuffle[:28],self.deck_before_shuffle[28:]
        self.card_stucks1_seacret,self.card_stucks2_seacret,self.card_stucks3_seacret,self.card_stucks4_seacret,self.card_stucks5_seacret,self.card_stucks6_seacret,self.card_stucks7_seacret= self.seacret_card[:1],self.seacret_card[1:3],self.seacret_card[3:6],self.seacret_card[6:10],self.seacret_card[10:15],self.seacret_card[15:21],self.seacret_card[21:]
        self.card_stucks1[0] = self.card_stucks1_seacret[0]
        self.card_stucks2[1] = self.card_stucks2_seacret[0]
        self.card_stucks3[2] = self.card_stucks3_seacret[0]
        self.card_stucks4[3] = self.card_stucks4_seacret[0]
        self.card_stucks5[4] = self.card_stucks5_seacret[0]
        self.card_stucks6[5] = self.card_stucks6_seacret[0]
        self.card_stucks7[6] = self.card_stucks7_seacret[0]
    
    def get_configulation(self):
        return self.card_deck_num,self.index_list,self.move_suit_table,self.under_suit_table
    
    def get_deck(self):
        return self.card_deck,self.deck_count
    
    def get_card_stucks(self):
            return self.card_stucks1,self.card_stucks2,self.card_stucks3,self.card_stucks4,self.card_stucks5,self.card_stucks6,self.card_stucks7
    
    def get_stucks_count(self):
        return self.stucks1_count,self.stucks2_count,self.stucks3_count,self.stucks4_count,self.stucks5_count,self.stucks6_count,self.stucks7_count

    def get_stucks_stuck_count(self):
        return self.stucks1_stuck_count,self.stucks2_stuck_count,self.stucks3_stuck_count,self.stucks4_stuck_count,self.stucks5_stuck_count,self.stucks6_stuck_count,self.stucks7_stuck_count
    
    def get_card_stucks_seacret(self):
        return self.card_stucks1_seacret,self.card_stucks2_seacret,self.card_stucks3_seacret,self.card_stucks4_seacret,self.card_stucks5_seacret,self.card_stucks6_seacret,self.card_stucks7_seacret

    def get_card_stucks_seacret_count(self):
        return self.card_stucks2_seacret_count,self.card_stucks3_seacret_count,self.card_stucks4_seacret_count,self.card_stucks5_seacret_count,self.card_stucks6_seacret_count,self.card_stucks7_seacret_count

    def get_suit_count(self):
        return self.spade_suit_count,self.hurt_suit_count,self.dia_suit_count,self.club_suit_count

    def get_suit(self):
        return self.spade_suit,self.hurt_suit,self.dia_suit,self.club_suit

class game_field(tk.Canvas):
    def __init__(self,master):
        super().__init__()
        self.master = master
        
        self.canvas_deck = tk.Canvas(master, width=120 , height=170,bg='green3')

        self.canvas_deck_open = tk.Canvas(master, width=120 , height=170,bg='green',highlightthickness=0)

        self.canvas_spade = tk.Canvas(master , width=120 , height=170,bg='green3')

        self.canvas_hurt = tk.Canvas(master , width=120 , height=170,bg='green3')

        self.canvas_dia = tk.Canvas(master , width=120 , height=170,bg='green3')

        self.canvas_club = tk.Canvas(master , width=120 , height=170,bg='green3')

        self.canvas_stucks1 = tk.Canvas(master, width=120 , height=695,bg='green',highlightthickness=0)

        self.canvas_stucks2 = tk.Canvas(master, width=120 , height=695,bg='green',highlightthickness=0)

        self.canvas_stucks3 = tk.Canvas(master, width=120 , height=695,bg='green',highlightthickness=0)

        self.canvas_stucks4 = tk.Canvas(master, width=120 , height=695,bg='green',highlightthickness=0)

        self.canvas_stucks5 = tk.Canvas(master, width=120 , height=695,bg='green',highlightthickness=0)

        self.canvas_stucks6 = tk.Canvas(master, width=120 , height=695,bg='green',highlightthickness=0)

        self.canvas_stucks7 = tk.Canvas(master, width=120 , height=695,bg='green',highlightthickness=0)

        #山札の矢印
        self.canvas_arrow_deck_open = tk.Canvas(master, width=70 , height=40,bg='green',highlightthickness=0)

        #スペードの矢印
        self.canvas_arrow_spade_suit = tk.Canvas(master, width=70 , height=40,bg='green',highlightthickness=0)

        #ハートの矢印
        self.canvas_arrow_hurt_suit = tk.Canvas(master, width=70 , height=40,bg='green',highlightthickness=0)

        #ダイヤの矢印
        self.canvas_arrow_dia_suit = tk.Canvas(master, width=70 , height=40,bg='green',highlightthickness=0)

        #クラブの矢印
        self.canvas_arrow_club_suit = tk.Canvas(master, width=70 , height=40,bg='green',highlightthickness=0)

        #場札1の矢印
        self.canvas_arrow_stuck1 = tk.Canvas(master, width=70 , height=50,bg='green',highlightthickness=0)

        #場札2の矢印
        self.canvas_arrow_stuck2 = tk.Canvas(master, width=70 , height=50,bg='green',highlightthickness=0)

        #場札3の矢印
        self.canvas_arrow_stuck3 = tk.Canvas(master, width=70 , height=50,bg='green',highlightthickness=0)

        #場札4の矢印
        self.canvas_arrow_stuck4 = tk.Canvas(master, width=70 , height=50,bg='green',highlightthickness=0)

        #場札5の矢印
        self.canvas_arrow_stuck5 = tk.Canvas(master, width=70 , height=50,bg='green',highlightthickness=0)

        #場札6の矢印
        self.canvas_arrow_stuck6 = tk.Canvas(master, width=70 , height=50,bg='green',highlightthickness=0)

        #場札7の矢印
        self.canvas_arrow_stuck7 = tk.Canvas(master, width=70 , height=50,bg='green',highlightthickness=0)


        self.spade_img = tk.PhotoImage(file = 'tramp_picture/start_spade.png',width=120,height=170)
        
        self.canvas_spade.create_image(7,3,image=self.spade_img, tags='spade',anchor=tk.NW)

        self.hurt_img = tk.PhotoImage(file = 'tramp_picture/start_hurt.png',width=120,height=170)

        self.canvas_hurt.create_image(7,3,image=self.hurt_img, tags='hurt',anchor=tk.NW)

        self.dia_img = tk.PhotoImage(file = 'tramp_picture/start_dia.png',width=120,height=170)

        self.canvas_dia.create_image(7,3,image=self.dia_img, tags='dia',anchor=tk.NW)

        self.club_img = tk.PhotoImage(file = 'tramp_picture/start_club.png',width=120,height=170)

        self.canvas_club.create_image(7,3,image=self.club_img, tags='club',anchor=tk.NW)

        #キャンバスの位置設定

        self.canvas_deck.place(x=30,y=30)

        self.canvas_deck_open.place(x=170,y=30)

        self.canvas_spade.place(x=400,y=30)

        self.canvas_hurt.place(x=540,y=30)

        self.canvas_dia.place(x=680,y=30)

        self.canvas_club.place(x=820,y=30)

        self.canvas_stucks1.place(x=20,y=310)

        self.canvas_stucks2.place(x=160,y=310)

        self.canvas_stucks3.place(x=300,y=310)

        self.canvas_stucks4.place(x=440,y=310)

        self.canvas_stucks5.place(x=580,y=310)

        self.canvas_stucks6.place(x=720,y=310)

        self.canvas_stucks7.place(x=860,y=310)

        self.game = set_game()

        #場札の裏返し部分を作った数
        self.picture_count = 1

        #トリミング画像を作った数
        self.cropped_count = 0

        self.card_deck,self.deck_count = self.game.get_deck()

        self.card_deck_num,self.index_list,self.move_suit_table,self.under_suit_table = self.game.get_configulation()

        self.card_stucks1,self.card_stucks2,self.card_stucks3,self.card_stucks4,self.card_stucks5,self.card_stucks6,self.card_stucks7 = self.game.get_card_stucks()

        self.stucks1_count,self.stucks2_count,self.stucks3_count,self.stucks4_count,self.stucks5_count,self.stucks6_count,self.stucks7_count = self.game.get_stucks_count()

        self.stucks1_stuck_count,self.stucks2_stuck_count,self.stucks3_stuck_count,self.stucks4_stuck_count,self.stucks5_stuck_count,self.stucks6_stuck_count,self.stucks7_stuck_count =self.game.get_stucks_stuck_count()

        self.card_stucks1_seacret,self.card_stucks2_seacret,self.card_stucks3_seacret,self.card_stucks4_seacret,self.card_stucks5_seacret,self.card_stucks6_seacret,self.card_stucks7_seacret = self.game.get_card_stucks_seacret()

        self.card_stucks2_seacret_count,self.card_stucks3_seacret_count,self.card_stucks4_seacret_count,self.card_stucks5_seacret_count,self.card_stucks6_seacret_count,self.card_stucks7_seacret_count = self.game.get_card_stucks_seacret_count()

        self.spade_suit,self.hurt_suit,self.dia_suit,self.club_suit = self.game.get_suit()

        self.spade_suit_count,self.hurt_suit_count,self.dia_suit_count,self.club_suit_count = self.game.get_suit_count()

        self.before_card = ''

        self.before_event_y = 0
        
        #山札の生成
        self.backside_img = self.create_backside_image()
        self.canvas_deck.create_image(7,3,image=self.backside_img, tags='deck',anchor=tk.NW)
        
        #場札1の生成
        self.stucks1_img = tk.PhotoImage(file = 'tramp_picture/' + self.card_stucks1[self.stucks1_count - 1] + '.png', width=110 , height=155)
        self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

        #場札2の生成
        self.picture_count += 1

        self.counter2 = self.card_stucks2.count('*')

        self.stucks2 = 'tramp_picture/' + self.card_stucks2[self.stucks2_count - 1] + '.png'

        self.create_first_stucks_picture(self.stucks2,self.counter2,self.picture_count).save('create_picture/stucks2_picture.png')

        self.stucks2_picture = 'create_picture/stucks2_picture.png'

        self.stucks2_open = Image.open(self.stucks2_picture)

        self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

        self.canvas_stucks2.place(x=160,y=310)

        #場札3の生成
        self.picture_count += 1

        self.counter3 = self.card_stucks3.count('*')

        self.stucks3 = 'tramp_picture/' + self.card_stucks3[self.stucks3_count - 1] + '.png'

        self.create_first_stucks_picture(self.stucks3,self.counter3,self.picture_count).save('create_picture/stucks3_picture.png')

        self.stucks3_picture = 'create_picture/stucks3_picture.png'

        self.stucks3_open = Image.open(self.stucks3_picture)

        self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

        self.canvas_stucks3.place(x=300,y=310)

        #場札4の生成
        self.picture_count += 1

        self.counter4 = self.card_stucks4.count('*')

        self.stucks4 = 'tramp_picture/' + self.card_stucks4[self.stucks4_count - 1] + '.png'

        self.create_first_stucks_picture(self.stucks4,self.counter4,self.picture_count).save('create_picture/stucks4_picture.png')

        self.stucks4_picture = 'create_picture/stucks4_picture.png'

        self.stucks4_open = Image.open(self.stucks4_picture)

        self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

        self.canvas_stucks4.place(x=440,y=310)

        #場札5の生成
        self.picture_count += 1

        self.counter5 = self.card_stucks5.count('*')

        self.stucks5 = 'tramp_picture/' + self.card_stucks5[self.stucks5_count - 1] + '.png'

        self.create_first_stucks_picture(self.stucks5,self.counter5,self.picture_count).save('create_picture/stucks5_picture.png')

        self.stucks5_picture = 'create_picture/stucks5_picture.png'

        self.stucks5_open = Image.open(self.stucks5_picture)

        self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

        self.canvas_stucks5.place(x=580,y=310)

        #場札6の生成
        self.picture_count += 1

        self.counter6 = self.card_stucks6.count('*')

        self.stucks6 = 'tramp_picture/' + self.card_stucks6[self.stucks6_count - 1] + '.png'

        self.create_first_stucks_picture(self.stucks6,self.counter6,self.picture_count).save('create_picture/stucks6_picture.png')

        self.stucks6_picture = 'create_picture/stucks6_picture.png'

        self.stucks6_open = Image.open(self.stucks6_picture)

        self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

        self.canvas_stucks6.place(x=720,y=310)

        #場札7の生成
        self.picture_count += 1

        self.counter7 = self.card_stucks7.count('*')

        self.stucks7 = 'tramp_picture/' + self.card_stucks7[self.stucks7_count - 1] + '.png'

        self.create_first_stucks_picture(self.stucks7,self.counter7,self.picture_count).save('create_picture/stucks7_picture.png')

        self.stucks7_picture = 'create_picture/stucks7_picture.png'

        self.stucks7_open = Image.open(self.stucks7_picture)

        self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

        self.canvas_stucks7.place(x=860,y=310)

        #イベント受付の開始
        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

        

    def deck_click_event(self,master,event):
        print(self.deck_count,self.card_deck_num)
        print(event.widget)
        print(self.card_deck)
        
        if str(event.widget) == '.!canvas':
            x,y = self.canvas_deck.canvasx(event.x),self.canvas_deck.canvasy(event.y)
            l = [self.canvas_deck.itemcget(obj, 'tags') for obj in self.canvas_deck.find_overlapping(x,y,x,y)]
        
        elif str(event.widget) == '.!canvas2':
            x,y = self.canvas_deck_open.canvasx(event.x),self.canvas_deck_open.canvasy(event.y)
            l = [self.canvas_deck_open.itemcget(obj, 'tags') for obj in self.canvas_deck_open.find_overlapping(x,y,x,y)]

        print(l)

        if 'deck' in l[0]:
            if self.card_deck_num == 0:
                j = 0
                while True:
                    if j >= len(self.card_deck):
                        break
                    if self.card_deck[j] == "":
                        del self.card_deck[j]
                        #print("山札：",card_deck,j)
                        continue
                    #print("山札：",card_deck,j)
                    j += 1
                self.deck_count = 0
                self.card_deck_num = len(self.card_deck)
                self.deck_open_img = None
                self.backside_img = self.create_backside_image()
                self.canvas_deck.create_image(7,4,image=self.backside_img, tags='deck',anchor=tk.NW)
                return
            self.create_deck_open_image(self.card_deck,self.deck_count)
            self.deck_count = self.deck_count + 1
            self.card_deck_num = self.card_deck_num -1
            self.canvas_deck_open.tag_bind('open','<ButtonPress>',partial(self.deck_click_event,self))

        elif 'open' in l[0]:
            #山札の矢印
            self.canvas_arrow_deck_open_img = tk.PhotoImage(file = 'tramp_picture/up_arrow.png',width=70,height=40)

            self.canvas_arrow_deck_open.create_image(7,3,image=self.canvas_arrow_deck_open_img , tags='arrow',anchor=tk.NW)

            self.canvas_arrow_deck_open.place(x=195,y=210)

            self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.create_spade_image,self))

            self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.create_hurt_image,self))

            self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.create_dia_image,self))

            self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.create_club_image,self))

            self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.move_deckcard_to_stucks,self))

            self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.move_deckcard_to_stucks,self))

            self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.move_deckcard_to_stucks,self))

            self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.move_deckcard_to_stucks,self))

            self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.move_deckcard_to_stucks,self))

            self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.move_deckcard_to_stucks,self))

            self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.move_deckcard_to_stucks,self))

            self.canvas_deck.tag_unbind('deck','<ButtonPress>')

        if self.card_deck_num == 0:
            self.backside_img = None

    def stucks_click_event(self,master,event):
        print(event.widget)
        self.before_card = str(event.widget)
        self.before_event_y = int(event.y)

        if str(event.widget) == '.!canvas7':
            if self.stucks1_count == 0:
                return
            
            else:
                #場札1の矢印
                self.canvas_arrow_stuck_img = tk.PhotoImage(file = 'tramp_picture/down_arrow.png',width=70,height=50)

                self.canvas_arrow_stuck1.create_image(7,3,image=self.canvas_arrow_stuck_img, tags='arrow',anchor=tk.NW)

                self.canvas_arrow_stuck1.place(x=45,y=260)

                self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

        if str(event.widget) == '.!canvas8':
            if self.stucks2_count == 0:
                return
            else:
                #場札2の矢印
                self.canvas_arrow_stuck_img = tk.PhotoImage(file = 'tramp_picture/down_arrow.png',width=70,height=50)

                self.canvas_arrow_stuck2.create_image(7,3,image=self.canvas_arrow_stuck_img, tags='arrow',anchor=tk.NW)

                self.canvas_arrow_stuck2.place(x=185,y=260)

                self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))
 
        if str(event.widget) == '.!canvas9':
            if self.stucks3_count == 0:
                return
            else:
                #場札3の矢印
                self.canvas_arrow_stuck_img = tk.PhotoImage(file = 'tramp_picture/down_arrow.png',width=70,height=50)

                self.canvas_arrow_stuck3.create_image(7,3,image=self.canvas_arrow_stuck_img, tags='arrow',anchor=tk.NW)

                self.canvas_arrow_stuck3.place(x=325,y=260)

                self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

        if str(event.widget) == '.!canvas10':
            if self.stucks4_count == 0:
                return
            else:
                #場札4の矢印
                self.canvas_arrow_stuck_img = tk.PhotoImage(file = 'tramp_picture/down_arrow.png',width=70,height=50)

                self.canvas_arrow_stuck4.create_image(7,3,image=self.canvas_arrow_stuck_img, tags='arrow',anchor=tk.NW)

                self.canvas_arrow_stuck4.place(x=465,y=260)

                self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))
        
        if str(event.widget) == '.!canvas11':
            if self.stucks5_count == 0:
                return
            else:
                #場札5の矢印
                self.canvas_arrow_stuck_img = tk.PhotoImage(file = 'tramp_picture/down_arrow.png',width=70,height=50)

                self.canvas_arrow_stuck5.create_image(7,3,image=self.canvas_arrow_stuck_img, tags='arrow',anchor=tk.NW)

                self.canvas_arrow_stuck5.place(x=605,y=260)

                self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))
        
        if str(event.widget) == '.!canvas12':
            if self.stucks6_count == 0:
                return
            else:
                #場札6の矢印
                self.canvas_arrow_stuck_img = tk.PhotoImage(file = 'tramp_picture/down_arrow.png',width=70,height=50)

                self.canvas_arrow_stuck6.create_image(7,3,image=self.canvas_arrow_stuck_img, tags='arrow',anchor=tk.NW)

                self.canvas_arrow_stuck6.place(x=745,y=260)

                self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

        if str(event.widget) == '.!canvas13':
            if self.stucks7_count == 0:
                return
            else:
                #場札7の矢印
                self.canvas_arrow_stuck_img = tk.PhotoImage(file = 'tramp_picture/down_arrow.png',width=70,height=50)

                self.canvas_arrow_stuck7.create_image(7,3,image=self.canvas_arrow_stuck_img, tags='arrow',anchor=tk.NW)

                self.canvas_arrow_stuck7.place(x=885,y=260)

                self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.move_stuckscard_to_suit,self))

                self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

                self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.move_stuckscard_to_stucks,self))

    def suit_click_event(self,master,event):
        print(event.widget)
        self.before_card = str(event.widget)

        if str(event.widget) == '.!canvas3':
            if self.spade_suit_count == 0:
                return
            
            #スペードの矢印
            self.canvas_arrow_suit_img = tk.PhotoImage(file = 'tramp_picture/up_arrow.png',width=70,height=40)

            self.canvas_arrow_spade_suit.create_image(7,3,image=self.canvas_arrow_suit_img , tags='arrow',anchor=tk.NW)

            self.canvas_arrow_spade_suit.place(x=425,y=210)

            self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

        
        elif str(event.widget) == '.!canvas4':
            if self.hurt_suit_count == 0:
                return
            
            #ハートの矢印
            self.canvas_arrow_suit_img = tk.PhotoImage(file = 'tramp_picture/up_arrow.png',width=70,height=40)

            self.canvas_arrow_hurt_suit.create_image(7,3,image=self.canvas_arrow_suit_img , tags='arrow',anchor=tk.NW)

            self.canvas_arrow_hurt_suit.place(x=565,y=210)

            self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            
        elif str(event.widget) == '.!canvas5':
            if self.dia_suit_count == 0:
                return
            
            #ダイヤの矢印
            self.canvas_arrow_suit_img = tk.PhotoImage(file = 'tramp_picture/up_arrow.png',width=70,height=40)

            self.canvas_arrow_dia_suit.create_image(7,3,image=self.canvas_arrow_suit_img , tags='arrow',anchor=tk.NW)

            self.canvas_arrow_dia_suit.place(x=705,y=210)

            self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

        
        elif str(event.widget) == '.!canvas6':
            if self.club_suit_count == 0:
                return
            
            #クラブの矢印
            self.canvas_arrow_suit_img = tk.PhotoImage(file = 'tramp_picture/up_arrow.png',width=70,height=40)

            self.canvas_arrow_club_suit.create_image(7,3,image=self.canvas_arrow_suit_img , tags='arrow',anchor=tk.NW)

            self.canvas_arrow_club_suit.place(x=845,y=210)

            self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

            self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.move_suitcard_to_stucks,self))

    def create_deck_open_image(self,card_deck,deck_count):
        self.open_deck = 'tramp_picture/' + card_deck[deck_count] + '.png'
        self.deck_open_img = tk.PhotoImage(file = self.open_deck, width=110 , height=155)
        self.canvas_deck_open.create_image(7,7.5,image=self.deck_open_img, tags='open',anchor=tk.NW)

    def move_deckcard_to_stucks(self,master,event):
        if str(event.widget) == '.!canvas7':
            x,y = self.canvas_stucks1.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_stucks1.itemcget(obj, 'tags') for obj in self.canvas_stucks1.find_overlapping(x,y,x,y)]

        elif str(event.widget) == '.!canvas8':
            x,y = self.canvas_stucks2.canvasx(event.x),self.canvas_stucks2.canvasy(event.y)
            l = [self.canvas_stucks2.itemcget(obj, 'tags') for obj in self.canvas_stucks2.find_overlapping(x,y,x,y)]

        elif str(event.widget) == '.!canvas9':
            x,y = self.canvas_stucks3.canvasx(event.x),self.canvas_stucks3.canvasy(event.y)
            l = [self.canvas_stucks3.itemcget(obj, 'tags') for obj in self.canvas_stucks3.find_overlapping(x,y,x,y)]

        elif str(event.widget) == '.!canvas10':
            x,y = self.canvas_stucks4.canvasx(event.x),self.canvas_stucks4.canvasy(event.y)
            l = [self.canvas_stucks4.itemcget(obj, 'tags') for obj in self.canvas_stucks4.find_overlapping(x,y,x,y)]

        elif str(event.widget) == '.!canvas11':
            x,y = self.canvas_stucks5.canvasx(event.x),self.canvas_stucks5.canvasy(event.y)
            l = [self.canvas_stucks5.itemcget(obj, 'tags') for obj in self.canvas_stucks5.find_overlapping(x,y,x,y)]

        elif str(event.widget) == '.!canvas12':
            x,y = self.canvas_stucks6.canvasx(event.x),self.canvas_stucks6.canvasy(event.y)
            l = [self.canvas_stucks6.itemcget(obj, 'tags') for obj in self.canvas_stucks6.find_overlapping(x,y,x,y)]

        elif str(event.widget) == '.!canvas13':
            x,y = self.canvas_stucks7.canvasx(event.x),self.canvas_stucks7.canvasy(event.y)
            l = [self.canvas_stucks7.itemcget(obj, 'tags') for obj in self.canvas_stucks7.find_overlapping(x,y,x,y)]

        print(event.widget)

        print(l)

        if 'stucks1' in l[0]:
            if self.card_stucks1[0] == '':
                if self.card_deck[self.deck_count - 1].endswith('K'):
                    self.card_stucks1[self.stucks1_count] = self.card_deck[self.deck_count - 1]
                    self.card_deck[self.deck_count - 1] = ''
                    self.stucks1_count += 1
                    self.stucks1_stuck_count += 1
                    self.stucks1_img = tk.PhotoImage(file = 'tramp_picture/' + self.card_stucks1[self.stucks1_count-1] + '.png', width=110 , height=155)
                    self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)
                    self.canvas_stucks1.place(x=20,y=310)
                    self.deck_open_img = None
                    self.canvas_deck_open.tag_unbind('open','<ButtonPress>')
            
            else:
                if self.card_deck[self.deck_count - 1].startswith('♠'):
                    set_table = spade_table

                elif self.card_deck[self.deck_count - 1].startswith('♥'):
                    set_table = hurt_table

                elif self.card_deck[self.deck_count - 1].startswith('♦'):
                    set_table = dia_table

                elif self.card_deck[self.deck_count - 1].startswith('♣'):
                    set_table = club_table

                if self.card_stucks1[self.stucks1_count-1].startswith('♠'):
                    if self.card_deck[self.deck_count - 1].startswith('♠') or self.card_deck[self.deck_count - 1].startswith('♣'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = spade_table

                elif self.card_stucks1[self.stucks1_count-1].startswith('♥'):
                    if self.card_deck[self.deck_count - 1].startswith('♥') or self.card_deck[self.deck_count - 1].startswith('♦'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = hurt_table

                elif self.card_stucks1[self.stucks1_count-1].startswith('♦'):
                    if self.card_deck[self.deck_count - 1].startswith('♥') or self.card_deck[self.deck_count - 1].startswith('♦'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = dia_table

                elif self.card_stucks1[self.stucks1_count-1].startswith('♣'):
                    if self.card_deck[self.deck_count - 1].startswith('♠') or self.card_deck[self.deck_count - 1].startswith('♣'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = club_table

                if set_table[stuck_table.index(self.card_stucks1[self.stucks1_count-1])-1] == self.card_deck[self.deck_count - 1]:
                    self.card_stucks1[self.stucks1_count] = self.card_deck[self.deck_count - 1]
                    self.card_deck[self.deck_count - 1] = ''
                    self.stucks1_count += 1
                    self.stucks1_stuck_count += 1
                    self.deck_open_img = None
                    self.canvas_deck_open.tag_unbind('open','<ButtonPress>')
            
                self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                self.canvas_stucks1.place(x=20,y=310)
            

        elif 'stucks2' in l[0]:
            if self.card_stucks2[0] == '':
                if self.card_deck[self.deck_count - 1].endswith('K'):
                    self.card_stucks2[self.stucks2_count] = self.card_deck[self.deck_count - 1]
                    self.card_deck[self.deck_count - 1] = ''
                    self.stucks2_count += 1
                    self.stucks2_stuck_count += 1
                    self.stucks2_img = tk.PhotoImage(file = 'tramp_picture/' + self.card_stucks2[self.stucks2_count-1] + '.png', width=110 , height=155)
                    self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                    self.canvas_stucks2.place(x=160,y=310)
                    self.deck_open_img = None
                    self.canvas_deck_open.tag_unbind('open','<ButtonPress>')

            else:
                if self.card_deck[self.deck_count - 1].startswith('♠'):
                    set_table = spade_table

                elif self.card_deck[self.deck_count - 1].startswith('♥'):
                    set_table = hurt_table

                elif self.card_deck[self.deck_count - 1].startswith('♦'):
                    set_table = dia_table

                elif self.card_deck[self.deck_count - 1].startswith('♣'):
                    set_table = club_table

                if self.card_stucks2[self.stucks2_count-1].startswith('♠'):
                    if self.card_deck[self.deck_count - 1].startswith('♠') or self.card_deck[self.deck_count - 1].startswith('♣'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = spade_table

                elif self.card_stucks2[self.stucks2_count-1].startswith('♥'):
                    if self.card_deck[self.deck_count - 1].startswith('♥') or self.card_deck[self.deck_count - 1].startswith('♦'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = hurt_table

                elif self.card_stucks2[self.stucks2_count-1].startswith('♦'):
                    if self.card_deck[self.deck_count - 1].startswith('♥') or self.card_deck[self.deck_count - 1].startswith('♦'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = dia_table

                elif self.card_stucks2[self.stucks2_count-1].startswith('♣'):
                    if self.card_deck[self.deck_count - 1].startswith('♠') or self.card_deck[self.deck_count - 1].startswith('♣'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = club_table

                if set_table[stuck_table.index(self.card_stucks2[self.stucks2_count-1])-1] == self.card_deck[self.deck_count - 1]:
                    self.card_stucks2[self.stucks2_count] = self.card_deck[self.deck_count - 1]
                    self.card_deck[self.deck_count - 1] = ''
                    self.stucks2_count += 1
                    self.stucks2_stuck_count += 1
                    self.deck_open_img = None
                    self.canvas_deck_open.tag_unbind('open','<ButtonPress>')

                else:
                    #受付の解除
                    self.canvas_arrow_deck_open_img = None
                    
                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                self.counter2 = self.card_stucks2.count('*')
                print(self.counter2)

                if self.counter2 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,event)

                    backside_img = self.chain_backside_picture(self.counter2,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                    
                    self.stucks2_picture = 'create_picture/stucks2_picture.png'

                    self.stucks2_open = Image.open(self.stucks2_picture)

                    self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                    self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                
                else:
                    self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                    self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                self.canvas_stucks2.place(x=160,y=310)

        
        elif 'stucks3' in l[0]:
            if self.card_stucks3[0] == '':
                if self.card_deck[self.deck_count - 1].endswith('K'):
                    self.card_stucks3[self.stucks3_count] = self.card_deck[self.deck_count - 1]
                    self.card_deck[self.deck_count - 1] = ''
                    self.stucks3_count += 1
                    self.stucks3_stuck_count += 1
                    self.stucks3_img = tk.PhotoImage(file = 'tramp_picture/' + self.card_stucks3[self.stucks3_count-1] + '.png', width=110 , height=155)
                    self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                    self.canvas_stucks3.place(x=300,y=310)
                    self.deck_open_img = None
                    self.canvas_deck_open.tag_unbind('open','<ButtonPress>')
                
            else:
                if self.card_deck[self.deck_count - 1].startswith('♠'):
                    set_table = spade_table

                elif self.card_deck[self.deck_count - 1].startswith('♥'):
                    set_table = hurt_table

                elif self.card_deck[self.deck_count - 1].startswith('♦'):
                    set_table = dia_table

                elif self.card_deck[self.deck_count - 1].startswith('♣'):
                    set_table = club_table

                if self.card_stucks3[self.stucks3_count-1].startswith('♠'):
                    if self.card_deck[self.deck_count - 1].startswith('♠') or self.card_deck[self.deck_count - 1].startswith('♣'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = spade_table

                elif self.card_stucks3[self.stucks3_count-1].startswith('♥'):
                    if self.card_deck[self.deck_count - 1].startswith('♥') or self.card_deck[self.deck_count - 1].startswith('♦'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = hurt_table

                elif self.card_stucks3[self.stucks3_count-1].startswith('♦'):
                    if self.card_deck[self.deck_count - 1].startswith('♥') or self.card_deck[self.deck_count - 1].startswith('♦'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = dia_table

                elif self.card_stucks3[self.stucks3_count-1].startswith('♣'):
                    if self.card_deck[self.deck_count - 1].startswith('♠') or self.card_deck[self.deck_count - 1].startswith('♣'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = club_table

                if set_table[stuck_table.index(self.card_stucks3[self.stucks3_count-1])-1] == self.card_deck[self.deck_count - 1]:
                    self.card_stucks3[self.stucks3_count] = self.card_deck[self.deck_count - 1]
                    self.card_deck[self.deck_count - 1] = ''
                    self.stucks3_count += 1
                    self.stucks3_stuck_count += 1
                    self.deck_open_img = None
                    self.canvas_deck_open.tag_unbind('open','<ButtonPress>')
                
                else:
                    #受付の解除
                    self.canvas_arrow_deck_open_img = None
                    
                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                
                self.counter3 = self.card_stucks3.count('*')
                print(self.counter3)

                if self.counter3 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,event)

                    backside_img = self.chain_backside_picture(self.counter3,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                    
                    self.stucks3_picture = 'create_picture/stucks3_picture.png'

                    self.stucks3_open = Image.open(self.stucks3_picture)

                    self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                    self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                
                else:
                    self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                    self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                self.canvas_stucks3.place(x=300,y=310)


        elif 'stucks4' in l[0]:
            if self.card_stucks4[0] == '':
                if self.card_deck[self.deck_count - 1].endswith('K'):
                    self.card_stucks4[self.stucks4_count] = self.card_deck[self.deck_count - 1]
                    self.card_deck[self.deck_count - 1] = ''
                    self.stucks4_count += 1
                    self.stucks4_stuck_count += 1
                    self.stucks4_img = tk.PhotoImage(file = 'tramp_picture/' + self.card_stucks4[self.stucks4_count-1] + '.png', width=110 , height=155)
                    self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                    self.canvas_stucks4.place(x=440,y=310)
                    self.deck_open_img = None
                    self.canvas_deck_open.tag_unbind('open','<ButtonPress>')

            else:
                if self.card_deck[self.deck_count - 1].startswith('♠'):
                    set_table = spade_table

                elif self.card_deck[self.deck_count - 1].startswith('♥'):
                    set_table = hurt_table

                elif self.card_deck[self.deck_count - 1].startswith('♦'):
                    set_table = dia_table

                elif self.card_deck[self.deck_count - 1].startswith('♣'):
                    set_table = club_table

                if self.card_stucks4[self.stucks4_count-1].startswith('♠'):
                    if self.card_deck[self.deck_count - 1].startswith('♠') or self.card_deck[self.deck_count - 1].startswith('♣'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = spade_table

                elif self.card_stucks4[self.stucks4_count-1].startswith('♥'):
                    if self.card_deck[self.deck_count - 1].startswith('♥') or self.card_deck[self.deck_count - 1].startswith('♦'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = hurt_table

                elif self.card_stucks4[self.stucks4_count-1].startswith('♦'):
                    if self.card_deck[self.deck_count - 1].startswith('♥') or self.card_deck[self.deck_count - 1].startswith('♦'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = dia_table

                elif self.card_stucks4[self.stucks4_count-1].startswith('♣'):
                    if self.card_deck[self.deck_count - 1].startswith('♠') or self.card_deck[self.deck_count - 1].startswith('♣'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = club_table

                if set_table[stuck_table.index(self.card_stucks4[self.stucks4_count-1])-1] == self.card_deck[self.deck_count - 1]:
                    self.card_stucks4[self.stucks4_count] = self.card_deck[self.deck_count - 1]
                    self.card_deck[self.deck_count - 1] = ''
                    self.stucks4_count += 1
                    self.stucks4_stuck_count += 1
                    self.deck_open_img = None
                    self.canvas_deck_open.tag_unbind('open','<ButtonPress>')
                
                else:
                    #受付の解除
                    self.canvas_arrow_deck_open_img = None
                    
                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                self.counter4 = self.card_stucks4.count('*')
                print(self.counter4)

                if self.counter4 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,event)

                    backside_img = self.chain_backside_picture(self.counter4,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                    
                    self.stucks4_picture = 'create_picture/stucks4_picture.png'

                    self.stucks4_open = Image.open(self.stucks4_picture)

                    self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                    self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                
                else:
                    self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                    self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                self.canvas_stucks4.place(x=440,y=310)


        elif 'stucks5' in l[0]:
            if self.card_stucks5[0] == '':
                if self.card_deck[self.deck_count - 1].endswith('K'):
                    self.card_stucks5[self.stucks5_count] = self.card_deck[self.deck_count - 1]
                    self.card_deck[self.deck_count - 1] = ''
                    self.stucks5_count += 1
                    self.stucks5_stuck_count += 1
                    self.stucks5_img = tk.PhotoImage(file = 'tramp_picture/' + self.card_stucks5[self.stucks5_count-1] + '.png', width=110 , height=155)
                    self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                    self.canvas_stucks5.place(x=580,y=310)
                    self.deck_open_img = None
                    self.canvas_deck_open.tag_unbind('open','<ButtonPress>')

            else:
                if self.card_deck[self.deck_count - 1].startswith('♠'):
                    set_table = spade_table

                elif self.card_deck[self.deck_count - 1].startswith('♥'):
                    set_table = hurt_table

                elif self.card_deck[self.deck_count - 1].startswith('♦'):
                    set_table = dia_table

                elif self.card_deck[self.deck_count - 1].startswith('♣'):
                    set_table = club_table

                if self.card_stucks5[self.stucks5_count-1].startswith('♠'):
                    if self.card_deck[self.deck_count - 1].startswith('♠') or self.card_deck[self.deck_count - 1].startswith('♣'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = spade_table

                elif self.card_stucks5[self.stucks5_count-1].startswith('♥'):
                    if self.card_deck[self.deck_count - 1].startswith('♥') or self.card_deck[self.deck_count - 1].startswith('♦'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = hurt_table

                elif self.card_stucks5[self.stucks5_count-1].startswith('♦'):
                    if self.card_deck[self.deck_count - 1].startswith('♥') or self.card_deck[self.deck_count - 1].startswith('♦'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = dia_table

                elif self.card_stucks5[self.stucks5_count-1].startswith('♣'):
                    if self.card_deck[self.deck_count - 1].startswith('♠') or self.card_deck[self.deck_count - 1].startswith('♣'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = club_table

                if set_table[stuck_table.index(self.card_stucks5[self.stucks5_count-1])-1] == self.card_deck[self.deck_count - 1]:
                    self.card_stucks5[self.stucks5_count] = self.card_deck[self.deck_count - 1]
                    self.card_deck[self.deck_count - 1] = ''
                    self.stucks5_count += 1
                    self.stucks5_stuck_count += 1
                    self.deck_open_img = None
                    self.canvas_deck_open.tag_unbind('open','<ButtonPress>')
                
                else:
                    #受付の解除
                    self.canvas_arrow_deck_open_img = None
                    
                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                self.counter5 = self.card_stucks5.count('*')
                print(self.counter5)

                if self.counter5 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,event)

                    backside_img = self.chain_backside_picture(self.counter5,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                    
                    self.stucks5_picture = 'create_picture/stucks5_picture.png'

                    self.stucks5_open = Image.open(self.stucks5_picture)

                    self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                    self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                else:
                    self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                    self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                self.canvas_stucks5.place(x=580,y=310)


        elif 'stucks6' in l[0]:
            if self.card_stucks6[0] == '':
                if self.card_deck[self.deck_count - 1].endswith('K'):
                    self.card_stucks6[self.stucks6_count] = self.card_deck[self.deck_count - 1]
                    self.card_deck[self.deck_count - 1] = ''
                    self.stucks6_count += 1
                    self.stucks6_stuck_count += 1
                    self.stucks6_img = tk.PhotoImage(file = 'tramp_picture/' + self.card_stucks6[self.stucks6_count-1] + '.png', width=110 , height=155)
                    self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)
                    self.canvas_stucks6.place(x=720,y=310)
                    self.deck_open_img = None
                    self.canvas_deck_open.tag_unbind('open','<ButtonPress>')

            else:
                if self.card_deck[self.deck_count - 1].startswith('♠'):
                    set_table = spade_table

                elif self.card_deck[self.deck_count - 1].startswith('♥'):
                    set_table = hurt_table

                elif self.card_deck[self.deck_count - 1].startswith('♦'):
                    set_table = dia_table

                elif self.card_deck[self.deck_count - 1].startswith('♣'):
                    set_table = club_table

                if self.card_stucks6[self.stucks6_count-1].startswith('♠'):
                    if self.card_deck[self.deck_count - 1].startswith('♠') or self.card_deck[self.deck_count - 1].startswith('♣'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = spade_table

                elif self.card_stucks6[self.stucks6_count-1].startswith('♥'):
                    if self.card_deck[self.deck_count - 1].startswith('♥') or self.card_deck[self.deck_count - 1].startswith('♦'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = hurt_table

                elif self.card_stucks6[self.stucks6_count-1].startswith('♦'):
                    if self.card_deck[self.deck_count - 1].startswith('♥') or self.card_deck[self.deck_count - 1].startswith('♦'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = dia_table

                elif self.card_stucks6[self.stucks6_count-1].startswith('♣'):
                    if self.card_deck[self.deck_count - 1].startswith('♠') or self.card_deck[self.deck_count - 1].startswith('♣'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = club_table

                if set_table[stuck_table.index(self.card_stucks6[self.stucks6_count-1])-1] == self.card_deck[self.deck_count - 1]:
                    self.card_stucks6[self.stucks6_count] = self.card_deck[self.deck_count - 1]
                    self.card_deck[self.deck_count - 1] = ''
                    self.stucks6_count += 1
                    self.stucks6_stuck_count += 1
                    self.deck_open_img = None
                    self.canvas_deck_open.tag_unbind('open','<ButtonPress>')

                else:
                    #受付の解除
                    self.canvas_arrow_deck_open_img = None
                    
                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))


                self.counter6 = self.card_stucks6.count('*')
                print(self.counter6)

                if self.counter6 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,event)

                    backside_img = self.chain_backside_picture(self.counter6,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                    
                    self.stucks6_picture = 'create_picture/stucks6_picture.png'

                    self.stucks6_open = Image.open(self.stucks6_picture)

                    self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                    self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                else:
                    self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                    self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                self.canvas_stucks6.place(x=720,y=310)


        elif 'stucks7' in l[0]:
            if self.card_stucks7[0] == '':
                if self.card_deck[self.deck_count - 1].endswith('K'):
                    self.card_stucks7[self.stucks7_count] = self.card_deck[self.deck_count - 1]
                    self.card_deck[self.deck_count] = ''
                    self.stucks7_count += 1
                    self.stucks7_stuck_count += 1
                    self.stucks7_img = tk.PhotoImage(file = 'tramp_picture/' + self.card_stucks7[self.stucks7_count-1] + '.png', width=110 , height=155)
                    self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)
                    self.canvas_stucks7.place(x=860,y=310)
                    self.deck_open_img = None
                    self.canvas_deck_open.tag_unbind('open','<ButtonPress>')

            else:
                if self.card_deck[self.deck_count - 1].startswith('♠'):
                    set_table = spade_table

                elif self.card_deck[self.deck_count - 1].startswith('♥'):
                    set_table = hurt_table

                elif self.card_deck[self.deck_count - 1].startswith('♦'):
                    set_table = dia_table

                elif self.card_deck[self.deck_count - 1].startswith('♣'):
                    set_table = club_table

                if self.card_stucks7[self.stucks7_count-1].startswith('♠'):
                    if self.card_deck[self.deck_count - 1].startswith('♠') or self.card_deck[self.deck_count - 1].startswith('♣'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = spade_table

                elif self.card_stucks7[self.stucks7_count-1].startswith('♥'):
                    if self.card_deck[self.deck_count - 1].startswith('♥') or self.card_deck[self.deck_count - 1].startswith('♦'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = hurt_table

                elif self.card_stucks7[self.stucks7_count-1].startswith('♦'):
                    if self.card_deck[self.deck_count - 1].startswith('♥') or self.card_deck[self.deck_count - 1].startswith('♦'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = dia_table

                elif self.card_stucks7[self.stucks7_count-1].startswith('♣'):
                    if self.card_deck[self.deck_count - 1].startswith('♠') or self.card_deck[self.deck_count - 1].startswith('♣'):
                        #受付の解除
                        self.canvas_arrow_deck_open_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                    stuck_table = club_table

                if set_table[stuck_table.index(self.card_stucks7[self.stucks7_count-1])-1] == self.card_deck[self.deck_count - 1]:
                    self.card_stucks7[self.stucks7_count] = self.card_deck[self.deck_count - 1]
                    self.card_deck[self.deck_count - 1] = ''
                    self.stucks7_count += 1
                    self.stucks7_stuck_count += 1
                    self.deck_open_img = None
                    self.canvas_deck_open.tag_unbind('open','<ButtonPress>')

                else:
                    #受付の解除
                    self.canvas_arrow_deck_open_img = None
                    
                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))


                self.counter7 = self.card_stucks7.count('*')
                print(self.counter7)

                if self.counter7 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,event)

                    backside_img = self.chain_backside_picture(self.counter7,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                    
                    self.stucks7_picture = 'create_picture/stucks7_picture.png'

                    self.stucks7_open = Image.open(self.stucks7_picture)

                    self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                    self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                else:
                    self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                    self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                self.canvas_stucks7.place(x=860,y=310)
        

        #受付の解除
        self.canvas_arrow_deck_open_img = None

        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

        self.canvas_club.tag_unbind('club','<ButtonPress>')

        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

        #再受付
        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

    def move_stuckscard_to_suit(self,master,event ):
        print("場札：" ,"\n","場札1",self.card_stucks1,"\n","場札2",self.card_stucks2,"\n","場札3",self.card_stucks3,"\n","場札4",self.card_stucks4,"\n","場札5",self.card_stucks5,"\n","場札6",self.card_stucks6,"\n","場札7",self.card_stucks7,"\n")
        print(event.widget)
        print('before_card:' + str(self.before_card))
        if str(event.widget) == '.!canvas3':
            x,y = self.canvas_spade.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_spade.itemcget(obj, 'tags') for obj in self.canvas_spade.find_overlapping(x,y,x,y)]

        elif str(event.widget) == '.!canvas4':
            x,y = self.canvas_hurt.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_hurt.itemcget(obj, 'tags') for obj in self.canvas_hurt.find_overlapping(x,y,x,y)]

        elif str(event.widget) == '.!canvas5':
            x,y = self.canvas_dia.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_dia.itemcget(obj, 'tags') for obj in self.canvas_dia.find_overlapping(x,y,x,y)]

        elif str(event.widget) == '.!canvas6':
            x,y = self.canvas_club.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_club.itemcget(obj, 'tags') for obj in self.canvas_club.find_overlapping(x,y,x,y)]

        print(l)

        if 'spade' in l[0]:
            if self.before_card == '.!canvas7':
                try:
                    if self.card_stucks1[self.stucks1_count - 1] == spade_table[self.spade_suit_count]:
                        self.spade_suit[self.spade_suit_count] = self.card_stucks1[self.stucks1_count - 1]
                        self.spade_suit_count += 1
                        self.card_stucks1[self.stucks1_count - 1] = ''
                        self.stucks1_count -= 1
                        self.stucks1_stuck_count -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.spade = 'tramp_picture/' + self.spade_suit[self.spade_suit_count-1] + '.png'
                self.spade_img = tk.PhotoImage(file = self.spade, width=110 , height=155)
                self.canvas_spade.create_image(7,7.5,image=self.spade_img, tags='spade',anchor=tk.NW)
                self.canvas_spade.place(x=400,y=30)

                print(self.card_stucks1)

                if self.stucks1_count == 0:
                    self.stucks1_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                    self.canvas_stucks1.place(x=20,y=310)

                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                else:
                    self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                    self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                    self.canvas_stucks1.place(x=20,y=310)

            elif self.before_card == '.!canvas8':
                try:
                    if self.card_stucks2[self.stucks2_count - 1] == spade_table[self.spade_suit_count]:
                        self.spade_suit[self.spade_suit_count] = self.card_stucks2[self.stucks2_count - 1]
                        self.spade_suit_count += 1
                        self.card_stucks2[self.stucks2_count - 1] = ''
                        self.stucks2_count -= 1
                        self.stucks2_stuck_count -= 1
                        if self.card_stucks2[self.stucks2_count-1] == '*':
                            self.card_stucks2[self.stucks2_count-1] = self.card_stucks2_seacret[self.card_stucks2_seacret_count]
                            self.card_stucks2_seacret_count += 1
                            self.stucks2_stuck_count += 1
                            self.counter2 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.spade = 'tramp_picture/' + self.spade_suit[self.spade_suit_count-1] + '.png'
                self.spade_img = tk.PhotoImage(file = self.spade, width=110 , height=155)
                self.canvas_spade.create_image(7,7.5,image=self.spade_img, tags='spade',anchor=tk.NW)
                self.canvas_spade.place(x=400,y=30)

                if self.stucks2_count == 0:
                    self.stucks2_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                    self.canvas_stucks2.place(x=160,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                else:
                    if self.counter2 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,self.before_card)

                        backside_img = self.chain_backside_picture(self.counter2,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                    
                        self.stucks2_picture = 'create_picture/stucks2_picture.png'

                        self.stucks2_open = Image.open(self.stucks2_picture)

                        self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                    
                    else:
                        self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                    self.canvas_stucks2.place(x=160,y=310)

            elif self.before_card == '.!canvas9':
                try:
                    if self.card_stucks3[self.stucks3_count - 1] == spade_table[self.spade_suit_count]:
                        self.spade_suit[self.spade_suit_count] = self.card_stucks3[self.stucks3_count - 1]
                        self.spade_suit_count += 1
                        self.card_stucks3[self.stucks3_count - 1] = ''
                        self.stucks3_count -= 1
                        self.stucks3_stuck_count -= 1

                        if self.card_stucks3[self.stucks3_count-1] == '*':
                            self.card_stucks3[self.stucks3_count-1] = self.card_stucks3_seacret[self.card_stucks3_seacret_count]
                            self.card_stucks3_seacret_count += 1
                            self.stucks3_stuck_count += 1                        
                            self.counter3 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.spade = 'tramp_picture/' + self.spade_suit[self.spade_suit_count-1] + '.png'
                self.spade_img = tk.PhotoImage(file = self.spade, width=110 , height=155)
                self.canvas_spade.create_image(7,7.5,image=self.spade_img, tags='spade',anchor=tk.NW)
                self.canvas_spade.place(x=400,y=30)

                if self.stucks3_count == 0:
                    self.stucks3_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                    
                    self.canvas_stucks3.place(x=300,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter3 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter3,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                        
                        self.stucks3_picture = 'create_picture/stucks3_picture.png'

                        self.stucks3_open = Image.open(self.stucks3_picture)

                        self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                    
                    else:
                        self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                    self.canvas_stucks3.place(x=300,y=310)

            elif self.before_card == '.!canvas10':
                try:
                    if self.card_stucks4[self.stucks4_count - 1] == spade_table[self.spade_suit_count]:
                        self.spade_suit[self.spade_suit_count] = self.card_stucks4[self.stucks4_count - 1]
                        self.spade_suit_count += 1
                        self.card_stucks4[self.stucks4_count - 1] = ''
                        self.stucks4_count -= 1
                        self.stucks4_stuck_count -= 1
                
                        if self.card_stucks4[self.stucks4_count-1] == '*':
                            self.card_stucks4[self.stucks4_count-1] = self.card_stucks4_seacret[self.card_stucks4_seacret_count]
                            self.card_stucks4_seacret_count += 1
                            self.stucks4_stuck_count += 1
                            self.counter4 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.spade = 'tramp_picture/' + self.spade_suit[self.spade_suit_count-1] + '.png'
                self.spade_img = tk.PhotoImage(file = self.spade, width=110 , height=155)
                self.canvas_spade.create_image(7,7.5,image=self.spade_img, tags='spade',anchor=tk.NW)
                self.canvas_spade.place(x=400,y=30)

                if self.stucks4_count == 0:
                    self.stucks4_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                    self.canvas_stucks4.place(x=440,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter4 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter4,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                        
                        self.stucks4_picture = 'create_picture/stucks4_picture.png'

                        self.stucks4_open = Image.open(self.stucks4_picture)

                        self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                    
                    else:
                        self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                    self.canvas_stucks4.place(x=440,y=310)

            elif self.before_card == '.!canvas11':
                try:
                    if self.card_stucks5[self.stucks5_count - 1] == spade_table[self.spade_suit_count]:
                        self.spade_suit[self.spade_suit_count] = self.card_stucks5[self.stucks5_count - 1]
                        self.spade_suit_count += 1
                        self.card_stucks5[self.stucks5_count - 1] = ''
                        self.stucks5_count -= 1
                        self.stucks5_stuck_count -= 1
                        
                        if self.card_stucks5[self.stucks5_count-1] == '*':
                            self.card_stucks5[self.stucks5_count-1] = self.card_stucks5_seacret[self.card_stucks5_seacret_count]
                            self.card_stucks5_seacret_count += 1
                            self.stucks5_stuck_count += 1
                            self.counter5 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.spade = 'tramp_picture/' + self.spade_suit[self.spade_suit_count-1] + '.png'
                self.spade_img = tk.PhotoImage(file = self.spade, width=110 , height=155)
                self.canvas_spade.create_image(7,7.5,image=self.spade_img, tags='spade',anchor=tk.NW)
                self.canvas_spade.place(x=400,y=30)

                if self.stucks5_count == 0:
                    self.stucks5_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                    self.canvas_stucks5.place(x=580,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter5> 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter5,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                        
                        self.stucks5_picture = 'create_picture/stucks5_picture.png'

                        self.stucks5_open = Image.open(self.stucks5_picture)

                        self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                    
                    else:
                        self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                    self.canvas_stucks5.place(x=580,y=310)

            elif self.before_card == '.!canvas12':
                try:
                    if self.card_stucks6[self.stucks6_count - 1] == spade_table[self.spade_suit_count]:
                        self.spade_suit[self.spade_suit_count] = self.card_stucks6[self.stucks6_count - 1]
                        self.spade_suit_count += 1
                        self.card_stucks6[self.stucks6_count - 1] = ''
                        self.stucks6_count -= 1
                        self.stucks6_stuck_count -= 1
                        if self.card_stucks6[self.stucks6_count-1] == '*':
                            self.card_stucks6[self.stucks6_count-1] = self.card_stucks6_seacret[self.card_stucks6_seacret_count]
                            self.card_stucks6_seacret_count += 1
                            self.stucks6_stuck_count += 1
                            self.counter6 -= 1

                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.spade = 'tramp_picture/' + self.spade_suit[self.spade_suit_count-1] + '.png'
                self.spade_img = tk.PhotoImage(file = self.spade, width=110 , height=155)
                self.canvas_spade.create_image(7,7.5,image=self.spade_img, tags='spade',anchor=tk.NW)
                self.canvas_spade.place(x=400,y=30)

                if self.stucks6_count == 0:
                    self.stucks6_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    self.canvas_stucks6.place(x=720,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                else:
                    if self.counter6 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter6,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                        
                        self.stucks6_picture = 'create_picture/stucks6_picture.png'

                        self.stucks6_open = Image.open(self.stucks6_picture)

                        self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    else:
                        self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    self.canvas_stucks6.place(x=720,y=310)

            elif self.before_card == '.!canvas13':
                try:
                    if self.card_stucks7[self.stucks7_count - 1] == spade_table[self.spade_suit_count]:
                        self.spade_suit[self.spade_suit_count] = self.card_stucks7[self.stucks7_count - 1]
                        self.spade_suit_count += 1
                        self.card_stucks7[self.stucks7_count - 1] = ''
                        self.stucks7_count -= 1
                        self.stucks7_stuck_count -= 1
                        if self.card_stucks7[self.stucks7_count-1] == '*':
                            self.card_stucks7[self.stucks7_count-1] = self.card_stucks7_seacret[self.card_stucks7_seacret_count]
                            self.card_stucks7_seacret_count += 1
                            self.stucks7_stuck_count += 1
                            self.counter7 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.spade = 'tramp_picture/' + self.spade_suit[self.spade_suit_count-1] + '.png'
                self.spade_img = tk.PhotoImage(file = self.spade, width=110 , height=155)
                self.canvas_spade.create_image(7,7.5,image=self.spade_img, tags='spade',anchor=tk.NW)
                self.canvas_spade.place(x=400,y=30)

                if self.stucks7_count == 0:
                    self.stucks7_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    self.canvas_stucks7.place(x=860,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter7:
                        openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter7,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                        
                        self.stucks7_picture = 'create_picture/stucks7_picture.png'

                        self.stucks7_open = Image.open(self.stucks7_picture)

                        self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    else:
                        self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    self.canvas_stucks7.place(x=860,y=310)

        elif 'hurt' in l[0]:
            if self.before_card == '.!canvas7':
                try:
                    if self.card_stucks1[self.stucks1_count - 1] == hurt_table[self.hurt_suit_count]:
                        self.hurt_suit[self.hurt_suit_count] = self.card_stucks1[self.stucks1_count - 1]
                        self.hurt_suit_count += 1
                        self.card_stucks1[self.stucks1_count - 1] = ''
                        self.stucks1_count -= 1
                        self.stucks1_stuck_count -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.hurt = 'tramp_picture/' + self.hurt_suit[self.hurt_suit_count-1] + '.png'
                self.hurt_img = tk.PhotoImage(file = self.hurt, width=110 , height=155)
                self.canvas_hurt.create_image(7,7.5,image=self.hurt_img, tags='hurt',anchor=tk.NW)
                self.canvas_hurt.place(x=540,y=30)

                print(self.card_stucks1)

                if self.stucks1_count == 0:
                    self.stucks1_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                    self.canvas_stucks1.place(x=20,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                    self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                    self.canvas_stucks1.place(x=20,y=310)

            elif self.before_card == '.!canvas8':
                try:
                    if self.card_stucks2[self.stucks2_count - 1] == hurt_table[self.hurt_suit_count]:
                        self.hurt_suit[self.hurt_suit_count] = self.card_stucks2[self.stucks2_count - 1]
                        self.hurt_suit_count += 1
                        self.card_stucks2[self.stucks2_count - 1] = ''
                        self.stucks2_count -= 1
                        self.stucks2_stuck_count -= 1
                        if self.card_stucks2[self.stucks2_count-1] == '*':
                            self.card_stucks2[self.stucks2_count-1] = self.card_stucks2_seacret[self.card_stucks2_seacret_count]
                            self.card_stucks2_seacret_count += 1
                            self.stucks2_stuck_count += 1
                            self.counter2 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.hurt = 'tramp_picture/' + self.hurt_suit[self.hurt_suit_count-1] + '.png'
                self.hurt_img = tk.PhotoImage(file = self.hurt, width=110 , height=155)
                self.canvas_hurt.create_image(7,7.5,image=self.hurt_img, tags='hurt',anchor=tk.NW)
                self.canvas_hurt.place(x=540,y=30)

                if self.stucks2_count == 0:
                    self.stucks2_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                    self.canvas_stucks2.place(x=160,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter2 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,self.before_card)

                        backside_img = self.chain_backside_picture(self.counter2,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                    
                        self.stucks2_picture = 'create_picture/stucks2_picture.png'

                        self.stucks2_open = Image.open(self.stucks2_picture)

                        self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                    
                    else:
                        self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                    self.canvas_stucks2.place(x=160,y=310)

            elif self.before_card == '.!canvas9':
                try:
                    if self.card_stucks3[self.stucks3_count - 1] == hurt_table[self.hurt_suit_count]:
                        self.hurt_suit[self.hurt_suit_count] = self.card_stucks3[self.stucks3_count - 1]
                        self.hurt_suit_count += 1
                        self.card_stucks3[self.stucks3_count - 1] = ''
                        self.stucks3_count -= 1
                        self.stucks3_stuck_count -= 1
                        if self.card_stucks3[self.stucks3_count-1] == '*':
                            self.card_stucks3[self.stucks3_count-1] = self.card_stucks3_seacret[self.card_stucks3_seacret_count]
                            self.card_stucks3_seacret_count += 1
                            self.stucks3_stuck_count += 1
                            self.counter3 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.hurt = 'tramp_picture/' + self.hurt_suit[self.hurt_suit_count-1] + '.png'
                self.hurt_img = tk.PhotoImage(file = self.hurt, width=110 , height=155)
                self.canvas_hurt.create_image(7,7.5,image=self.hurt_img, tags='hurt',anchor=tk.NW)
                self.canvas_hurt.place(x=540,y=30)

                if self.stucks3_count == 0:
                    self.stucks3_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                    
                    self.canvas_stucks3.place(x=300,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter3 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter3,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                        
                        self.stucks3_picture = 'create_picture/stucks3_picture.png'

                        self.stucks3_open = Image.open(self.stucks3_picture)

                        self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                    
                    else:
                        self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                    self.canvas_stucks3.place(x=300,y=310)

            elif self.before_card == '.!canvas10':
                try:
                    if self.card_stucks4[self.stucks4_count - 1] == hurt_table[self.hurt_suit_count]:
                        self.hurt_suit[self.hurt_suit_count] = self.card_stucks4[self.stucks4_count - 1]
                        self.hurt_suit_count += 1
                        self.card_stucks4[self.stucks4_count - 1] = ''
                        self.stucks4_count -= 1
                        self.stucks4_stuck_count -= 1
                        if self.card_stucks4[self.stucks4_count-1] == '*':
                            self.card_stucks4[self.stucks4_count-1] = self.card_stucks4_seacret[self.card_stucks4_seacret_count]
                            self.card_stucks4_seacret_count += 1
                            self.stucks4_stuck_count += 1
                            self.counter4 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.hurt = 'tramp_picture/' + self.hurt_suit[self.hurt_suit_count-1] + '.png'
                self.hurt_img = tk.PhotoImage(file = self.hurt, width=110 , height=155)
                self.canvas_hurt.create_image(7,7.5,image=self.hurt_img, tags='hurt',anchor=tk.NW)
                self.canvas_hurt.place(x=540,y=30)

                if self.stucks4_count == 0:
                    self.stucks4_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                    self.canvas_stucks4.place(x=440,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter4 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter4,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                        
                        self.stucks4_picture = 'create_picture/stucks4_picture.png'

                        self.stucks4_open = Image.open(self.stucks4_picture)

                        self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                    
                    else:
                        self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                    self.canvas_stucks4.place(x=440,y=310)

            elif self.before_card == '.!canvas11':
                try:
                    if self.card_stucks5[self.stucks5_count - 1] == hurt_table[self.hurt_suit_count]:
                        self.hurt_suit[self.hurt_suit_count] = self.card_stucks5[self.stucks5_count - 1]
                        self.hurt_suit_count += 1
                        self.card_stucks5[self.stucks5_count - 1] = ''
                        self.stucks5_count -= 1
                        self.stucks5_stuck_count -= 1
                        if self.card_stucks5[self.stucks5_count-1] == '*':
                            self.card_stucks5[self.stucks5_count-1] = self.card_stucks5_seacret[self.card_stucks5_seacret_count]
                            self.card_stucks5_seacret_count += 1
                            self.stucks5_stuck_count += 1
                            self.counter5 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.hurt = 'tramp_picture/' + self.hurt_suit[self.hurt_suit_count-1] + '.png'
                self.hurt_img = tk.PhotoImage(file = self.hurt, width=110 , height=155)
                self.canvas_hurt.create_image(7,7.5,image=self.hurt_img, tags='hurt',anchor=tk.NW)
                self.canvas_hurt.place(x=540,y=30)

                if self.stucks5_count == 0:
                    self.stucks5_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                    self.canvas_stucks5.place(x=580,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter5> 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter5,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                        
                        self.stucks5_picture = 'create_picture/stucks5_picture.png'

                        self.stucks5_open = Image.open(self.stucks5_picture)

                        self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                    
                    else:
                        self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                    self.canvas_stucks5.place(x=580,y=310)


            elif self.before_card == '.!canvas12':
                try:
                    if self.card_stucks6[self.stucks6_count - 1] == hurt_table[self.hurt_suit_count]:
                        self.hurt_suit[self.hurt_suit_count] = self.card_stucks6[self.stucks6_count - 1]
                        self.hurt_suit_count += 1
                        self.card_stucks6[self.stucks6_count - 1] = ''
                        self.stucks6_count -= 1
                        self.stucks6_stuck_count -= 1
                        if self.card_stucks6[self.stucks6_count-1] == '*':
                            self.card_stucks6[self.stucks6_count-1] = self.card_stucks6_seacret[self.card_stucks6_seacret_count]
                            self.card_stucks6_seacret_count += 1
                            self.stucks6_stuck_count += 1
                            self.counter6 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.hurt = 'tramp_picture/' + self.hurt_suit[self.hurt_suit_count-1] + '.png'
                self.hurt_img = tk.PhotoImage(file = self.hurt, width=110 , height=155)
                self.canvas_hurt.create_image(7,7.5,image=self.hurt_img, tags='hurt',anchor=tk.NW)
                self.canvas_hurt.place(x=540,y=30)

                if self.stucks6_count == 0:
                    self.stucks6_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    self.canvas_stucks6.place(x=720,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter6 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter6,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                        
                        self.stucks6_picture = 'create_picture/stucks6_picture.png'

                        self.stucks6_open = Image.open(self.stucks6_picture)

                        self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    else:
                        self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    self.canvas_stucks6.place(x=720,y=310)

            elif self.before_card == '.!canvas13':
                try:
                    if self.card_stucks7[self.stucks7_count - 1] == hurt_table[self.hurt_suit_count]:
                        self.hurt_suit[self.hurt_suit_count] = self.card_stucks7[self.stucks7_count - 1]
                        self.hurt_suit_count += 1
                        self.card_stucks7[self.stucks7_count - 1] = ''
                        self.stucks7_count -= 1
                        self.stucks7_stuck_count -= 1
                        if self.card_stucks7[self.stucks7_count-1] == '*':
                            self.card_stucks7[self.stucks7_count-1] = self.card_stucks7_seacret[self.card_stucks7_seacret_count]
                            self.card_stucks7_seacret_count += 1
                            self.stucks7_stuck_count += 1
                            self.counter7 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.hurt = 'tramp_picture/' + self.hurt_suit[self.hurt_suit_count-1] + '.png'
                self.hurt_img = tk.PhotoImage(file = self.hurt, width=110 , height=155)
                self.canvas_hurt.create_image(7,7.5,image=self.hurt_img, tags='hurt',anchor=tk.NW)
                self.canvas_hurt.place(x=540,y=30)

                if self.stucks7_count == 0:
                    self.stucks7_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    self.canvas_stucks7.place(x=860,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter7:
                        openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter7,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                        
                        self.stucks7_picture = 'create_picture/stucks7_picture.png'

                        self.stucks7_open = Image.open(self.stucks7_picture)

                        self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    else:
                        self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    self.canvas_stucks7.place(x=860,y=310)

        elif 'dia' in l[0]:
            if self.before_card == '.!canvas7':
                try:
                    if self.card_stucks1[self.stucks1_count - 1] == dia_table[self.dia_suit_count]:
                        self.dia_suit[self.dia_suit_count] = self.card_stucks1[self.stucks1_count - 1]
                        self.dia_suit_count += 1
                        self.card_stucks1[self.stucks1_count - 1] = ''
                        self.stucks1_count -= 1
                        self.stucks1_stuck_count -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.dia = 'tramp_picture/' + self.dia_suit[self.dia_suit_count-1] + '.png'
                self.dia_img = tk.PhotoImage(file = self.dia, width=110 , height=155)
                self.canvas_dia.create_image(7,7.5,image=self.dia_img, tags='dia',anchor=tk.NW)
                self.canvas_dia.place(x=680,y=30)

                print(self.card_stucks1)

                if self.stucks1_count == 0:
                    self.stucks1_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                    self.canvas_stucks1.place(x=20,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                    self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                    self.canvas_stucks1.place(x=20,y=310)

            elif self.before_card == '.!canvas8':
                try:
                    if self.card_stucks2[self.stucks2_count - 1] == dia_table[self.dia_suit_count]:
                        self.dia_suit[self.dia_suit_count] = self.card_stucks2[self.stucks2_count - 1]
                        self.dia_suit_count += 1
                        self.card_stucks2[self.stucks2_count - 1] = ''
                        self.stucks2_count -= 1
                        self.stucks2_stuck_count -= 1
                        if self.card_stucks2[self.stucks2_count-1] == '*':
                            self.card_stucks2[self.stucks2_count-1] = self.card_stucks2_seacret[self.card_stucks2_seacret_count]
                            self.card_stucks2_seacret_count += 1
                            self.stucks2_stuck_count += 1
                            self.counter2 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.dia = 'tramp_picture/' + self.dia_suit[self.dia_suit_count-1] + '.png'
                self.dia_img = tk.PhotoImage(file = self.dia, width=110 , height=155)
                self.canvas_dia.create_image(7,7.5,image=self.dia_img, tags='dia',anchor=tk.NW)
                self.canvas_dia.place(x=680,y=30)

                if self.stucks2_count == 0:
                    self.stucks2_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                    self.canvas_stucks2.place(x=160,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter2 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,self.before_card)

                        backside_img = self.chain_backside_picture(self.counter2,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                    
                        self.stucks2_picture = 'create_picture/stucks2_picture.png'

                        self.stucks2_open = Image.open(self.stucks2_picture)

                        self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                    
                    else:
                        self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                    self.canvas_stucks2.place(x=160,y=310)

            elif self.before_card == '.!canvas9':
                try:
                    if self.card_stucks3[self.stucks3_count - 1] == dia_table[self.dia_suit_count]:
                        self.dia_suit[self.dia_suit_count] = self.card_stucks3[self.stucks3_count - 1]
                        self.dia_suit_count += 1
                        self.card_stucks3[self.stucks3_count - 1] = ''
                        self.stucks3_count -= 1
                        self.stucks3_stuck_count -= 1
                        if self.card_stucks3[self.stucks3_count-1] == '*':
                            self.card_stucks3[self.stucks3_count-1] = self.card_stucks3_seacret[self.card_stucks3_seacret_count]
                            self.card_stucks3_seacret_count += 1
                            self.stucks3_stuck_count += 1
                            self.counter3 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.dia = 'tramp_picture/' + self.dia_suit[self.dia_suit_count-1] + '.png'
                self.dia_img = tk.PhotoImage(file = self.dia, width=110 , height=155)
                self.canvas_dia.create_image(7,7.5,image=self.dia_img, tags='dia',anchor=tk.NW)
                self.canvas_dia.place(x=680,y=30)

                if self.stucks3_count == 0:
                    self.stucks3_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                    
                    self.canvas_stucks3.place(x=300,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter3 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter3,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                        
                        self.stucks3_picture = 'create_picture/stucks3_picture.png'

                        self.stucks3_open = Image.open(self.stucks3_picture)

                        self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                    
                    else:
                        self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                    self.canvas_stucks3.place(x=300,y=310)

            elif self.before_card == '.!canvas10':
                try:
                    if self.card_stucks4[self.stucks4_count - 1] == dia_table[self.dia_suit_count]:
                        self.dia_suit[self.dia_suit_count] = self.card_stucks4[self.stucks4_count - 1]
                        self.dia_suit_count += 1
                        self.card_stucks4[self.stucks4_count - 1] = ''
                        self.stucks4_count -= 1
                        self.stucks4_stuck_count -= 1
                        if self.card_stucks4[self.stucks4_count-1] == '*':
                            self.card_stucks4[self.stucks4_count-1] = self.card_stucks4_seacret[self.card_stucks4_seacret_count]
                            self.card_stucks4_seacret_count += 1
                            self.stucks4_stuck_count += 1
                            self.counter4 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.dia = 'tramp_picture/' + self.dia_suit[self.dia_suit_count-1] + '.png'
                self.dia_img = tk.PhotoImage(file = self.dia, width=110 , height=155)
                self.canvas_dia.create_image(7,7.5,image=self.dia_img, tags='dia',anchor=tk.NW)
                self.canvas_dia.place(x=680,y=30)

                if self.stucks4_count == 0:
                    self.stucks4_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                    self.canvas_stucks4.place(x=440,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter4 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter4,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                        
                        self.stucks4_picture = 'create_picture/stucks4_picture.png'

                        self.stucks4_open = Image.open(self.stucks4_picture)

                        self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                    
                    else:
                        self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                    self.canvas_stucks4.place(x=440,y=310)

            elif self.before_card == '.!canvas11':
                try:
                    if self.card_stucks5[self.stucks5_count - 1] == dia_table[self.dia_suit_count]:
                        self.dia_suit[self.dia_suit_count] = self.card_stucks5[self.stucks5_count - 1]
                        self.dia_suit_count += 1
                        self.card_stucks5[self.stucks5_count - 1] = ''
                        self.stucks5_count -= 1
                        self.stucks5_stuck_count -= 1
                        if self.card_stucks5[self.stucks5_count-1] == '*':
                            self.card_stucks5[self.stucks5_count-1] = self.card_stucks5_seacret[self.card_stucks5_seacret_count]
                            self.card_stucks5_seacret_count += 1
                            self.stucks5_stuck_count += 1
                            self.counter5 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.dia = 'tramp_picture/' + self.dia_suit[self.dia_suit_count-1] + '.png'
                self.dia_img = tk.PhotoImage(file = self.dia, width=110 , height=155)
                self.canvas_dia.create_image(7,7.5,image=self.dia_img, tags='dia',anchor=tk.NW)
                self.canvas_dia.place(x=680,y=30)

                if self.stucks5_count == 0:
                    self.stucks5_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                    self.canvas_stucks5.place(x=580,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter5> 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter5,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                        
                        self.stucks5_picture = 'create_picture/stucks5_picture.png'

                        self.stucks5_open = Image.open(self.stucks5_picture)

                        self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                    
                    else:
                        self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                    self.canvas_stucks5.place(x=580,y=310)


            elif self.before_card == '.!canvas12':
                try:
                    if self.card_stucks6[self.stucks6_count - 1] == dia_table[self.dia_suit_count]:
                        self.dia_suit[self.dia_suit_count] = self.card_stucks6[self.stucks6_count - 1]
                        self.dia_suit_count += 1
                        self.card_stucks6[self.stucks6_count - 1] = ''
                        self.stucks6_count -= 1
                        self.stucks6_stuck_count -= 1
                        if self.card_stucks6[self.stucks6_count-1] == '*':
                            self.card_stucks6[self.stucks6_count-1] = self.card_stucks6_seacret[self.card_stucks6_seacret_count]
                            self.card_stucks6_seacret_count += 1
                            self.stucks6_stuck_count += 1
                            self.counter6 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.dia = 'tramp_picture/' + self.dia_suit[self.dia_suit_count-1] + '.png'
                self.dia_img = tk.PhotoImage(file = self.dia, width=110 , height=155)
                self.canvas_dia.create_image(7,7.5,image=self.dia_img, tags='dia',anchor=tk.NW)
                self.canvas_dia.place(x=680,y=30)

                if self.stucks6_count == 0:
                    self.stucks6_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    self.canvas_stucks6.place(x=720,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter6 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter6,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                        
                        self.stucks6_picture = 'create_picture/stucks6_picture.png'

                        self.stucks6_open = Image.open(self.stucks6_picture)

                        self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    else:
                        self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    self.canvas_stucks6.place(x=720,y=310)

            elif self.before_card == '.!canvas13':
                try:
                    if self.card_stucks7[self.stucks7_count - 1] == dia_table[self.dia_suit_count]:
                        self.dia_suit[self.dia_suit_count] = self.card_stucks7[self.stucks7_count - 1]
                        self.dia_suit_count += 1
                        self.card_stucks7[self.stucks7_count - 1] = ''
                        self.stucks7_count -= 1
                        self.stucks7_stuck_count -= 1
                        if self.card_stucks7[self.stucks7_count-1] == '*':
                            self.card_stucks7[self.stucks7_count-1] = self.card_stucks7_seacret[self.card_stucks7_seacret_count]
                            self.card_stucks7_seacret_count += 1
                            self.stucks7_stuck_count += 1
                            self.counter7 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.dia = 'tramp_picture/' + self.dia_suit[self.dia_suit_count-1] + '.png'
                self.dia_img = tk.PhotoImage(file = self.dia, width=110 , height=155)
                self.canvas_dia.create_image(7,7.5,image=self.dia_img, tags='dia',anchor=tk.NW)
                self.canvas_dia.place(x=680,y=30)

                if self.stucks7_count == 0:
                    self.stucks7_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    self.canvas_stucks7.place(x=860,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter7:
                        openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter7,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                        
                        self.stucks7_picture = 'create_picture/stucks7_picture.png'

                        self.stucks7_open = Image.open(self.stucks7_picture)

                        self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    else:
                        self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    self.canvas_stucks7.place(x=860,y=310)

        elif 'club' in l[0]:
            if self.before_card == '.!canvas7':
                try:
                    if self.card_stucks1[self.stucks1_count - 1] == club_table[self.club_suit_count]:
                        self.club_suit[self.club_suit_count] = self.card_stucks1[self.stucks1_count - 1]
                        self.club_suit_count += 1
                        self.card_stucks1[self.stucks1_count - 1] = ''
                        self.stucks1_count -= 1
                        self.stucks1_stuck_count -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.club = 'tramp_picture/' + self.club_suit[self.club_suit_count-1] + '.png'
                self.club_img = tk.PhotoImage(file = self.club, width=110 , height=155)
                self.canvas_club.create_image(7,7.5,image=self.club_img, tags='club',anchor=tk.NW)
                self.canvas_club.place(x=820,y=30)

                print(self.card_stucks1)

                if self.stucks1_count == 0:
                    self.stucks1_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                    self.canvas_stucks1.place(x=20,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                    self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                    self.canvas_stucks1.place(x=20,y=310)

            elif self.before_card == '.!canvas8':
                try:
                    if self.card_stucks2[self.stucks2_count - 1] == club_table[self.club_suit_count]:
                        self.club_suit[self.club_suit_count] = self.card_stucks2[self.stucks2_count - 1]
                        self.club_suit_count += 1
                        self.card_stucks2[self.stucks2_count - 1] = ''
                        self.stucks2_count -= 1
                        self.stucks2_stuck_count -= 1
                        if self.card_stucks2[self.stucks2_count-1] == '*':
                            self.card_stucks2[self.stucks2_count-1] = self.card_stucks2_seacret[self.card_stucks2_seacret_count]
                            self.card_stucks2_seacret_count += 1
                            self.stucks2_stuck_count += 1
                            self.counter2 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.club = 'tramp_picture/' + self.club_suit[self.club_suit_count-1] + '.png'
                self.club_img = tk.PhotoImage(file = self.club, width=110 , height=155)
                self.canvas_club.create_image(7,7.5,image=self.club_img, tags='club',anchor=tk.NW)
                self.canvas_club.place(x=820,y=30)

                if self.stucks2_count == 0:
                    self.stucks2_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                    self.canvas_stucks2.place(x=160,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter2 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,self.before_card)

                        backside_img = self.chain_backside_picture(self.counter2,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                    
                        self.stucks2_picture = 'create_picture/stucks2_picture.png'

                        self.stucks2_open = Image.open(self.stucks2_picture)

                        self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                    
                    else:
                        self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                    self.canvas_stucks2.place(x=160,y=310)

            elif self.before_card == '.!canvas9':
                try:
                    if self.card_stucks3[self.stucks3_count - 1] == club_table[self.club_suit_count]:
                        self.club_suit[self.club_suit_count] = self.card_stucks3[self.stucks3_count - 1]
                        self.club_suit_count += 1
                        self.card_stucks3[self.stucks3_count - 1] = ''
                        self.stucks3_count -= 1
                        self.stucks3_stuck_count -= 1
                        if self.card_stucks3[self.stucks3_count-1] == '*':
                            self.card_stucks3[self.stucks3_count-1] = self.card_stucks3_seacret[self.card_stucks3_seacret_count]
                            self.card_stucks3_seacret_count += 1
                            self.stucks3_stuck_count += 1
                            self.counter3 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.club = 'tramp_picture/' + self.club_suit[self.club_suit_count-1] + '.png'
                self.club_img = tk.PhotoImage(file = self.club, width=110 , height=155)
                self.canvas_club.create_image(7,7.5,image=self.club_img, tags='club',anchor=tk.NW)
                self.canvas_club.place(x=820,y=30)

                if self.stucks3_count == 0:
                    self.stucks3_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                    
                    self.canvas_stucks3.place(x=300,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter3 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter3,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                        
                        self.stucks3_picture = 'create_picture/stucks3_picture.png'

                        self.stucks3_open = Image.open(self.stucks3_picture)

                        self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                    
                    else:
                        self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                    self.canvas_stucks3.place(x=300,y=310)

            elif self.before_card == '.!canvas10':
                try:
                    if self.card_stucks4[self.stucks4_count - 1] == club_table[self.club_suit_count]:
                        self.club_suit[self.club_suit_count] = self.card_stucks4[self.stucks4_count - 1]
                        self.club_suit_count += 1
                        self.card_stucks4[self.stucks4_count - 1] = ''
                        self.stucks4_count -= 1
                        self.stucks4_stuck_count -= 1
                        if self.card_stucks4[self.stucks4_count-1] == '*':
                            self.card_stucks4[self.stucks4_count-1] = self.card_stucks4_seacret[self.card_stucks4_seacret_count]
                            self.card_stucks4_seacret_count += 1
                            self.stucks4_stuck_count += 1
                            self.counter4 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.club = 'tramp_picture/' + self.club_suit[self.club_suit_count-1] + '.png'
                self.club_img = tk.PhotoImage(file = self.club, width=110 , height=155)
                self.canvas_club.create_image(7,7.5,image=self.club_img, tags='club',anchor=tk.NW)
                self.canvas_club.place(x=820,y=30)

                if self.stucks4_count == 0:
                    self.stucks4_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                    self.canvas_stucks4.place(x=440,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter4 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter4,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                        
                        self.stucks4_picture = 'create_picture/stucks4_picture.png'

                        self.stucks4_open = Image.open(self.stucks4_picture)

                        self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                    
                    else:
                        self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                    self.canvas_stucks4.place(x=440,y=310)

            elif self.before_card == '.!canvas11':
                try:
                    if self.card_stucks5[self.stucks5_count - 1] == club_table[self.club_suit_count]:
                        self.club_suit[self.club_suit_count] = self.card_stucks5[self.stucks5_count - 1]
                        self.club_suit_count += 1
                        self.card_stucks5[self.stucks5_count - 1] = ''
                        self.stucks5_count -= 1
                        self.stucks5_stuck_count -= 1
                        if self.card_stucks5[self.stucks5_count-1] == '*':
                            self.card_stucks5[self.stucks5_count-1] = self.card_stucks5_seacret[self.card_stucks5_seacret_count]
                            self.card_stucks5_seacret_count += 1
                            self.stucks5_stuck_count += 1
                            self.counter5 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.club = 'tramp_picture/' + self.club_suit[self.club_suit_count-1] + '.png'
                self.club_img = tk.PhotoImage(file = self.club, width=110 , height=155)
                self.canvas_club.create_image(7,7.5,image=self.club_img, tags='club',anchor=tk.NW)
                self.canvas_club.place(x=820,y=30)

                if self.stucks5_count == 0:
                    self.stucks5_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                    self.canvas_stucks5.place(x=580,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter5> 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter5,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                        
                        self.stucks5_picture = 'create_picture/stucks5_picture.png'

                        self.stucks5_open = Image.open(self.stucks5_picture)

                        self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                    
                    else:
                        self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                    self.canvas_stucks5.place(x=580,y=310)


            elif self.before_card == '.!canvas12':
                try:
                    if self.card_stucks6[self.stucks6_count - 1] == club_table[self.club_suit_count]:
                        self.club_suit[self.club_suit_count] = self.card_stucks6[self.stucks6_count - 1]
                        self.club_suit_count += 1
                        self.card_stucks6[self.stucks6_count - 1] = ''
                        self.stucks6_count -= 1
                        self.stucks6_stuck_count -= 1
                        if self.card_stucks6[self.stucks6_count-1] == '*':
                            self.card_stucks6[self.stucks6_count-1] = self.card_stucks6_seacret[self.card_stucks6_seacret_count]
                            self.card_stucks6_seacret_count += 1
                            self.stucks6_stuck_count += 1
                            self.counter6 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.club = 'tramp_picture/' + self.club_suit[self.club_suit_count-1] + '.png'
                self.club_img = tk.PhotoImage(file = self.club, width=110 , height=155)
                self.canvas_club.create_image(7,7.5,image=self.club_img, tags='club',anchor=tk.NW)
                self.canvas_club.place(x=820,y=30)

                if self.stucks6_count == 0:
                    self.stucks6_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    self.canvas_stucks6.place(x=720,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter6 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter6,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                        
                        self.stucks6_picture = 'create_picture/stucks6_picture.png'

                        self.stucks6_open = Image.open(self.stucks6_picture)

                        self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    else:
                        self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    self.canvas_stucks6.place(x=720,y=310)

            elif self.before_card == '.!canvas13':
                try:
                    if self.card_stucks7[self.stucks7_count - 1] == club_table[self.club_suit_count]:
                        self.club_suit[self.club_suit_count] = self.card_stucks7[self.stucks7_count - 1]
                        self.club_suit_count += 1
                        self.card_stucks7[self.stucks7_count - 1] = ''
                        self.stucks7_count -= 1
                        self.stucks7_stuck_count -= 1
                        if self.card_stucks7[self.stucks7_count-1] == '*':
                            self.card_stucks7[self.stucks7_count-1] = self.card_stucks7_seacret[self.card_stucks7_seacret_count]
                            self.card_stucks7_seacret_count += 1
                            self.stucks7_stuck_count += 1
                            self.counter7 -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        return
                except IndexError:
                    print('カードを移動できませんでした\n')
                    return
                
                self.club = 'tramp_picture/' + self.club_suit[self.club_suit_count-1] + '.png'
                self.club_img = tk.PhotoImage(file = self.club, width=110 , height=155)
                self.canvas_club.create_image(7,7.5,image=self.club_img, tags='club',anchor=tk.NW)
                self.canvas_club.place(x=820,y=30)

                if self.stucks7_count == 0:
                    self.stucks7_img = tk.PhotoImage(file = 'tramp_picture/start.png',width=120,height=170)

                    self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    self.canvas_stucks7.place(x=860,y=310)
                    #受付の解除
                    self.canvas_arrow_stuck_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    if self.counter7:
                        openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,self.before_card)
                                                                
                        backside_img = self.chain_backside_picture(self.counter7,self.before_card)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                        
                        self.stucks7_picture = 'create_picture/stucks7_picture.png'

                        self.stucks7_open = Image.open(self.stucks7_picture)

                        self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    else:
                        self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    self.canvas_stucks7.place(x=860,y=310)

        if self.spade_suit[12] == '♠K' and self.hurt_suit[12] == '♥K' and self.dia_suit[12] == '♦K' and self.club_suit[12] == '♣K':
            sub_window = tk.Toplevel()
            sub_window.title('おめでとうございます！')
            sub_window.geometry("300x150+750+450")
            sub_window['bg'] = 'white'
            message = tk.Label(sub_window,text='ゲームクリア！',font=("MSゴシック","20","bold"),bg='white')
            message.place(x=60,y=50)
        
        #受付の解除
        self.canvas_arrow_stuck_img = None

        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

        self.canvas_club.tag_unbind('club','<ButtonPress>')

        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

        #再受付
        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

    def move_suitcard_to_stucks(self,master,event ):
        print("場札：" ,"\n","場札1",self.card_stucks1,"\n","場札2",self.card_stucks2,"\n","場札3",self.card_stucks3,"\n","場札4",self.card_stucks4,"\n","場札5",self.card_stucks5,"\n","場札6",self.card_stucks6,"\n","場札7",self.card_stucks7,"\n")
        print(event.widget)
        print('before_card:' + str(self.before_card))
        if str(event.widget) == '.!canvas7':
            x,y = self.canvas_spade.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_stucks1.itemcget(obj, 'tags') for obj in self.canvas_stucks1.find_overlapping(x,y,x,y)]

        elif str(event.widget) == '.!canvas8':
            x,y = self.canvas_hurt.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_stucks2.itemcget(obj, 'tags') for obj in self.canvas_stucks2.find_overlapping(x,y,x,y)]

        elif str(event.widget) == '.!canvas9':
            x,y = self.canvas_dia.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_stucks3.itemcget(obj, 'tags') for obj in self.canvas_stucks3.find_overlapping(x,y,x,y)]

        elif str(event.widget) == '.!canvas10':
            x,y = self.canvas_club.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_stucks4.itemcget(obj, 'tags') for obj in self.canvas_stucks4.find_overlapping(x,y,x,y)]

        elif str(event.widget) == '.!canvas11':
            x,y = self.canvas_club.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_stucks5.itemcget(obj, 'tags') for obj in self.canvas_stucks5.find_overlapping(x,y,x,y)]
        
        elif str(event.widget) == '.!canvas12':
            x,y = self.canvas_club.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_stucks6.itemcget(obj, 'tags') for obj in self.canvas_stucks6.find_overlapping(x,y,x,y)]
            
        elif str(event.widget) == '.!canvas13':
            x,y = self.canvas_club.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_stucks7.itemcget(obj, 'tags') for obj in self.canvas_stucks7.find_overlapping(x,y,x,y)]

        print(l)

        if 'stucks1' in l[0]:
            if self.before_card == '.!canvas3':
                try:
                    if self.card_stucks1[self.stucks1_count-1].startswith('♠') or self.card_stucks1[self.stucks1_count-1].startswith('♣'):
                        return
                    else:
                        if self.card_stucks1[self.stucks1_count-1].startswith('♥'):
                            stuck_table = hurt_table

                        elif self.card_stucks1[self.stucks1_count-1].startswith('♦'):
                            stuck_table = dia_table

                        if self.spade_suit[self.spade_suit_count-1] == spade_table[stuck_table.index(self.card_stucks1[self.stucks1_count-1])-1]:
                            self.card_stucks1[self.stucks1_count] = self.spade_suit[self.spade_suit_count-1]
                            self.stucks1_count += 1
                            self.stucks1_stuck_count += 1
                            self.spade_suit[self.spade_suit_count-1] = ''
                            self.spade_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                self.canvas_stucks1.place(x=20,y=310)

                print(self.card_stucks1)

                if self.spade_suit_count == 0:
                    self.spade_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_spade.place(x=400,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.spade = 'tramp_picture/' + self.spade_suit[self.spade_suit_count-1] + '.png'

                    self.spade_img = tk.PhotoImage(file = self.spade, width=110 , height=155)

                    self.canvas_spade.create_image(7,7.5,image=self.spade_img, tags='spade',anchor=tk.NW)

                    self.canvas_spade.place(x=400,y=30)


            if self.before_card == '.!canvas4':
                try:
                    if self.card_stucks1[self.stucks1_count-1].startswith('♥') or self.card_stucks1[self.stucks1_count-1].startswith('♦'):
                        return
                    
                    else:
                        if self.card_stucks1[self.stucks1_count-1].startswith('♠'):
                            stuck_table = spade_table

                        elif self.card_stucks1[self.stucks1_count-1].startswith('♣'):
                            stuck_table = club_table

                        if self.hurt_suit[self.hurt_suit_count-1] == hurt_table[stuck_table.index(self.card_stucks1[self.stucks1_count-1])-1]:
                            self.card_stucks1[self.stucks1_count] = self.hurt_suit[self.hurt_suit_count-1]
                            self.stucks1_count += 1
                            self.stucks1_stuck_count += 1
                            self.hurt_suit[self.hurt_suit_count-1] = ''
                            self.hurt_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                self.canvas_stucks1.place(x=20,y=310)

                print(self.card_stucks1)

                if self.hurt_suit_count == 0:
                    self.hurt_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_hurt.place(x=540,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.hurt = 'tramp_picture/' + self.hurt_suit[self.hurt_suit_count-1] + '.png'

                    self.hurt_img = tk.PhotoImage(file = self.hurt, width=110 , height=155)

                    self.canvas_hurt.create_image(7,7.5,image=self.hurt_img, tags='hurt',anchor=tk.NW)

                    self.canvas_hurt.place(x=540,y=30)
            
            if self.before_card == '.!canvas5':
                try:
                    if self.card_stucks1[self.stucks1_count-1].startswith('♦') or self.card_stucks1[self.stucks1_count-1].startswith('♥'):
                        return

                    else:
                        if self.card_stucks1[self.stucks1_count-1].startswith('♠'):
                            stuck_table = spade_table

                        elif self.card_stucks1[self.stucks1_count-1].startswith('♣'):
                            stuck_table = club_table

                        if self.dia_suit[self.dia_suit_count-1] == dia_table[stuck_table.index(self.card_stucks1[self.stucks1_count-1])-1]:
                            self.card_stucks1[self.stucks1_count] = self.dia_suit[self.dia_suit_count-1]
                            self.stucks1_count += 1
                            self.stucks1_stuck_count += 1
                            self.dia_suit[self.dia_suit_count-1] = ''
                            self.dia_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                self.canvas_stucks1.place(x=20,y=310)

                print(self.card_stucks1)

                if self.dia_suit_count == 0:
                    self.dia_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_dia.place(x=680,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.dia = 'tramp_picture/' + self.dia_suit[self.dia_suit_count-1] + '.png'

                    self.dia_img = tk.PhotoImage(file = self.dia, width=110 , height=155)

                    self.canvas_dia.create_image(7,7.5,image=self.dia_img, tags='dia',anchor=tk.NW)

                    self.canvas_dia.place(x=680,y=30)

            if self.before_card == '.!canvas6':
                try:
                    if self.card_stucks1[self.stucks1_count-1].startswith('♣') or self.card_stucks1[self.stucks1_count-1].startswith('♠'):
                        return
                        
                    else:    
                        if self.card_stucks1[self.stucks1_count-1].startswith('♥'):
                            stuck_table = hurt_table

                        elif self.card_stucks1[self.stucks1_count-1].startswith('♦'):
                            stuck_table = dia_table

                        if self.club_suit[self.club_suit_count-1] == club_table[stuck_table.index(self.card_stucks1[self.stucks1_count-1])-1]:
                            self.card_stucks1[self.stucks1_count] = self.club_suit[self.club_suit_count-1]
                            self.stucks1_count += 1
                            self.stucks1_stuck_count += 1
                            self.club_suit[self.club_suit_count-1] = ''
                            self.club_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                self.canvas_stucks1.place(x=20,y=310)

                print(self.card_stucks1)

                if self.club_suit_count == 0:
                    self.club_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_club.place(x=820,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.club = 'tramp_picture/' + self.club_suit[self.club_suit_count-1] + '.png'

                    self.club_img = tk.PhotoImage(file = self.club, width=110 , height=155)

                    self.canvas_club.create_image(7,7.5,image=self.club_img, tags='club',anchor=tk.NW)

                    self.canvas_club.place(x=820,y=30)

        if 'stucks2' in l[0]:
            if self.before_card == '.!canvas3':
                try:
                    if self.card_stucks2[self.stucks2_count-1].startswith('♠') or self.card_stucks2[self.stucks2_count-1].startswith('♣'):
                        return
                    else:
                        if self.card_stucks2[self.stucks2_count-1].startswith('♥'):
                            stuck_table = hurt_table

                        elif self.card_stucks2[self.stucks2_count-1].startswith('♦'):
                            stuck_table = dia_table

                        if self.spade_suit[self.spade_suit_count-1] == spade_table[stuck_table.index(self.card_stucks2[self.stucks2_count-1])-1]:
                            self.card_stucks2[self.stucks2_count] = self.spade_suit[self.spade_suit_count-1]
                            self.stucks2_count += 1
                            self.stucks2_stuck_count += 1
                            self.spade_suit[self.spade_suit_count-1] = ''
                            self.spade_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter2 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,event)

                    backside_img = self.chain_backside_picture(self.counter2,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                
                    self.stucks2_picture = 'create_picture/stucks2_picture.png'

                    self.stucks2_open = Image.open(self.stucks2_picture)

                    self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                    self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                    
                else:
                    self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                    self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                self.canvas_stucks2.place(x=160,y=310)

                print(self.card_stucks2)

                if self.spade_suit_count == 0:
                    self.spade_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_spade.place(x=400,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.spade = 'tramp_picture/' + self.spade_suit[self.spade_suit_count-1] + '.png'

                    self.spade_img = tk.PhotoImage(file = self.spade, width=110 , height=155)

                    self.canvas_spade.create_image(7,7.5,image=self.spade_img, tags='spade',anchor=tk.NW)

                    self.canvas_spade.place(x=400,y=30)


            if self.before_card == '.!canvas4':
                try:
                    if self.card_stucks2[self.stucks2_count-1].startswith('♥') or self.card_stucks2[self.stucks2_count-1].startswith('♦'):
                        return
                    
                    else:
                        if self.card_stucks2[self.stucks2_count-1].startswith('♠'):
                            stuck_table = spade_table

                        elif self.card_stucks2[self.stucks2_count-1].startswith('♣'):
                            stuck_table = club_table

                        if self.hurt_suit[self.hurt_suit_count-1] == hurt_table[stuck_table.index(self.card_stucks2[self.stucks2_count-1])-1]:
                            self.card_stucks2[self.stucks2_count] = self.hurt_suit[self.hurt_suit_count-1]
                            self.stucks2_count += 1
                            self.stucks2_stuck_count += 1
                            self.hurt_suit[self.hurt_suit_count-1] = ''
                            self.hurt_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter2 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,event)

                    backside_img = self.chain_backside_picture(self.counter2,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                
                    self.stucks2_picture = 'create_picture/stucks2_picture.png'

                    self.stucks2_open = Image.open(self.stucks2_picture)

                    self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                    self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                    
                else:
                    self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                    self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                self.canvas_stucks2.place(x=160,y=310)

                print(self.card_stucks2)

                if self.hurt_suit_count == 0:
                    self.hurt_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_hurt.place(x=540,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.hurt = 'tramp_picture/' + self.hurt_suit[self.hurt_suit_count-1] + '.png'

                    self.hurt_img = tk.PhotoImage(file = self.hurt, width=110 , height=155)

                    self.canvas_hurt.create_image(7,7.5,image=self.hurt_img, tags='hurt',anchor=tk.NW)

                    self.canvas_hurt.place(x=540,y=30)
            
            if self.before_card == '.!canvas5':
                try:
                    if self.card_stucks2[self.stucks2_count-1].startswith('♦') or self.card_stucks2[self.stucks2_count-1].startswith('♥'):
                        return

                    else:
                        if self.card_stucks2[self.stucks2_count-1].startswith('♠'):
                            stuck_table = spade_table

                        elif self.card_stucks2[self.stucks2_count-1].startswith('♣'):
                            stuck_table = club_table

                        if self.dia_suit[self.dia_suit_count-1] == dia_table[stuck_table.index(self.card_stucks2[self.stucks2_count-1])-1]:
                            self.card_stucks2[self.stucks2_count] = self.dia_suit[self.dia_suit_count-1]
                            self.stucks2_count += 1
                            self.stucks2_stuck_count += 1
                            self.dia_suit[self.dia_suit_count-1] = ''
                            self.dia_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter2 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,event)

                    backside_img = self.chain_backside_picture(self.counter2,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                
                    self.stucks2_picture = 'create_picture/stucks2_picture.png'

                    self.stucks2_open = Image.open(self.stucks2_picture)

                    self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                    self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                    
                else:
                    self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                    self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                self.canvas_stucks2.place(x=160,y=310)

                print(self.card_stucks2)

                if self.dia_suit_count == 0:
                    self.dia_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_dia.place(x=680,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.dia = 'tramp_picture/' + self.dia_suit[self.dia_suit_count-1] + '.png'

                    self.dia_img = tk.PhotoImage(file = self.dia, width=110 , height=155)

                    self.canvas_dia.create_image(7,7.5,image=self.dia_img, tags='dia',anchor=tk.NW)

                    self.canvas_dia.place(x=680,y=30)

            if self.before_card == '.!canvas6':
                try:
                    if self.card_stucks2[self.stucks2_count-1].startswith('♣') or self.card_stucks2[self.stucks2_count-1].startswith('♠'):
                        return
                    
                    else:
                        if self.card_stucks2[self.stucks2_count-1].startswith('♥'):
                            stuck_table = hurt_table

                        elif self.card_stucks2[self.stucks2_count-1].startswith('♦'):
                            stuck_table = dia_table

                        if self.club_suit[self.club_suit_count-1] == club_table[stuck_table.index(self.card_stucks2[self.stucks2_count-1])-1]:
                            self.card_stucks2[self.stucks2_count] = self.club_suit[self.club_suit_count-1]
                            self.stucks2_count += 1
                            self.stucks2_stuck_count += 1
                            self.club_suit[self.club_suit_count-1] = ''
                            self.club_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter2 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,event)

                    backside_img = self.chain_backside_picture(self.counter2,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                
                    self.stucks2_picture = 'create_picture/stucks2_picture.png'

                    self.stucks2_open = Image.open(self.stucks2_picture)

                    self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                    self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                    
                else:
                    self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                    self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                self.canvas_stucks2.place(x=160,y=310)

                print(self.card_stucks2)

                if self.club_suit_count == 0:
                    self.club_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_club.place(x=820,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.club = 'tramp_picture/' + self.club_suit[self.club_suit_count-1] + '.png'

                    self.club_img = tk.PhotoImage(file = self.club, width=110 , height=155)

                    self.canvas_club.create_image(7,7.5,image=self.club_img, tags='club',anchor=tk.NW)

                    self.canvas_club.place(x=820,y=30)

        if 'stucks3' in l[0]:
            if self.before_card == '.!canvas3':
                try:
                    if self.card_stucks3[self.stucks3_count-1].startswith('♠') or self.card_stucks3[self.stucks3_count-1].startswith('♣'):
                        return
                    else:
                        if self.card_stucks3[self.stucks3_count-1].startswith('♥'):
                            stuck_table = hurt_table

                        elif self.card_stucks3[self.stucks3_count-1].startswith('♦'):
                            stuck_table = dia_table

                        if self.spade_suit[self.spade_suit_count-1] == spade_table[stuck_table.index(self.card_stucks3[self.stucks3_count-1])-1]:
                            self.card_stucks3[self.stucks3_count] = self.spade_suit[self.spade_suit_count-1]
                            self.stucks3_count += 1
                            self.stucks3_stuck_count += 1
                            self.spade_suit[self.spade_suit_count-1] = ''
                            self.spade_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter3 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter3,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                    
                    self.stucks3_picture = 'create_picture/stucks3_picture.png'

                    self.stucks3_open = Image.open(self.stucks3_picture)

                    self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                    self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                
                else:
                    self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                    self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                self.canvas_stucks3.place(x=300,y=310)

                print(self.card_stucks3)

                if self.spade_suit_count == 0:
                    self.spade_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_spade.place(x=400,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.spade = 'tramp_picture/' + self.spade_suit[self.spade_suit_count-1] + '.png'

                    self.spade_img = tk.PhotoImage(file = self.spade, width=110 , height=155)

                    self.canvas_spade.create_image(7,7.5,image=self.spade_img, tags='spade',anchor=tk.NW)

                    self.canvas_spade.place(x=400,y=30)


            if self.before_card == '.!canvas4':
                try:
                    if self.card_stucks3[self.stucks3_count-1].startswith('♥') or self.card_stucks3[self.stucks3_count-1].startswith('♦'):
                        return
                    
                    else:
                        if self.card_stucks3[self.stucks3_count-1].startswith('♠'):
                            stuck_table = spade_table

                        elif self.card_stucks3[self.stucks3_count-1].startswith('♣'):
                            stuck_table = club_table

                        if self.hurt_suit[self.hurt_suit_count-1] == hurt_table[stuck_table.index(self.card_stucks3[self.stucks3_count-1])-1]:
                            self.card_stucks3[self.stucks3_count] = self.hurt_suit[self.hurt_suit_count-1]
                            self.stucks3_count += 1
                            self.stucks3_stuck_count += 1
                            self.hurt_suit[self.hurt_suit_count-1] = ''
                            self.hurt_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter3 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter3,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                    
                    self.stucks3_picture = 'create_picture/stucks3_picture.png'

                    self.stucks3_open = Image.open(self.stucks3_picture)

                    self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                    self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                    
                else:
                    self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                    self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                self.canvas_stucks3.place(x=300,y=310)

                print(self.card_stucks3)

                if self.hurt_suit_count == 0:
                    self.hurt_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_hurt.place(x=540,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.hurt = 'tramp_picture/' + self.hurt_suit[self.hurt_suit_count-1] + '.png'

                    self.hurt_img = tk.PhotoImage(file = self.hurt, width=110 , height=155)

                    self.canvas_hurt.create_image(7,7.5,image=self.hurt_img, tags='hurt',anchor=tk.NW)

                    self.canvas_hurt.place(x=540,y=30)
            
            if self.before_card == '.!canvas5':
                try:
                    if self.card_stucks3[self.stucks3_count-1].startswith('♦') or self.card_stucks3[self.stucks3_count-1].startswith('♥'):
                        return

                    else:
                        if self.card_stucks3[self.stucks3_count-1].startswith('♠'):
                            stuck_table = spade_table

                        elif self.card_stucks3[self.stucks3_count-1].startswith('♣'):
                            stuck_table = club_table

                        if self.dia_suit[self.dia_suit_count-1] == dia_table[stuck_table.index(self.card_stucks3[self.stucks3_count-1])-1]:
                            self.card_stucks3[self.stucks3_count] = self.dia_suit[self.dia_suit_count-1]
                            self.stucks3_count += 1
                            self.stucks3_stuck_count += 1
                            self.dia_suit[self.dia_suit_count-1] = ''
                            self.dia_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter3 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter3,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                    
                    self.stucks3_picture = 'create_picture/stucks3_picture.png'

                    self.stucks3_open = Image.open(self.stucks3_picture)

                    self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                    self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                
                else:
                    self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                    self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                self.canvas_stucks3.place(x=300,y=310)

                print(self.card_stucks3)

                if self.dia_suit_count == 0:
                    self.dia_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_dia.place(x=680,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.dia = 'tramp_picture/' + self.dia_suit[self.dia_suit_count-1] + '.png'

                    self.dia_img = tk.PhotoImage(file = self.dia, width=110 , height=155)

                    self.canvas_dia.create_image(7,7.5,image=self.dia_img, tags='dia',anchor=tk.NW)

                    self.canvas_dia.place(x=680,y=30)

            if self.before_card == '.!canvas6':
                try:
                    if self.card_stucks3[self.stucks3_count-1].startswith('♣') or self.card_stucks3[self.stucks3_count-1].startswith('♠'):
                        return
                    
                    else:
                        if self.card_stucks3[self.stucks3_count-1].startswith('♥'):
                            stuck_table = hurt_table

                        elif self.card_stucks3[self.stucks3_count-1].startswith('♦'):
                            stuck_table = dia_table

                        if self.club_suit[self.club_suit_count-1] == club_table[stuck_table.index(self.card_stucks3[self.stucks3_count-1])-1]:
                            self.card_stucks3[self.stucks3_count] = self.club_suit[self.club_suit_count-1]
                            self.stucks3_count += 1
                            self.stucks3_stuck_count += 1
                            self.club_suit[self.club_suit_count-1] = ''
                            self.club_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter3 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter3,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                    
                    self.stucks3_picture = 'create_picture/stucks3_picture.png'

                    self.stucks3_open = Image.open(self.stucks3_picture)

                    self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                    self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                
                else:
                    self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                    self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                self.canvas_stucks3.place(x=300,y=310)

                print(self.card_stucks3)

                if self.club_suit_count == 0:
                    self.club_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_club.place(x=820,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.club = 'tramp_picture/' + self.club_suit[self.club_suit_count-1] + '.png'

                    self.club_img = tk.PhotoImage(file = self.club, width=110 , height=155)

                    self.canvas_club.create_image(7,7.5,image=self.club_img, tags='club',anchor=tk.NW)

                    self.canvas_club.place(x=820,y=30)

        if 'stucks4' in l[0]:
            if self.before_card == '.!canvas3':
                try:
                    if self.card_stucks4[self.stucks4_count-1].startswith('♠') or self.card_stucks4[self.stucks4_count-1].startswith('♣'):
                        return
                    else:
                        if self.card_stucks4[self.stucks4_count-1].startswith('♥'):
                            stuck_table = hurt_table

                        elif self.card_stucks4[self.stucks4_count-1].startswith('♦'):
                            stuck_table = dia_table

                        if self.spade_suit[self.spade_suit_count-1] == spade_table[stuck_table.index(self.card_stucks4[self.stucks4_count-1])-1]:
                            self.card_stucks4[self.stucks4_count] = self.spade_suit[self.spade_suit_count-1]
                            self.stucks4_count += 1
                            self.stucks4_stuck_count += 1
                            self.spade_suit[self.spade_suit_count-1] = ''
                            self.spade_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter4 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter4,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                    
                    self.stucks4_picture = 'create_picture/stucks4_picture.png'

                    self.stucks4_open = Image.open(self.stucks4_picture)

                    self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                    self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                
                else:
                    self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                    self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                self.canvas_stucks4.place(x=440,y=310)

                if self.spade_suit_count == 0:
                    self.spade_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_spade.place(x=400,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.spade = 'tramp_picture/' + self.spade_suit[self.spade_suit_count-1] + '.png'

                    self.spade_img = tk.PhotoImage(file = self.spade, width=110 , height=155)

                    self.canvas_spade.create_image(7,7.5,image=self.spade_img, tags='spade',anchor=tk.NW)

                    self.canvas_spade.place(x=400,y=30)


            if self.before_card == '.!canvas4':
                try:
                    if self.card_stucks4[self.stucks4_count-1].startswith('♥') or self.card_stucks4[self.stucks4_count-1].startswith('♦'):
                        return
                    
                    else:
                        if self.card_stucks4[self.stucks4_count-1].startswith('♠'):
                            stuck_table = spade_table

                        elif self.card_stucks4[self.stucks4_count-1].startswith('♣'):
                            stuck_table = club_table

                        if self.hurt_suit[self.hurt_suit_count-1] == hurt_table[stuck_table.index(self.card_stucks4[self.stucks4_count-1])-1]:
                            self.card_stucks4[self.stucks4_count] = self.hurt_suit[self.hurt_suit_count-1]
                            self.stucks4_count += 1
                            self.stucks4_stuck_count += 1
                            self.hurt_suit[self.hurt_suit_count-1] = ''
                            self.hurt_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter4 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter4,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                    
                    self.stucks4_picture = 'create_picture/stucks4_picture.png'

                    self.stucks4_open = Image.open(self.stucks4_picture)

                    self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                    self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                
                else:
                    self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                    self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                self.canvas_stucks4.place(x=440,y=310)

                if self.hurt_suit_count == 0:
                    self.hurt_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_hurt.place(x=540,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.hurt = 'tramp_picture/' + self.hurt_suit[self.hurt_suit_count-1] + '.png'

                    self.hurt_img = tk.PhotoImage(file = self.hurt, width=110 , height=155)

                    self.canvas_hurt.create_image(7,7.5,image=self.hurt_img, tags='hurt',anchor=tk.NW)

                    self.canvas_hurt.place(x=540,y=30)
            
            if self.before_card == '.!canvas5':
                try:
                    if self.card_stucks4[self.stucks4_count-1].startswith('♦') or self.card_stucks4[self.stucks4_count-1].startswith('♥'):
                        return

                    else:
                        if self.card_stucks4[self.stucks4_count-1].startswith('♠'):
                            stuck_table = spade_table
                        
                        elif self.card_stucks4[self.stucks4_count-1].startswith('♣'):
                            stuck_table = club_table

                        if self.dia_suit[self.dia_suit_count-1] == dia_table[stuck_table.index(self.card_stucks4[self.stucks4_count-1])-1]:
                            self.card_stucks4[self.stucks4_count] = self.dia_suit[self.dia_suit_count-1]
                            self.stucks4_count += 1
                            self.stucks4_stuck_count += 1
                            self.dia_suit[self.dia_suit_count-1] = ''
                            self.dia_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter4 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter4,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                    
                    self.stucks4_picture = 'create_picture/stucks4_picture.png'

                    self.stucks4_open = Image.open(self.stucks4_picture)

                    self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                    self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                
                else:
                    self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                    self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                self.canvas_stucks4.place(x=440,y=310)

                if self.dia_suit_count == 0:
                    self.dia_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_dia.place(x=680,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.dia = 'tramp_picture/' + self.dia_suit[self.dia_suit_count-1] + '.png'

                    self.dia_img = tk.PhotoImage(file = self.dia, width=110 , height=155)

                    self.canvas_dia.create_image(7,7.5,image=self.dia_img, tags='dia',anchor=tk.NW)

                    self.canvas_dia.place(x=680,y=30)

            if self.before_card == '.!canvas6':
                try:
                    if self.card_stucks4[self.stucks4_count-1].startswith('♣') or self.card_stucks4[self.stucks4_count-1].startswith('♠'):
                        return
                    
                    else:
                        if self.card_stucks4[self.stucks4_count-1].startswith('♥'):
                            stuck_table = hurt_table

                        elif self.card_stucks4[self.stucks4_count-1].startswith('♦'):
                            stuck_table = dia_table

                        if self.club_suit[self.club_suit_count-1] == club_table[stuck_table.index(self.card_stucks4[self.stucks4_count-1])-1]:
                            self.card_stucks4[self.stucks4_count] = self.club_suit[self.club_suit_count-1]
                            self.stucks4_count += 1
                            self.stucks4_stuck_count += 1
                            self.club_suit[self.club_suit_count-1] = ''
                            self.club_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter4 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter4,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                    
                    self.stucks4_picture = 'create_picture/stucks4_picture.png'

                    self.stucks4_open = Image.open(self.stucks4_picture)

                    self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                    self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                
                else:
                    self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                    self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                self.canvas_stucks4.place(x=440,y=310)

                if self.club_suit_count == 0:
                    self.club_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_club.place(x=820,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.club = 'tramp_picture/' + self.club_suit[self.club_suit_count-1] + '.png'

                    self.club_img = tk.PhotoImage(file = self.club, width=110 , height=155)

                    self.canvas_club.create_image(7,7.5,image=self.club_img, tags='club',anchor=tk.NW)

                    self.canvas_club.place(x=820,y=30)


        if 'stucks5' in l[0]:
            if self.before_card == '.!canvas3':
                try:
                    if self.card_stucks5[self.stucks5_count-1].startswith('♠') or self.card_stucks5[self.stucks5_count-1].startswith('♣'):
                        return
                    else:
                        if self.card_stucks5[self.stucks5_count-1].startswith('♥'):
                            stuck_table = hurt_table

                        elif self.card_stucks5[self.stucks5_count-1].startswith('♦'):
                            stuck_table = dia_table

                        if self.spade_suit[self.spade_suit_count-1] == spade_table[stuck_table.index(self.card_stucks5[self.stucks5_count-1])-1]:
                            self.card_stucks5[self.stucks5_count] = self.spade_suit[self.spade_suit_count-1]
                            self.stucks5_count += 1
                            self.stucks5_stuck_count += 1
                            self.spade_suit[self.spade_suit_count-1] = ''
                            self.spade_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter5> 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter5,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                    
                    self.stucks5_picture = 'create_picture/stucks5_picture.png'

                    self.stucks5_open = Image.open(self.stucks5_picture)

                    self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                    self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                
                else:
                    self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                    self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                self.canvas_stucks5.place(x=580,y=310)

                print(self.card_stucks5)

                if self.spade_suit_count == 0:
                    self.spade_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_spade.place(x=400,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.spade = 'tramp_picture/' + self.spade_suit[self.spade_suit_count-1] + '.png'

                    self.spade_img = tk.PhotoImage(file = self.spade, width=110 , height=155)

                    self.canvas_spade.create_image(7,7.5,image=self.spade_img, tags='spade',anchor=tk.NW)

                    self.canvas_spade.place(x=400,y=30)


            if self.before_card == '.!canvas4':
                try:
                    if self.card_stucks5[self.stucks5_count-1].startswith('♥') or self.card_stucks5[self.stucks5_count-1].startswith('♦'):
                        return
                    
                    else:
                        if self.card_stucks5[self.stucks5_count-1].startswith('♠'):
                            stuck_table = spade_table

                        elif self.card_stucks5[self.stucks5_count-1].startswith('♣'):
                            stuck_table = club_table

                        if self.hurt_suit[self.hurt_suit_count-1] == hurt_table[stuck_table.index(self.card_stucks5[self.stucks5_count-1])-1]:
                            self.card_stucks5[self.stucks5_count] = self.hurt_suit[self.hurt_suit_count-1]
                            self.stucks5_count += 1
                            self.stucks5_stuck_count += 1
                            self.hurt_suit[self.hurt_suit_count-1] = ''
                            self.hurt_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter5> 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter5,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                    
                    self.stucks5_picture = 'create_picture/stucks5_picture.png'

                    self.stucks5_open = Image.open(self.stucks5_picture)

                    self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                    self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                
                else:
                    self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                    self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                self.canvas_stucks5.place(x=580,y=310)

                print(self.card_stucks5)

                if self.hurt_suit_count == 0:
                    self.hurt_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_hurt.place(x=540,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.hurt = 'tramp_picture/' + self.hurt_suit[self.hurt_suit_count-1] + '.png'

                    self.hurt_img = tk.PhotoImage(file = self.hurt, width=110 , height=155)

                    self.canvas_hurt.create_image(7,7.5,image=self.hurt_img, tags='hurt',anchor=tk.NW)

                    self.canvas_hurt.place(x=540,y=30)
            
            if self.before_card == '.!canvas5':
                try:
                    if self.card_stucks5[self.stucks5_count-1].startswith('♦') or self.card_stucks5[self.stucks5_count-1].startswith('♥'):
                        return

                    else:
                        if self.card_stucks5[self.stucks5_count-1].startswith('♠'):
                            stuck_table = spade_table

                        elif self.card_stucks5[self.stucks5_count-1].startswith('♣'):
                            stuck_table = club_table

                        if self.dia_suit[self.dia_suit_count-1] == dia_table[stuck_table.index(self.card_stucks5[self.stucks5_count-1])-1]:
                            self.card_stucks5[self.stucks5_count] = self.dia_suit[self.dia_suit_count-1]
                            self.stucks5_count += 1
                            self.stucks5_stuck_count += 1
                            self.dia_suit[self.dia_suit_count-1] = ''
                            self.dia_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter5> 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter5,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                    
                    self.stucks5_picture = 'create_picture/stucks5_picture.png'

                    self.stucks5_open = Image.open(self.stucks5_picture)

                    self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                    self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                
                else:
                    self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                    self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                self.canvas_stucks5.place(x=580,y=310)

                print(self.card_stucks5)

                if self.dia_suit_count == 0:
                    self.dia_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_dia.place(x=680,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.dia = 'tramp_picture/' + self.dia_suit[self.dia_suit_count-1] + '.png'

                    self.dia_img = tk.PhotoImage(file = self.dia, width=110 , height=155)

                    self.canvas_dia.create_image(7,7.5,image=self.dia_img, tags='dia',anchor=tk.NW)

                    self.canvas_dia.place(x=680,y=30)

            if self.before_card == '.!canvas6':
                try:
                    if self.card_stucks5[self.stucks5_count-1].startswith('♣') or self.card_stucks5[self.stucks5_count-1].startswith('♠'):
                        return
                    
                    else:
                        if self.card_stucks5[self.stucks5_count-1].startswith('♥'):
                            stuck_table = hurt_table

                        elif self.card_stucks5[self.stucks5_count-1].startswith('♦'):
                            stuck_table = dia_table

                        if self.club_suit[self.club_suit_count-1] == club_table[stuck_table.index(self.card_stucks5[self.stucks5_count-1])-1]:
                            self.card_stucks5[self.stucks5_count] = self.club_suit[self.club_suit_count-1]
                            self.stucks5_count += 1
                            self.stucks5_stuck_count += 1
                            self.club_suit[self.club_suit_count-1] = ''
                            self.club_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter5> 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter5,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                    
                    self.stucks5_picture = 'create_picture/stucks5_picture.png'

                    self.stucks5_open = Image.open(self.stucks5_picture)

                    self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                    self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                
                else:
                    self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                    self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                self.canvas_stucks5.place(x=580,y=310)

                print(self.card_stucks5)

                if self.club_suit_count == 0:
                    self.club_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_club.place(x=820,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.club = 'tramp_picture/' + self.club_suit[self.club_suit_count-1] + '.png'

                    self.club_img = tk.PhotoImage(file = self.club, width=110 , height=155)

                    self.canvas_club.create_image(7,7.5,image=self.club_img, tags='club',anchor=tk.NW)

                    self.canvas_club.place(x=820,y=30)

        if 'stucks6' in l[0]:
            if self.before_card == '.!canvas3':
                try:
                    if self.card_stucks6[self.stucks6_count-1].startswith('♠') or self.card_stucks6[self.stucks6_count-1].startswith('♣'):
                        return
                    else:
                        if self.card_stucks6[self.stucks6_count-1].startswith('♥'):
                            stuck_table = hurt_table

                        elif self.card_stucks6[self.stucks6_count-1].startswith('♦'):
                            stuck_table = dia_table

                        if self.spade_suit[self.spade_suit_count-1] == spade_table[stuck_table.index(self.card_stucks6[self.stucks6_count-1])-1]:
                            self.card_stucks6[self.stucks6_count] = self.spade_suit[self.spade_suit_count-1]
                            self.stucks6_count += 1
                            self.stucks6_stuck_count += 1
                            self.spade_suit[self.spade_suit_count-1] = ''
                            self.spade_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter6 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter6,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                    
                    self.stucks6_picture = 'create_picture/stucks6_picture.png'

                    self.stucks6_open = Image.open(self.stucks6_picture)

                    self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                    self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                else:
                    self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                    self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                self.canvas_stucks6.place(x=720,y=310)

                print(self.card_stucks6)

                if self.spade_suit_count == 0:
                    self.spade_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_spade.place(x=400,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.spade = 'tramp_picture/' + self.spade_suit[self.spade_suit_count-1] + '.png'

                    self.spade_img = tk.PhotoImage(file = self.spade, width=110 , height=155)

                    self.canvas_spade.create_image(7,7.5,image=self.spade_img, tags='spade',anchor=tk.NW)

                    self.canvas_spade.place(x=400,y=30)


            if self.before_card == '.!canvas4':
                try:
                    if self.card_stucks6[self.stucks6_count-1].startswith('♥') or self.card_stucks6[self.stucks6_count-1].startswith('♦'):
                        return
                    
                    else:
                        if self.card_stucks6[self.stucks6_count-1].startswith('♠'):
                            stuck_table = spade_table

                        elif self.card_stucks6[self.stucks6_count-1].startswith('♣'):
                            stuck_table = club_table

                        if self.hurt_suit[self.hurt_suit_count-1] == hurt_table[stuck_table.index(self.card_stucks6[self.stucks6_count-1])-1]:
                            self.card_stucks6[self.stucks6_count] = self.hurt_suit[self.hurt_suit_count-1]
                            self.stucks6_count += 1
                            self.stucks6_stuck_count += 1
                            self.hurt_suit[self.hurt_suit_count-1] = ''
                            self.hurt_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter6 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter6,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                    
                    self.stucks6_picture = 'create_picture/stucks6_picture.png'

                    self.stucks6_open = Image.open(self.stucks6_picture)

                    self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                    self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                else:
                    self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                    self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                self.canvas_stucks6.place(x=720,y=310)


                print(self.card_stucks1)

                if self.hurt_suit_count == 0:
                    self.hurt_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_hurt.place(x=540,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.hurt = 'tramp_picture/' + self.hurt_suit[self.hurt_suit_count-1] + '.png'

                    self.hurt_img = tk.PhotoImage(file = self.hurt, width=110 , height=155)

                    self.canvas_hurt.create_image(7,7.5,image=self.hurt_img, tags='hurt',anchor=tk.NW)

                    self.canvas_hurt.place(x=540,y=30)
            
            if self.before_card == '.!canvas5':
                try:
                    if self.card_stucks6[self.stucks6_count-1].startswith('♦') or self.card_stucks6[self.stucks6_count-1].startswith('♥'):
                        return

                    else:
                        if self.card_stucks6[self.stucks6_count-1].startswith('♠'):
                            stuck_table = spade_table

                        elif self.card_stucks6[self.stucks6_count-1].startswith('♣'):
                            stuck_table = club_table

                        if self.dia_suit[self.dia_suit_count-1] == dia_table[stuck_table.index(self.card_stucks6[self.stucks6_count-1])-1]:
                            self.card_stucks6[self.stucks6_count] = self.dia_suit[self.dia_suit_count-1]
                            self.stucks6_count += 1
                            self.stucks6_stuck_count += 1
                            self.dia_suit[self.dia_suit_count-1] = ''
                            self.dia_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter6 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter6,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                    
                    self.stucks6_picture = 'create_picture/stucks6_picture.png'

                    self.stucks6_open = Image.open(self.stucks6_picture)

                    self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                    self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                else:
                    self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                    self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                self.canvas_stucks6.place(x=720,y=310)

                print(self.card_stucks6)

                if self.dia_suit_count == 0:
                    self.dia_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_dia.place(x=680,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.dia = 'tramp_picture/' + self.dia_suit[self.dia_suit_count-1] + '.png'

                    self.dia_img = tk.PhotoImage(file = self.dia, width=110 , height=155)

                    self.canvas_dia.create_image(7,7.5,image=self.dia_img, tags='dia',anchor=tk.NW)

                    self.canvas_dia.place(x=680,y=30)

            if self.before_card == '.!canvas6':
                try:
                    if self.card_stucks6[self.stucks6_count-1].startswith('♣') or self.card_stucks6[self.stucks6_count-1].startswith('♠'):
                        return
                    
                    else:
                        if self.card_stucks6[self.stucks6_count-1].startswith('♥'):
                            stuck_table = hurt_table

                        elif self.card_stucks6[self.stucks6_count-1].startswith('♦'):
                            stuck_table = dia_table

                        if self.club_suit[self.club_suit_count-1] == club_table[stuck_table.index(self.card_stucks6[self.stucks6_count-1])-1]:
                            self.card_stucks6[self.stucks6_count] = self.club_suit[self.club_suit_count-1]
                            self.stucks6_count += 1
                            self.stucks6_stuck_count += 1
                            self.club_suit[self.club_suit_count-1] = ''
                            self.club_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter6 > 0:
                    openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter6,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                    
                    self.stucks6_picture = 'create_picture/stucks6_picture.png'

                    self.stucks6_open = Image.open(self.stucks6_picture)

                    self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                    self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                else:
                    self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                    self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                self.canvas_stucks6.place(x=720,y=310)

                print(self.card_stucks6)

                if self.club_suit_count == 0:
                    self.club_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_club.place(x=820,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.club = 'tramp_picture/' + self.club_suit[self.club_suit_count-1] + '.png'

                    self.club_img = tk.PhotoImage(file = self.club, width=110 , height=155)

                    self.canvas_club.create_image(7,7.5,image=self.club_img, tags='club',anchor=tk.NW)

                    self.canvas_club.place(x=820,y=30)

        if 'stucks7' in l[0]:
            if self.before_card == '.!canvas3':
                try:
                    if self.card_stucks7[self.stucks7_count-1].startswith('♠') or self.card_stucks7[self.stucks7_count-1].startswith('♣'):
                        return
                    else:
                        if self.card_stucks7[self.stucks7_count-1].startswith('♥'):
                            stuck_table = hurt_table

                        elif self.card_stucks7[self.stucks7_count-1].startswith('♦'):
                            stuck_table = dia_table

                        if self.spade_suit[self.spade_suit_count-1] == spade_table[stuck_table.index(self.card_stucks7[self.stucks7_count-1])-1]:
                            self.card_stucks7[self.stucks7_count] = self.spade_suit[self.spade_suit_count-1]
                            self.stucks7_count += 1
                            self.stucks7_stuck_count += 1
                            self.spade_suit[self.spade_suit_count-1] = ''
                            self.spade_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter7:
                    openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter7,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                    
                    self.stucks7_picture = 'create_picture/stucks7_picture.png'

                    self.stucks7_open = Image.open(self.stucks7_picture)

                    self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                    self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                else:
                    self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                    self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                self.canvas_stucks7.place(x=860,y=310)

                print(self.card_stucks7)

                if self.spade_suit_count == 0:
                    self.spade_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_spade.place(x=400,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.spade = 'tramp_picture/' + self.spade_suit[self.spade_suit_count-1] + '.png'

                    self.spade_img = tk.PhotoImage(file = self.spade, width=110 , height=155)

                    self.canvas_spade.create_image(7,7.5,image=self.spade_img, tags='spade',anchor=tk.NW)

                    self.canvas_spade.place(x=400,y=30)


            if self.before_card == '.!canvas4':
                try:
                    if self.card_stucks7[self.stucks7_count-1].startswith('♥') or self.card_stucks7[self.stucks7_count-1].startswith('♦'):
                        return
                    
                    else:
                        if self.card_stucks7[self.stucks7_count-1].startswith('♠'):
                            stuck_table = spade_table

                        elif self.card_stucks7[self.stucks7_count-1].startswith('♣'):
                            stuck_table = club_table

                        if self.hurt_suit[self.hurt_suit_count-1] == hurt_table[stuck_table.index(self.card_stucks7[self.stucks7_count-1])-1]:
                            self.card_stucks7[self.stucks7_count] = self.hurt_suit[self.hurt_suit_count-1]
                            self.stucks7_count += 1
                            self.stucks7_stuck_count += 1
                            self.hurt_suit[self.hurt_suit_count-1] = ''
                            self.hurt_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter7:
                    openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter7,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                    
                    self.stucks7_picture = 'create_picture/stucks7_picture.png'

                    self.stucks7_open = Image.open(self.stucks7_picture)

                    self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                    self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                else:
                    self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                    self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                self.canvas_stucks7.place(x=860,y=310)

                print(self.card_stucks7)

                if self.hurt_suit_count == 0:
                    self.hurt_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_hurt.place(x=540,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.hurt = 'tramp_picture/' + self.hurt_suit[self.hurt_suit_count-1] + '.png'

                    self.hurt_img = tk.PhotoImage(file = self.hurt, width=110 , height=155)

                    self.canvas_hurt.create_image(7,7.5,image=self.hurt_img, tags='hurt',anchor=tk.NW)

                    self.canvas_hurt.place(x=540,y=30)
            
            if self.before_card == '.!canvas5':
                try:
                    if self.card_stucks7[self.stucks7_count-1].startswith('♦') or self.card_stucks7[self.stucks7_count-1].startswith('♥'):
                        return

                    else:
                        if self.card_stucks7[self.stucks7_count-1].startswith('♠'):
                            stuck_table = spade_table

                        elif self.card_stucks7[self.stucks7_count-1].startswith('♣'):
                            stuck_table = club_table

                        if self.dia_suit[self.dia_suit_count-1] == dia_table[stuck_table.index(self.card_stucks7[self.stucks7_count-1])-1]:
                            self.card_stucks7[self.stucks7_count] = self.dia_suit[self.dia_suit_count-1]
                            self.stucks7_count += 1
                            self.stucks7_stuck_count += 1
                            self.dia_suit[self.dia_suit_count-1] = ''
                            self.dia_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter7:
                    openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter7,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                    
                    self.stucks7_picture = 'create_picture/stucks7_picture.png'

                    self.stucks7_open = Image.open(self.stucks7_picture)

                    self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                    self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                else:
                    self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                    self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                self.canvas_stucks7.place(x=860,y=310)

                print(self.card_stucks7)

                if self.dia_suit_count == 0:
                    self.dia_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_dia.place(x=680,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.dia = 'tramp_picture/' + self.dia_suit[self.dia_suit_count-1] + '.png'

                    self.dia_img = tk.PhotoImage(file = self.dia, width=110 , height=155)

                    self.canvas_dia.create_image(7,7.5,image=self.dia_img, tags='dia',anchor=tk.NW)

                    self.canvas_dia.place(x=680,y=30)

            if self.before_card == '.!canvas6':
                try:
                    if self.card_stucks7[self.stucks7_count-1].startswith('♣') or self.card_stucks7[self.stucks7_count-1].startswith('♠'):
                        return
                    
                    else:
                        if self.card_stucks7[self.stucks7_count-1].startswith('♥'):
                            stuck_table = hurt_table

                        elif self.card_stucks7[self.stucks7_count-1].startswith('♦'):
                            stuck_table = dia_table

                        if self.club_suit[self.club_suit_count-1] == club_table[stuck_table.index(self.card_stucks7[self.stucks7_count-1])-1]:
                            self.card_stucks7[self.stucks7_count] = self.club_suit[self.club_suit_count-1]
                            self.stucks7_count += 1
                            self.stucks7_stuck_count += 1
                            self.club_suit[self.club_suit_count-1] = ''
                            self.club_suit_count -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            return
                except:
                    print('カードを移動できませんでした\n')
                    return
                
                if self.counter7:
                    openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,event)
                                                            
                    backside_img = self.chain_backside_picture(self.counter7,event)

                    self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                    
                    self.stucks7_picture = 'create_picture/stucks7_picture.png'

                    self.stucks7_open = Image.open(self.stucks7_picture)

                    self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                    self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                else:
                    self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                    self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                self.canvas_stucks7.place(x=860,y=310)

                print(self.card_stucks7)

                if self.club_suit_count == 0:
                    self.club_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                    self.canvas_club.place(x=820,y=30)
                    #受付の解除
                    self.canvas_arrow_suit_img = None

                    self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                    self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                    self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                    self.canvas_club.tag_unbind('club','<ButtonPress>')

                    self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                    self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                    self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                    self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                    self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                    self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                    self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                    #再受付
                    self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                    self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                    self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                    self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
                
                else:
                    self.club = 'tramp_picture/' + self.club_suit[self.club_suit_count-1] + '.png'

                    self.club_img = tk.PhotoImage(file = self.club, width=110 , height=155)

                    self.canvas_club.create_image(7,7.5,image=self.club_img, tags='club',anchor=tk.NW)

                    self.canvas_club.place(x=820,y=30)

        #受付の解除
        self.canvas_arrow_suit_img = None

        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

        self.canvas_club.tag_unbind('club','<ButtonPress>')

        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

        #再受付
        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

    def move_stuckscard_to_stucks(self,master,event):
        print("場札：" ,"\n","場札1",self.card_stucks1,"\n","場札2",self.card_stucks2,"\n","場札3",self.card_stucks3,"\n","場札4",self.card_stucks4,"\n","場札5",self.card_stucks5,"\n","場札6",self.card_stucks6,"\n","場札7",self.card_stucks7,"\n")
        print(event.widget)
        print('before_card:' + str(self.before_card))
        if str(event.widget) == '.!canvas7':
            x,y = self.canvas_spade.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_stucks1.itemcget(obj, 'tags') for obj in self.canvas_stucks1.find_overlapping(x,y,x,y)]

        elif str(event.widget) == '.!canvas8':
            x,y = self.canvas_hurt.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_stucks2.itemcget(obj, 'tags') for obj in self.canvas_stucks2.find_overlapping(x,y,x,y)]

        elif str(event.widget) == '.!canvas9':
            x,y = self.canvas_dia.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_stucks3.itemcget(obj, 'tags') for obj in self.canvas_stucks3.find_overlapping(x,y,x,y)]

        elif str(event.widget) == '.!canvas10':
            x,y = self.canvas_club.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_stucks4.itemcget(obj, 'tags') for obj in self.canvas_stucks4.find_overlapping(x,y,x,y)]

        elif str(event.widget) == '.!canvas11':
            x,y = self.canvas_club.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_stucks5.itemcget(obj, 'tags') for obj in self.canvas_stucks5.find_overlapping(x,y,x,y)]
        
        elif str(event.widget) == '.!canvas12':
            x,y = self.canvas_club.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_stucks6.itemcget(obj, 'tags') for obj in self.canvas_stucks6.find_overlapping(x,y,x,y)]
            
        elif str(event.widget) == '.!canvas13':
            x,y = self.canvas_club.canvasx(event.x),self.canvas_stucks1.canvasy(event.y)
            l = [self.canvas_stucks7.itemcget(obj, 'tags') for obj in self.canvas_stucks7.find_overlapping(x,y,x,y)]

        print(l)

        move_suit_table = []

        under_suit_table = []

        move_flag = 0

        if self.before_card == '.!canvas7':
            move_stucks = self.card_stucks1
            move_count = self.stucks1_count
            move_stucks_stuck_count = self.stucks1_stuck_count
        
        elif self.before_card == '.!canvas8':
            move_stucks = self.card_stucks2
            move_count = self.stucks2_count
            move_stucks_stuck_count = self.stucks2_stuck_count
            card_stucks_seacret = self.card_stucks2_seacret
            card_stucks_seacret_count = self.card_stucks2_seacret_count
            counter = self.counter2

        elif self.before_card == '.!canvas9':
            move_stucks = self.card_stucks3
            move_count = self.stucks3_count
            move_stucks_stuck_count = self.stucks3_stuck_count
            card_stucks_seacret = self.card_stucks3_seacret
            card_stucks_seacret_count = self.card_stucks3_seacret_count
            counter = self.counter3     
        
        elif self.before_card == '.!canvas10':
            move_stucks = self.card_stucks4
            move_count = self.stucks4_count 
            move_stucks_stuck_count = self.stucks4_stuck_count
            card_stucks_seacret = self.card_stucks4_seacret
            card_stucks_seacret_count = self.card_stucks4_seacret_count
            counter = self.counter4
        
        elif self.before_card == '.!canvas11':
            move_stucks = self.card_stucks5
            move_count = self.stucks5_count
            move_stucks_stuck_count = self.stucks5_stuck_count
            card_stucks_seacret = self.card_stucks5_seacret
            card_stucks_seacret_count = self.card_stucks5_seacret_count
            counter = self.counter5

        elif self.before_card == '.!canvas12':
            move_stucks = self.card_stucks6
            move_count = self.stucks6_count
            move_stucks_stuck_count = self.stucks6_stuck_count
            card_stucks_seacret = self.card_stucks6_seacret
            card_stucks_seacret_count = self.card_stucks6_seacret_count
            counter = self.counter6

        elif self.before_card == '.!canvas13':
            move_stucks = self.card_stucks7
            move_count = self.stucks7_count
            move_stucks_stuck_count = self.stucks7_stuck_count
            card_stucks_seacret = self.card_stucks7_seacret
            card_stucks_seacret_count = self.card_stucks7_seacret_count
            counter = self.counter7      


        if str(event.widget) == '.!canvas7':
            under_stucks = self.card_stucks1
            under_count = self.stucks1_count
            under_stucks_stuck_count = self.stucks1_stuck_count
        
        elif str(event.widget) =='.!canvas8':
            under_stucks = self.card_stucks2
            under_count = self.stucks2_count
            under_stucks_stuck_count = self.stucks2_stuck_count
            
        elif str(event.widget) =='.!canvas9':
            under_stucks = self.card_stucks3
            under_count = self.stucks3_count
            under_stucks_stuck_count = self.stucks3_stuck_count
            
        elif str(event.widget) =='.!canvas10':
            under_stucks = self.card_stucks4
            under_count = self.stucks4_count
            under_stucks_stuck_count = self.stucks4_stuck_count
        
        elif str(event.widget) =='.!canvas11':
            under_stucks = self.card_stucks5
            under_count = self.stucks5_count
            under_stucks_stuck_count = self.stucks5_stuck_count

        elif str(event.widget) =='.!canvas12':
            under_stucks = self.card_stucks6
            under_count = self.stucks6_count
            under_stucks_stuck_count = self.stucks6_stuck_count

        elif str(event.widget) =='.!canvas13':
            under_stucks = self.card_stucks7
            under_count = self.stucks7_count
            under_stucks_stuck_count = self.stucks7_stuck_count
        
        if move_stucks_stuck_count == 1:
            if under_stucks[0] == '':
                if move_stucks[move_count-1].endswith('K'):
                    under_stucks[under_count] = move_stucks[move_count-1]
                    under_count += 1
                    under_stucks_stuck_count += 1
                    move_stucks[move_count-1] = ''
                    move_count -= 1
                    move_stucks_stuck_count -= 1
                    move_flag = 1
                    if move_stucks[move_count-1] == '*':
                        move_stucks[move_count-1] = card_stucks_seacret[card_stucks_seacret_count]
                        move_stucks_stuck_count += 1
                        card_stucks_seacret_count += 1
                        counter -= 1
                else:
                    print('カードを置けませんでした\n')
                    move_flag = 0
            
            else:
                try:
                    if move_stucks[move_count-1].startswith('♠'):
                        if under_stucks[under_count-1].startswith('♠') or under_stucks[under_count-1].startswith('♣'):
                            print('カードを移動できませんでした\n')
                            move_flag = 0
                        
                        move_suit_table = spade_table

                        if under_stucks[under_count-1].startswith('♥'):
                            under_suit_table = hurt_table

                        elif under_stucks[under_count-1].startswith('♦'):
                            under_suit_table = dia_table
                        
                    elif move_stucks[move_count-1].startswith('♥'):
                        if under_stucks[under_count-1].startswith('♥') or under_stucks[under_count-1].startswith('♦'):
                            print('カードを移動できませんでした\n')
                            move_flag = 0
                        
                        move_suit_table = hurt_table

                        if under_stucks[under_count-1].startswith('♠'):
                            under_suit_table = spade_table

                        elif under_stucks[under_count-1].startswith('♣'):
                            under_suit_table = club_table

                    elif move_stucks[move_count-1].startswith('♦'):
                        if under_stucks[under_count-1].startswith('♥') or under_stucks[under_count-1].startswith('♦'):
                            print('カードを移動できませんでした\n')
                            move_flag =0

                        move_suit_table = dia_table

                        if under_stucks[under_count-1].startswith('♠'):
                            under_suit_table = spade_table

                        elif under_stucks[under_count-1].startswith('♣'):
                            under_suit_table = club_table

                    elif move_stucks[move_count-1].startswith('♣'):
                        if under_stucks[under_count-1].startswith('♠') or under_stucks[under_count-1].startswith('♣'):
                            print('カードを移動できませんでした\n')
                            move_flag = 0

                        move_suit_table = club_table

                        if under_stucks[under_count-1].startswith('♥'):
                            under_suit_table = hurt_table

                        elif under_stucks[under_count-1].startswith('♦'):
                            under_suit_table = dia_table
                    #print('上のカード' + move_stucks[move_count-1])
                    #print('重ねられるカード' + soritaire.move_suit_table[soritaire.under_suit_table.index(under_stucks[under_count-1])-1])

                    if move_stucks[move_count-1]== move_suit_table[under_suit_table.index(under_stucks[under_count-1])-1]:
                        under_stucks[under_count] = move_stucks[move_count-1]
                        under_count += 1
                        under_stucks_stuck_count += 1
                        move_stucks[move_count-1] = ''
                        move_count -= 1
                        move_stucks_stuck_count -= 1
                        move_flag = 1
                        if move_stucks[move_count-1] == '*':
                            move_stucks[move_count-1] = card_stucks_seacret[card_stucks_seacret_count]
                            move_stucks_stuck_count += 1
                            card_stucks_seacret_count += 1
                            counter -= 1
                    else:
                        print('カードを移動できませんでした\n')
                        move_flag = 0
                except:
                    print('カードを移動できませんでした\n')
                    move_flag = 0
        
        else:
            print('クリックした座標:' + str(self.before_event_y))
            #場札の画像の大きさ
            before_stucks_size = (move_count - 1) * 30 + 155

            #何枚動かすか判定する変数を初期化
            move_card_num = 0

            print('場札のサイズ:' + str(before_stucks_size))

            if self.before_card == '.!canvas7':
                if self.before_event_y > (before_stucks_size - 155) and self.before_event_y < before_stucks_size:
                    move_card_num = 1
                
                elif self.before_event_y > (before_stucks_size - 185) and self.before_event_y < (before_stucks_size -155):
                    move_card_num = 2

                elif self.before_event_y > (before_stucks_size - 215) and self.before_event_y < (before_stucks_size - 185):
                    move_card_num = 3
                    
                elif self.before_event_y > (before_stucks_size - 245) and self.before_event_y < (before_stucks_size - 215):
                    move_card_num = 4

                elif self.before_event_y > (before_stucks_size - 275) and self.before_event_y < (before_stucks_size - 245):
                    move_card_num = 5

                elif self.before_event_y > (before_stucks_size - 305) and self.before_event_y < (before_stucks_size - 275):
                    move_card_num = 6

                elif self.before_event_y > (before_stucks_size - 335) and self.before_event_y < (before_stucks_size - 305):
                    move_card_num = 7
                
                elif self.before_event_y > (before_stucks_size - 365) and self.before_event_y < (before_stucks_size - 335):
                    move_card_num = 8

                elif self.before_event_y > (before_stucks_size - 395) and self.before_event_y < (before_stucks_size - 365):
                    move_card_num = 9
                
                elif self.before_event_y > (before_stucks_size - 425) and self.before_event_y < (before_stucks_size - 395):
                    move_card_num = 10

                elif self.before_event_y > (before_stucks_size - 455) and self.before_event_y < (before_stucks_size - 425):
                    move_card_num = 11

                elif self.before_event_y > (before_stucks_size - 485) and self.before_event_y < (before_stucks_size - 455):
                    move_card_num = 12
                
                elif self.before_event_y > (before_stucks_size - 515) and self.before_event_y < (before_stucks_size - 485):
                    move_card_num = 13
            
            elif self.before_card == '.!canvas8':
                if self.before_event_y > (before_stucks_size - 155) and self.before_event_y < before_stucks_size:
                    move_card_num = 1
                
                elif self.before_event_y > (before_stucks_size - 185) and self.before_event_y < (before_stucks_size -155):
                    move_card_num = 2

                elif self.before_event_y > (before_stucks_size - 215) and self.before_event_y < (before_stucks_size - 185):
                    move_card_num = 3
                    
                elif self.before_event_y > (before_stucks_size - 245) and self.before_event_y < (before_stucks_size - 215):
                    move_card_num = 4

                elif self.before_event_y > (before_stucks_size - 275) and self.before_event_y < (before_stucks_size - 245):
                    move_card_num = 5

                elif self.before_event_y > (before_stucks_size - 305) and self.before_event_y < (before_stucks_size - 275):
                    move_card_num = 6

                elif self.before_event_y > (before_stucks_size - 335) and self.before_event_y < (before_stucks_size - 305):
                    move_card_num = 7
                
                elif self.before_event_y > (before_stucks_size - 365) and self.before_event_y < (before_stucks_size - 335):
                    move_card_num = 8

                elif self.before_event_y > (before_stucks_size - 395) and self.before_event_y < (before_stucks_size - 365):
                    move_card_num = 9
                
                elif self.before_event_y > (before_stucks_size - 425) and self.before_event_y < (before_stucks_size - 395):
                    move_card_num = 10

                elif self.before_event_y > (before_stucks_size - 455) and self.before_event_y < (before_stucks_size - 425):
                    move_card_num = 11

                elif self.before_event_y > (before_stucks_size - 485) and self.before_event_y < (before_stucks_size - 455):
                    move_card_num = 12
                
                elif self.before_event_y > (before_stucks_size - 515) and self.before_event_y < (before_stucks_size - 485):
                    move_card_num = 13

            elif self.before_card == '.!canvas9':
                if self.before_event_y > (before_stucks_size - 155) and self.before_event_y < before_stucks_size:
                    move_card_num = 1
                
                elif self.before_event_y > (before_stucks_size - 185) and self.before_event_y < (before_stucks_size -155):
                    move_card_num = 2

                elif self.before_event_y > (before_stucks_size - 215) and self.before_event_y < (before_stucks_size - 185):
                    move_card_num = 3
                    
                elif self.before_event_y > (before_stucks_size - 245) and self.before_event_y < (before_stucks_size - 215):
                    move_card_num = 4

                elif self.before_event_y > (before_stucks_size - 275) and self.before_event_y < (before_stucks_size - 245):
                    move_card_num = 5

                elif self.before_event_y > (before_stucks_size - 305) and self.before_event_y < (before_stucks_size - 275):
                    move_card_num = 6

                elif self.before_event_y > (before_stucks_size - 335) and self.before_event_y < (before_stucks_size - 305):
                    move_card_num = 7
                
                elif self.before_event_y > (before_stucks_size - 365) and self.before_event_y < (before_stucks_size - 335):
                    move_card_num = 8

                elif self.before_event_y > (before_stucks_size - 395) and self.before_event_y < (before_stucks_size - 365):
                    move_card_num = 9
                
                elif self.before_event_y > (before_stucks_size - 425) and self.before_event_y < (before_stucks_size - 395):
                    move_card_num = 10

                elif self.before_event_y > (before_stucks_size - 455) and self.before_event_y < (before_stucks_size - 425):
                    move_card_num = 11

                elif self.before_event_y > (before_stucks_size - 485) and self.before_event_y < (before_stucks_size - 455):
                    move_card_num = 12
                
                elif self.before_event_y > (before_stucks_size - 515) and self.before_event_y < (before_stucks_size - 485):
                    move_card_num = 13

            elif self.before_card == '.!canvas10':
                if self.before_event_y > (before_stucks_size - 155) and self.before_event_y < before_stucks_size:
                    move_card_num = 1
                
                elif self.before_event_y > (before_stucks_size - 185) and self.before_event_y < (before_stucks_size -155):
                    move_card_num = 2

                elif self.before_event_y > (before_stucks_size - 215) and self.before_event_y < (before_stucks_size - 185):
                    move_card_num = 3
                    
                elif self.before_event_y > (before_stucks_size - 245) and self.before_event_y < (before_stucks_size - 215):
                    move_card_num = 4

                elif self.before_event_y > (before_stucks_size - 275) and self.before_event_y < (before_stucks_size - 245):
                    move_card_num = 5

                elif self.before_event_y > (before_stucks_size - 305) and self.before_event_y < (before_stucks_size - 275):
                    move_card_num = 6

                elif self.before_event_y > (before_stucks_size - 335) and self.before_event_y < (before_stucks_size - 305):
                    move_card_num = 7
                
                elif self.before_event_y > (before_stucks_size - 365) and self.before_event_y < (before_stucks_size - 335):
                    move_card_num = 8

                elif self.before_event_y > (before_stucks_size - 395) and self.before_event_y < (before_stucks_size - 365):
                    move_card_num = 9
                
                elif self.before_event_y > (before_stucks_size - 425) and self.before_event_y < (before_stucks_size - 395):
                    move_card_num = 10

                elif self.before_event_y > (before_stucks_size - 455) and self.before_event_y < (before_stucks_size - 425):
                    move_card_num = 11

                elif self.before_event_y > (before_stucks_size - 485) and self.before_event_y < (before_stucks_size - 455):
                    move_card_num = 12
                
                elif self.before_event_y > (before_stucks_size - 515) and self.before_event_y < (before_stucks_size - 485):
                    move_card_num = 13

            elif self.before_card == '.!canvas11':
                if self.before_event_y > (before_stucks_size - 155) and self.before_event_y < before_stucks_size:
                    move_card_num = 1
                
                elif self.before_event_y > (before_stucks_size - 185) and self.before_event_y < (before_stucks_size -155):
                    move_card_num = 2

                elif self.before_event_y > (before_stucks_size - 215) and self.before_event_y < (before_stucks_size - 185):
                    move_card_num = 3
                    
                elif self.before_event_y > (before_stucks_size - 245) and self.before_event_y < (before_stucks_size - 215):
                    move_card_num = 4

                elif self.before_event_y > (before_stucks_size - 275) and self.before_event_y < (before_stucks_size - 245):
                    move_card_num = 5

                elif self.before_event_y > (before_stucks_size - 305) and self.before_event_y < (before_stucks_size - 275):
                    move_card_num = 6

                elif self.before_event_y > (before_stucks_size - 335) and self.before_event_y < (before_stucks_size - 305):
                    move_card_num = 7
                
                elif self.before_event_y > (before_stucks_size - 365) and self.before_event_y < (before_stucks_size - 335):
                    move_card_num = 8

                elif self.before_event_y > (before_stucks_size - 395) and self.before_event_y < (before_stucks_size - 365):
                    move_card_num = 9
                
                elif self.before_event_y > (before_stucks_size - 425) and self.before_event_y < (before_stucks_size - 395):
                    move_card_num = 10

                elif self.before_event_y > (before_stucks_size - 455) and self.before_event_y < (before_stucks_size - 425):
                    move_card_num = 11

                elif self.before_event_y > (before_stucks_size - 485) and self.before_event_y < (before_stucks_size - 455):
                    move_card_num = 12
                
                elif self.before_event_y > (before_stucks_size - 515) and self.before_event_y < (before_stucks_size - 485):
                    move_card_num = 13

            elif self.before_card == '.!canvas12':
                if self.before_event_y > (before_stucks_size - 155) and self.before_event_y < before_stucks_size:
                    move_card_num = 1
                
                elif self.before_event_y > (before_stucks_size - 185) and self.before_event_y < (before_stucks_size -155):
                    move_card_num = 2

                elif self.before_event_y > (before_stucks_size - 215) and self.before_event_y < (before_stucks_size - 185):
                    move_card_num = 3
                    
                elif self.before_event_y > (before_stucks_size - 245) and self.before_event_y < (before_stucks_size - 215):
                    move_card_num = 4

                elif self.before_event_y > (before_stucks_size - 275) and self.before_event_y < (before_stucks_size - 245):
                    move_card_num = 5

                elif self.before_event_y > (before_stucks_size - 305) and self.before_event_y < (before_stucks_size - 275):
                    move_card_num = 6

                elif self.before_event_y > (before_stucks_size - 335) and self.before_event_y < (before_stucks_size - 305):
                    move_card_num = 7
                
                elif self.before_event_y > (before_stucks_size - 365) and self.before_event_y < (before_stucks_size - 335):
                    move_card_num = 8

                elif self.before_event_y > (before_stucks_size - 395) and self.before_event_y < (before_stucks_size - 365):
                    move_card_num = 9
                
                elif self.before_event_y > (before_stucks_size - 425) and self.before_event_y < (before_stucks_size - 395):
                    move_card_num = 10

                elif self.before_event_y > (before_stucks_size - 455) and self.before_event_y < (before_stucks_size - 425):
                    move_card_num = 11

                elif self.before_event_y > (before_stucks_size - 485) and self.before_event_y < (before_stucks_size - 455):
                    move_card_num = 12
                
                elif self.before_event_y > (before_stucks_size - 515) and self.before_event_y < (before_stucks_size - 485):
                    move_card_num = 13

            elif self.before_card == '.!canvas13':
                if self.before_event_y > (before_stucks_size - 155) and self.before_event_y < before_stucks_size:
                    move_card_num = 1
                
                elif self.before_event_y > (before_stucks_size - 185) and self.before_event_y < (before_stucks_size -155):
                    move_card_num = 2

                elif self.before_event_y > (before_stucks_size - 215) and self.before_event_y < (before_stucks_size - 185):
                    move_card_num = 3
                    
                elif self.before_event_y > (before_stucks_size - 245) and self.before_event_y < (before_stucks_size - 215):
                    move_card_num = 4

                elif self.before_event_y > (before_stucks_size - 275) and self.before_event_y < (before_stucks_size - 245):
                    move_card_num = 5

                elif self.before_event_y > (before_stucks_size - 305) and self.before_event_y < (before_stucks_size - 275):
                    move_card_num = 6

                elif self.before_event_y > (before_stucks_size - 335) and self.before_event_y < (before_stucks_size - 305):
                    move_card_num = 7
                
                elif self.before_event_y > (before_stucks_size - 365) and self.before_event_y < (before_stucks_size - 335):
                    move_card_num = 8

                elif self.before_event_y > (before_stucks_size - 395) and self.before_event_y < (before_stucks_size - 365):
                    move_card_num = 9
                
                elif self.before_event_y > (before_stucks_size - 425) and self.before_event_y < (before_stucks_size - 395):
                    move_card_num = 10

                elif self.before_event_y > (before_stucks_size - 455) and self.before_event_y < (before_stucks_size - 425):
                    move_card_num = 11

                elif self.before_event_y > (before_stucks_size - 485) and self.before_event_y < (before_stucks_size - 455):
                    move_card_num = 12
                
                elif self.before_event_y > (before_stucks_size - 515) and self.before_event_y < (before_stucks_size - 485):
                    move_card_num = 13

            print('動かす枚数：' + str(move_card_num))

            if under_stucks[0] == '':
                if move_stucks[move_count - move_card_num].endswith('K'):
                    under_stucks[under_count] = move_stucks[move_count - move_card_num]
                    under_count += 1
                    under_stucks_stuck_count += 1
                    move_stucks[move_count - move_card_num] = ''
                    move_stucks_stuck_count -= 1
                    move_card_num -= 1
                    while move_stucks[move_count - move_card_num] != '':
                        if move_stucks[move_count - move_card_num].startswith('♠'):
                            move_suit_table = spade_table
                            if under_stucks[under_count-1].startswith('♥'):
                                under_suit_table = hurt_table

                            elif under_stucks[under_count-1].startswith('♦'):
                                under_suit_table = dia_table
                        
                        elif move_stucks[move_count - move_card_num].startswith('♥'):
                            move_suit_table = hurt_table
                            if under_stucks[under_count-1].startswith('♠'):
                                under_suit_table = spade_table

                            elif under_stucks[under_count-1].startswith('♣'):
                                under_suit_table = club_table

                        elif move_stucks[move_count - move_card_num].startswith('♦'):
                            move_suit_table = dia_table
                            if under_stucks[under_count-1].startswith('♠'):
                                under_suit_table = spade_table

                            elif under_stucks[under_count-1].startswith('♣'):
                                under_suit_table = club_table

                        elif move_stucks[move_count - move_card_num].startswith('♣'):
                            move_suit_table = club_table
                            if under_stucks[under_count-1].startswith('♥'):
                                under_suit_table = hurt_table

                            elif under_stucks[under_count-1].startswith('♦'):
                                under_suit_table = dia_table
                        try:
                            if move_stucks[move_count - move_card_num]== move_suit_table[under_suit_table.index(under_stucks[under_count-1])-1]:
                                under_stucks[under_count] = move_stucks[move_count - move_card_num]
                                under_count += 1
                                under_stucks_stuck_count += 1
                                move_stucks[move_count - move_card_num] = ''
                                move_stucks_stuck_count -= 1
                                move_flag = 1
                                move_card_num -= 1
                            else:
                                print('カードを移動できませんでした\n')
                                move_flag = 0
                                break
                        except:
                            print('カードを移動できませんでした\n')
                            move_flag = 0
                            break
                move_count = move_stucks.index('')

            else:
                while move_stucks[move_count - move_card_num] != '':
                    if move_stucks[move_count - move_card_num].startswith('♠'):
                        if under_stucks[under_count-1].startswith('♠') or under_stucks[under_count-1].startswith('♣'):
                            print('カードを移動できませんでした\n')
                            move_flag = 0
                            break
                        
                        move_suit_table = spade_table

                        if under_stucks[under_count-1].startswith('♥'):
                            under_suit_table = hurt_table

                        elif under_stucks[under_count-1].startswith('♦'):
                            under_suit_table = dia_table
                        
                    elif move_stucks[move_count - move_card_num].startswith('♥'):
                        if under_stucks[under_count-1].startswith('♥') or under_stucks[under_count-1].startswith('♦'):
                            print('カードを移動できませんでした\n')
                            move_flag = 0
                            break
                        
                        move_suit_table = hurt_table

                        if under_stucks[under_count-1].startswith('♠'):
                            under_suit_table = spade_table

                        elif under_stucks[under_count-1].startswith('♣'):
                            under_suit_table = club_table

                    elif move_stucks[move_count - move_card_num].startswith('♦'):
                        if under_stucks[under_count-1].startswith('♥') or under_stucks[under_count-1].startswith('♦'):
                            print('カードを移動できませんでした\n')
                            move_flag = 0
                            break

                        move_suit_table = dia_table

                        if under_stucks[under_count-1].startswith('♠'):
                            under_suit_table = spade_table

                        elif under_stucks[under_count-1].startswith('♣'):
                            under_suit_table = club_table

                    elif move_stucks[move_count - move_card_num].startswith('♣'):
                        if under_stucks[under_count-1].startswith('♠') or under_stucks[under_count-1].startswith('♣'):
                            print('カードを移動できませんでした\n')
                            move_flag = 0
                            break

                        move_suit_table = club_table

                        if under_stucks[under_count-1].startswith('♥'):
                            under_suit_table = hurt_table

                        elif under_stucks[under_count-1].startswith('♦'):
                            under_suit_table = dia_table
                    try:
                        if move_stucks[move_count - move_card_num] == move_suit_table[under_suit_table.index(under_stucks[under_count-1])-1]:
                            under_stucks[under_count] = move_stucks[move_count - move_card_num]
                            under_count += 1
                            under_stucks_stuck_count += 1
                            move_stucks[move_count - move_card_num] = ''
                            move_stucks_stuck_count -= 1
                            move_flag = 1
                            move_card_num -= 1
                        else:
                            print('カードを移動できませんでした\n')
                            move_flag =0
                            break
                    except:
                        print('カードを移動できませんでした\n')
                        move_flag = 0
                        break
         
                move_count = move_stucks.index('')


            if move_stucks[move_count-1] == '*':
                move_stucks[move_count-1] = card_stucks_seacret[card_stucks_seacret_count]
                move_stucks_stuck_count += 1
                card_stucks_seacret_count += 1
                counter -= 1



        if self.before_card == '.!canvas7':
            self.card_stucks1 = move_stucks
            self.stucks1_count = move_count
            self.stucks1_stuck_count = move_stucks_stuck_count
        
        elif self.before_card == '.!canvas8':
            self.card_stucks2 = move_stucks
            self.stucks2_count = move_count
            self.stucks2_stuck_count = move_stucks_stuck_count
            self.card_stucks2_seacret = card_stucks_seacret
            self.card_stucks2_seacret_count = card_stucks_seacret_count
            self.counter2 = counter
        
        elif self.before_card == '.!canvas9':
            self.card_stucks3 = move_stucks
            self.stucks3_count = move_count
            self.stucks3_stuck_count = move_stucks_stuck_count
            self.card_stucks3_seacret = card_stucks_seacret
            self.card_stucks3_seacret_count = card_stucks_seacret_count
            self.counter3 = counter
        
        elif self.before_card == '.!canvas10':
            self.card_stucks4 = move_stucks
            self.stucks4_count = move_count
            self.stucks4_stuck_count = move_stucks_stuck_count
            self.card_stucks4_seacret = card_stucks_seacret
            self.card_stucks4_seacret_count = card_stucks_seacret_count
            self.counter4 = counter
        
        elif self.before_card == '.!canvas11':
            self.card_stucks5 = move_stucks
            self.stucks5_count = move_count
            self.stucks5_stuck_count = move_stucks_stuck_count
            self.card_stucks5_seacret = card_stucks_seacret
            self.card_stucks5_seacret_count = card_stucks_seacret_count
            self.counter5 = counter

        elif self.before_card == '.!canvas12':
            self.card_stucks6 = move_stucks
            self.stucks6_count = move_count
            self.stucks6_stuck_count = move_stucks_stuck_count
            self.card_stucks6_seacret = card_stucks_seacret
            self.card_stucks6_seacret_count = card_stucks_seacret_count
            self.counter6 = counter

        elif self.before_card == '.!canvas13':
            self.card_stucks7 = move_stucks
            self.stucks7_count = move_count
            self.stucks7_stuck_count = move_stucks_stuck_count
            self.card_stucks7_seacret = card_stucks_seacret
            self.card_stucks7_seacret_count = card_stucks_seacret_count
            self.counter7 = counter
        
        if str(event.widget) == '.!canvas7':
            self.card_stucks1 = under_stucks
            self.stucks1_count = under_count
            self.stucks1_stuck_count = under_stucks_stuck_count
        
        elif str(event.widget) == '.!canvas8':
            self.card_stucks2 = under_stucks
            self.stucks2_count = under_count
            self.stucks2_stuck_count = under_stucks_stuck_count
        
        elif str(event.widget) == '.!canvas9':
            self.card_stucks3 = under_stucks
            self.stucks3_count = under_count
            self.stucks3_stuck_count = under_stucks_stuck_count

        elif str(event.widget) == '.!canvas10':
            self.card_stucks4 = under_stucks
            self.stucks4_count = under_count
            self.stucks4_stuck_count = under_stucks_stuck_count

        elif str(event.widget) == '.!canvas11':
            self.card_stucks5 = under_stucks
            self.stucks5_count = under_count
            self.stucks5_stuck_count = under_stucks_stuck_count

        elif str(event.widget) == '.!canvas12':
            self.card_stucks6 = under_stucks
            self.stucks6_count = under_count
            self.stucks6_stuck_count = under_stucks_stuck_count

        elif str(event.widget) == '.!canvas13':
            self.card_stucks7 = under_stucks
            self.stucks7_count = under_count
            self.stucks7_stuck_count = under_stucks_stuck_count

        if move_flag == 1:
            if self.before_card == '.!canvas7':    
                if 'stucks2' in l[0]:
                    if self.counter2 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,event)

                        backside_img = self.chain_backside_picture(self.counter2,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                    
                        self.stucks2_picture = 'create_picture/stucks2_picture.png'

                        self.stucks2_open = Image.open(self.stucks2_picture)

                        self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                        
                    else:
                        self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                    self.canvas_stucks2.place(x=160,y=310)

                    if self.stucks1_count == 0:
                        self.stucks1_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                        
                        self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                        self.canvas_stucks1.place(x=20,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None

                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                        self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                        self.canvas_stucks1.place(x=20,y=310)

                        print(self.card_stucks1)

                elif 'stucks3' in l[0]:
                    if self.counter3 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter3,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                        
                        self.stucks3_picture = 'create_picture/stucks3_picture.png'

                        self.stucks3_open = Image.open(self.stucks3_picture)

                        self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                    
                    else:
                        self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                    self.canvas_stucks3.place(x=300,y=310)
                
                    if self.stucks1_count == 0:
                        self.stucks1_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                        
                        self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                        self.canvas_stucks1.place(x=20,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                        self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                        self.canvas_stucks1.place(x=20,y=310)

                        print(self.card_stucks1)

                elif 'stucks4' in l[0]:
                    if self.counter4 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter4,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                        
                        self.stucks4_picture = 'create_picture/stucks4_picture.png'

                        self.stucks4_open = Image.open(self.stucks4_picture)

                        self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                    
                    else:
                        self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                    self.canvas_stucks4.place(x=440,y=310)

                    if self.stucks1_count == 0:
                        self.stucks1_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                        
                        self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                        self.canvas_stucks1.place(x=20,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                        self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                        self.canvas_stucks1.place(x=20,y=310)

                        print(self.card_stucks1)

                elif 'stucks5' in l[0]:
                    if self.counter5> 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter5,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                        
                        self.stucks5_picture = 'create_picture/stucks5_picture.png'

                        self.stucks5_open = Image.open(self.stucks5_picture)

                        self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                    
                    else:
                        self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                    
                    self.canvas_stucks5.place(x=580,y=310)


                    if self.stucks1_count == 0:
                        self.stucks1_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                        
                        self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                        self.canvas_stucks1.place(x=20,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                        self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                        self.canvas_stucks1.place(x=20,y=310)

                        print(self.card_stucks1)
                
                elif 'stucks6' in l[0]:
                    if self.counter6 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter6,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                        
                        self.stucks6_picture = 'create_picture/stucks6_picture.png'

                        self.stucks6_open = Image.open(self.stucks6_picture)

                        self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    else:
                        self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    self.canvas_stucks6.place(x=720,y=310)

                    if self.stucks1_count == 0:
                        self.stucks1_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                        
                        self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                        self.canvas_stucks1.place(x=20,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                        self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                        self.canvas_stucks1.place(x=20,y=310)

                        print(self.card_stucks1)

                elif 'stucks7' in l[0]:
                    if self.counter7 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter7,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                        
                        self.stucks7_picture = 'create_picture/stucks7_picture.png'

                        self.stucks7_open = Image.open(self.stucks7_picture)

                        self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    else:
                        self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    self.canvas_stucks7.place(x=860,y=310)


                    if self.stucks1_count == 0:
                        self.stucks1_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)
                        
                        self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                        self.canvas_stucks1.place(x=20,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                        self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                        self.canvas_stucks1.place(x=20,y=310)

                        print(self.card_stucks1)

            elif self.before_card == '.!canvas8':    
                if 'stucks1' in l[0]:
                    self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                    self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                    self.canvas_stucks1.place(x=20,y=310)

                    if self.stucks2_count == 0:
                        self.stucks2_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                        self.canvas_stucks2.place(x=160,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter2 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,self.before_card)

                            backside_img = self.chain_backside_picture(self.counter2,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                        
                            self.stucks2_picture = 'create_picture/stucks2_picture.png'

                            self.stucks2_open = Image.open(self.stucks2_picture)

                            self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                            self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                            
                        else:
                            self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                            self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                        self.canvas_stucks2.place(x=160,y=310)

                elif 'stucks3' in l[0]:
                    if self.counter3 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter3,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                        
                        self.stucks3_picture = 'create_picture/stucks3_picture.png'

                        self.stucks3_open = Image.open(self.stucks3_picture)

                        self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                    
                    else:
                        self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                    self.canvas_stucks3.place(x=300,y=310)
                
                    if self.stucks2_count == 0:
                        self.stucks2_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                        self.canvas_stucks2.place(x=160,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter2 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,self.before_card)

                            backside_img = self.chain_backside_picture(self.counter2,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                        
                            self.stucks2_picture = 'create_picture/stucks2_picture.png'

                            self.stucks2_open = Image.open(self.stucks2_picture)

                            self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                            self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                            
                        else:
                            self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                            self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                        self.canvas_stucks2.place(x=160,y=310)

                elif 'stucks4' in l[0]:
                    if self.counter4 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter4,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                        
                        self.stucks4_picture = 'create_picture/stucks4_picture.png'

                        self.stucks4_open = Image.open(self.stucks4_picture)

                        self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                    
                    else:
                        self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                    self.canvas_stucks4.place(x=440,y=310)

                    if self.stucks2_count == 0:
                        self.stucks2_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                        self.canvas_stucks2.place(x=160,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter2 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,self.before_card)

                            backside_img = self.chain_backside_picture(self.counter2,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                        
                            self.stucks2_picture = 'create_picture/stucks2_picture.png'

                            self.stucks2_open = Image.open(self.stucks2_picture)

                            self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                            self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                            
                        else:
                            self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                            self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                        self.canvas_stucks2.place(x=160,y=310)

                elif 'stucks5' in l[0]:
                    if self.counter5> 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter5,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                        
                        self.stucks5_picture = 'create_picture/stucks5_picture.png'

                        self.stucks5_open = Image.open(self.stucks5_picture)

                        self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                    
                    else:
                        self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                    
                    self.canvas_stucks5.place(x=580,y=310)


                    if self.stucks2_count == 0:
                        self.stucks2_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                        self.canvas_stucks2.place(x=160,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter2 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,self.before_card)

                            backside_img = self.chain_backside_picture(self.counter2,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                        
                            self.stucks2_picture = 'create_picture/stucks2_picture.png'

                            self.stucks2_open = Image.open(self.stucks2_picture)

                            self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                            self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                            
                        else:
                            self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                            self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                        self.canvas_stucks2.place(x=160,y=310)
                
                elif 'stucks6' in l[0]:
                    if self.counter6 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter6,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                        
                        self.stucks6_picture = 'create_picture/stucks6_picture.png'

                        self.stucks6_open = Image.open(self.stucks6_picture)

                        self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    else:
                        self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    self.canvas_stucks6.place(x=720,y=310)

                    if self.stucks2_count == 0:
                        self.stucks2_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                        self.canvas_stucks2.place(x=160,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter2 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,self.before_card)

                            backside_img = self.chain_backside_picture(self.counter2,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                        
                            self.stucks2_picture = 'create_picture/stucks2_picture.png'

                            self.stucks2_open = Image.open(self.stucks2_picture)

                            self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                            self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                            
                        else:
                            self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                            self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                        self.canvas_stucks2.place(x=160,y=310)

                elif 'stucks7' in l[0]:
                    if self.counter7 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter7,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                        
                        self.stucks7_picture = 'create_picture/stucks7_picture.png'

                        self.stucks7_open = Image.open(self.stucks7_picture)

                        self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    else:
                        self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    self.canvas_stucks7.place(x=860,y=310)


                    if self.stucks2_count == 0:
                        self.stucks2_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                        self.canvas_stucks2.place(x=160,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter2 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,self.before_card)

                            backside_img = self.chain_backside_picture(self.counter2,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                        
                            self.stucks2_picture = 'create_picture/stucks2_picture.png'

                            self.stucks2_open = Image.open(self.stucks2_picture)

                            self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                            self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                            
                        else:
                            self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                            self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                        self.canvas_stucks2.place(x=160,y=310)

            elif self.before_card == '.!canvas9':    
                if 'stucks1' in l[0]:
                    self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                    self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                    self.canvas_stucks1.place(x=20,y=310)

                    if self.stucks3_count == 0:
                        self.stucks3_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                        self.canvas_stucks3.place(x=300,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter3 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter3,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                            
                            self.stucks3_picture = 'create_picture/stucks3_picture.png'

                            self.stucks3_open = Image.open(self.stucks3_picture)

                            self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                            self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                        
                        else:
                            self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                            self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                        self.canvas_stucks3.place(x=300,y=310)

                elif 'stucks2' in l[0]:
                    if self.counter2 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,event)

                        backside_img = self.chain_backside_picture(self.counter2,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                    
                        self.stucks2_picture = 'create_picture/stucks2_picture.png'

                        self.stucks2_open = Image.open(self.stucks2_picture)

                        self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                        
                    else:
                        self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                    self.canvas_stucks2.place(x=160,y=310)
                
                    if self.stucks3_count == 0:
                        self.stucks3_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                        self.canvas_stucks3.place(x=300,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter3 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter3,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                            
                            self.stucks3_picture = 'create_picture/stucks3_picture.png'

                            self.stucks3_open = Image.open(self.stucks3_picture)

                            self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                            self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                        
                        else:
                            self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                            self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                        self.canvas_stucks3.place(x=300,y=310)

                elif 'stucks4' in l[0]:
                    if self.counter4 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter4,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                        
                        self.stucks4_picture = 'create_picture/stucks4_picture.png'

                        self.stucks4_open = Image.open(self.stucks4_picture)

                        self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                    
                    else:
                        self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                    self.canvas_stucks4.place(x=440,y=310)

                    if self.stucks3_count == 0:
                        self.stucks3_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                        self.canvas_stucks3.place(x=300,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter3 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter3,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                            
                            self.stucks3_picture = 'create_picture/stucks3_picture.png'

                            self.stucks3_open = Image.open(self.stucks3_picture)

                            self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                            self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                        
                        else:
                            self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                            self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                        self.canvas_stucks3.place(x=300,y=310)

                elif 'stucks5' in l[0]:
                    if self.counter5> 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter5,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                        
                        self.stucks5_picture = 'create_picture/stucks5_picture.png'

                        self.stucks5_open = Image.open(self.stucks5_picture)

                        self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                    
                    else:
                        self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                    
                    self.canvas_stucks5.place(x=580,y=310)


                    if self.stucks3_count == 0:
                        self.stucks3_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                        self.canvas_stucks3.place(x=300,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter3 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter3,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                            
                            self.stucks3_picture = 'create_picture/stucks3_picture.png'

                            self.stucks3_open = Image.open(self.stucks3_picture)

                            self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                            self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                        
                        else:
                            self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                            self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                        self.canvas_stucks3.place(x=300,y=310)
                
                elif 'stucks6' in l[0]:
                    if self.counter6 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter6,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                        
                        self.stucks6_picture = 'create_picture/stucks6_picture.png'

                        self.stucks6_open = Image.open(self.stucks6_picture)

                        self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    else:
                        self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    self.canvas_stucks6.place(x=720,y=310)

                    if self.stucks3_count == 0:
                        self.stucks3_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                        self.canvas_stucks3.place(x=300,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter3 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter3,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                            
                            self.stucks3_picture = 'create_picture/stucks3_picture.png'

                            self.stucks3_open = Image.open(self.stucks3_picture)

                            self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                            self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                        
                        else:
                            self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                            self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                        self.canvas_stucks3.place(x=300,y=310)

                elif 'stucks7' in l[0]:
                    if self.counter7 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter7,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                        
                        self.stucks7_picture = 'create_picture/stucks7_picture.png'

                        self.stucks7_open = Image.open(self.stucks7_picture)

                        self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    else:
                        self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    self.canvas_stucks7.place(x=860,y=310)


                    if self.stucks3_count == 0:
                        self.stucks3_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                        self.canvas_stucks3.place(x=300,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter3 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter3,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                            
                            self.stucks3_picture = 'create_picture/stucks3_picture.png'

                            self.stucks3_open = Image.open(self.stucks3_picture)

                            self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                            self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                        
                        else:
                            self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                            self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                        self.canvas_stucks3.place(x=300,y=310)

            elif self.before_card == '.!canvas10':    
                if 'stucks1' in l[0]:
                    self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                    self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                    self.canvas_stucks1.place(x=20,y=310)

                    if self.stucks4_count == 0:
                        self.stucks4_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                        self.canvas_stucks4.place(x=440,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter4 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter4,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                            
                            self.stucks4_picture = 'create_picture/stucks4_picture.png'

                            self.stucks4_open = Image.open(self.stucks4_picture)

                            self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                            self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                        
                        else:
                            self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                            self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                        self.canvas_stucks4.place(x=440,y=310)

                elif 'stucks2' in l[0]:
                    if self.counter2 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,event)

                        backside_img = self.chain_backside_picture(self.counter2,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                    
                        self.stucks2_picture = 'create_picture/stucks2_picture.png'

                        self.stucks2_open = Image.open(self.stucks2_picture)

                        self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                        
                    else:
                        self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                    self.canvas_stucks2.place(x=160,y=310)
                
                    if self.stucks4_count == 0:
                        self.stucks4_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                        self.canvas_stucks4.place(x=440,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter4 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter4,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                            
                            self.stucks4_picture = 'create_picture/stucks4_picture.png'

                            self.stucks4_open = Image.open(self.stucks4_picture)

                            self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                            self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                        
                        else:
                            self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                            self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                        self.canvas_stucks4.place(x=440,y=310)

                elif 'stucks3' in l[0]:
                    if self.counter3 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter3,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                        
                        self.stucks3_picture = 'create_picture/stucks3_picture.png'

                        self.stucks3_open = Image.open(self.stucks3_picture)

                        self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                    
                    else:
                        self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                    self.canvas_stucks3.place(x=300,y=310)

                    if self.stucks4_count == 0:
                        self.stucks4_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                        self.canvas_stucks4.place(x=440,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter4 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter4,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                            
                            self.stucks4_picture = 'create_picture/stucks4_picture.png'

                            self.stucks4_open = Image.open(self.stucks4_picture)

                            self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                            self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                        
                        else:
                            self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                            self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                        self.canvas_stucks4.place(x=440,y=310)

                elif 'stucks5' in l[0]:
                    if self.counter5> 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter5,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                        
                        self.stucks5_picture = 'create_picture/stucks5_picture.png'

                        self.stucks5_open = Image.open(self.stucks5_picture)

                        self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                    
                    else:
                        self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                    
                    self.canvas_stucks5.place(x=580,y=310)


                    if self.stucks4_count == 0:
                        self.stucks4_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                        self.canvas_stucks4.place(x=440,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter4 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter4,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                            
                            self.stucks4_picture = 'create_picture/stucks4_picture.png'

                            self.stucks4_open = Image.open(self.stucks4_picture)

                            self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                            self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                        
                        else:
                            self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                            self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                        self.canvas_stucks4.place(x=440,y=310)
                
                elif 'stucks6' in l[0]:
                    if self.counter6 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter6,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                        
                        self.stucks6_picture = 'create_picture/stucks6_picture.png'

                        self.stucks6_open = Image.open(self.stucks6_picture)

                        self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    else:
                        self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    self.canvas_stucks6.place(x=720,y=310)

                    if self.stucks4_count == 0:
                        self.stucks4_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                        self.canvas_stucks4.place(x=440,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter4 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter4,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                            
                            self.stucks4_picture = 'create_picture/stucks4_picture.png'

                            self.stucks4_open = Image.open(self.stucks4_picture)

                            self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                            self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                        
                        else:
                            self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                            self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                        self.canvas_stucks4.place(x=440,y=310)

                elif 'stucks7' in l[0]:
                    if self.counter7 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter7,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                        
                        self.stucks7_picture = 'create_picture/stucks7_picture.png'

                        self.stucks7_open = Image.open(self.stucks7_picture)

                        self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    else:
                        self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    self.canvas_stucks7.place(x=860,y=310)


                    if self.stucks4_count == 0:
                        self.stucks4_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                        self.canvas_stucks4.place(x=440,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter4 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter4,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                            
                            self.stucks4_picture = 'create_picture/stucks4_picture.png'

                            self.stucks4_open = Image.open(self.stucks4_picture)

                            self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                            self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                        
                        else:
                            self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                            self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                        self.canvas_stucks4.place(x=440,y=310)

            elif self.before_card == '.!canvas11':    
                if 'stucks1' in l[0]:
                    self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                    self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                    self.canvas_stucks1.place(x=20,y=310)

                    if self.stucks5_count == 0:
                        self.stucks5_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                        self.canvas_stucks5.place(x=580,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter5> 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter5,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                            
                            self.stucks5_picture = 'create_picture/stucks5_picture.png'

                            self.stucks5_open = Image.open(self.stucks5_picture)

                            self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                            self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                        
                        else:
                            self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                            self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                        
                        self.canvas_stucks5.place(x=580,y=310)

                elif 'stucks2' in l[0]:
                    if self.counter2 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,event)

                        backside_img = self.chain_backside_picture(self.counter2,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                    
                        self.stucks2_picture = 'create_picture/stucks2_picture.png'

                        self.stucks2_open = Image.open(self.stucks2_picture)

                        self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                        
                    else:
                        self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                    self.canvas_stucks2.place(x=160,y=310)
                
                    if self.stucks5_count == 0:
                        self.stucks5_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                        self.canvas_stucks5.place(x=580,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter5> 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter5,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                            
                            self.stucks5_picture = 'create_picture/stucks5_picture.png'

                            self.stucks5_open = Image.open(self.stucks5_picture)

                            self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                            self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                        
                        else:
                            self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                            self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                        
                        self.canvas_stucks5.place(x=580,y=310)

                elif 'stucks3' in l[0]:
                    if self.counter3 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter3,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                        
                        self.stucks3_picture = 'create_picture/stucks3_picture.png'

                        self.stucks3_open = Image.open(self.stucks3_picture)

                        self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                    
                    else:
                        self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                    self.canvas_stucks3.place(x=300,y=310)

                    if self.stucks5_count == 0:
                        self.stucks5_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                        self.canvas_stucks5.place(x=580,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter5> 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter5,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                            
                            self.stucks5_picture = 'create_picture/stucks5_picture.png'

                            self.stucks5_open = Image.open(self.stucks5_picture)

                            self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                            self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                        
                        else:
                            self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                            self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                        
                        self.canvas_stucks5.place(x=580,y=310)

                elif 'stucks4' in l[0]:
                    if self.counter4 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter4,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                        
                        self.stucks4_picture = 'create_picture/stucks4_picture.png'

                        self.stucks4_open = Image.open(self.stucks4_picture)

                        self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                    
                    else:
                        self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                    self.canvas_stucks4.place(x=440,y=310)


                    if self.stucks5_count == 0:
                        self.stucks5_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                        self.canvas_stucks5.place(x=580,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter5> 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter5,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                            
                            self.stucks5_picture = 'create_picture/stucks5_picture.png'

                            self.stucks5_open = Image.open(self.stucks5_picture)

                            self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                            self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                        
                        else:
                            self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                            self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                        
                        self.canvas_stucks5.place(x=580,y=310)
                
                elif 'stucks6' in l[0]:
                    if self.counter6 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter6,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                        
                        self.stucks6_picture = 'create_picture/stucks6_picture.png'

                        self.stucks6_open = Image.open(self.stucks6_picture)

                        self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    else:
                        self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    self.canvas_stucks6.place(x=720,y=310)

                    if self.stucks5_count == 0:
                        self.stucks5_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                        self.canvas_stucks5.place(x=580,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter5> 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter5,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                            
                            self.stucks5_picture = 'create_picture/stucks5_picture.png'

                            self.stucks5_open = Image.open(self.stucks5_picture)

                            self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                            self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                        
                        else:
                            self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                            self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                        
                        self.canvas_stucks5.place(x=580,y=310)

                elif 'stucks7' in l[0]:
                    if self.counter7 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter7,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                        
                        self.stucks7_picture = 'create_picture/stucks7_picture.png'

                        self.stucks7_open = Image.open(self.stucks7_picture)

                        self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    else:
                        self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    self.canvas_stucks7.place(x=860,y=310)


                    if self.stucks5_count == 0:
                        self.stucks5_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)

                        self.canvas_stucks5.place(x=580,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter5> 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter5,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                            
                            self.stucks5_picture = 'create_picture/stucks5_picture.png'

                            self.stucks5_open = Image.open(self.stucks5_picture)

                            self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                            self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                        
                        else:
                            self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                            self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                        
                        self.canvas_stucks5.place(x=580,y=310)

            elif self.before_card == '.!canvas12':    
                if 'stucks1' in l[0]:
                    self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                    self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                    self.canvas_stucks1.place(x=20,y=310)

                    if self.stucks6_count == 0:
                        self.stucks6_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        self.canvas_stucks6.place(x=720,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter6 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter6,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                            
                            self.stucks6_picture = 'create_picture/stucks6_picture.png'

                            self.stucks6_open = Image.open(self.stucks6_picture)

                            self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                            self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        else:
                            self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                            self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        self.canvas_stucks6.place(x=720,y=310)

                elif 'stucks2' in l[0]:
                    if self.counter2 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,event)

                        backside_img = self.chain_backside_picture(self.counter2,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                    
                        self.stucks2_picture = 'create_picture/stucks2_picture.png'

                        self.stucks2_open = Image.open(self.stucks2_picture)

                        self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                        
                    else:
                        self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                    self.canvas_stucks2.place(x=160,y=310)
                
                    if self.stucks6_count == 0:
                        self.stucks6_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        self.canvas_stucks6.place(x=720,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter6 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter6,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                            
                            self.stucks6_picture = 'create_picture/stucks6_picture.png'

                            self.stucks6_open = Image.open(self.stucks6_picture)

                            self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                            self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        else:
                            self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                            self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        self.canvas_stucks6.place(x=720,y=310)

                elif 'stucks3' in l[0]:
                    if self.counter3 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter3,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                        
                        self.stucks3_picture = 'create_picture/stucks3_picture.png'

                        self.stucks3_open = Image.open(self.stucks3_picture)

                        self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                    
                    else:
                        self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                    self.canvas_stucks3.place(x=300,y=310)

                    if self.stucks6_count == 0:
                        self.stucks6_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        self.canvas_stucks6.place(x=720,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter6 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter6,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                            
                            self.stucks6_picture = 'create_picture/stucks6_picture.png'

                            self.stucks6_open = Image.open(self.stucks6_picture)

                            self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                            self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        else:
                            self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                            self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        self.canvas_stucks6.place(x=720,y=310)

                elif 'stucks4' in l[0]:
                    if self.counter4 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter4,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                        
                        self.stucks4_picture = 'create_picture/stucks4_picture.png'

                        self.stucks4_open = Image.open(self.stucks4_picture)

                        self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                    
                    else:
                        self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                    self.canvas_stucks4.place(x=440,y=310)


                    if self.stucks6_count == 0:
                        self.stucks6_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        self.canvas_stucks6.place(x=720,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter6 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter6,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                            
                            self.stucks6_picture = 'create_picture/stucks6_picture.png'

                            self.stucks6_open = Image.open(self.stucks6_picture)

                            self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                            self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        else:
                            self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                            self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        self.canvas_stucks6.place(x=720,y=310)
                
                elif 'stucks5' in l[0]:
                    if self.counter5> 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter5,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                        
                        self.stucks5_picture = 'create_picture/stucks5_picture.png'

                        self.stucks5_open = Image.open(self.stucks5_picture)

                        self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                    
                    else:
                        self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                    
                    self.canvas_stucks5.place(x=580,y=310)

                    if self.stucks6_count == 0:
                        self.stucks6_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        self.canvas_stucks6.place(x=720,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter6 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter6,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                            
                            self.stucks6_picture = 'create_picture/stucks6_picture.png'

                            self.stucks6_open = Image.open(self.stucks6_picture)

                            self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                            self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        else:
                            self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                            self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        self.canvas_stucks6.place(x=720,y=310)

                elif 'stucks7' in l[0]:
                    if self.counter7 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter7,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                        
                        self.stucks7_picture = 'create_picture/stucks7_picture.png'

                        self.stucks7_open = Image.open(self.stucks7_picture)

                        self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    else:
                        self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                    self.canvas_stucks7.place(x=860,y=310)


                    if self.stucks6_count == 0:
                        self.stucks6_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        self.canvas_stucks6.place(x=720,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter6 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter6,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                            
                            self.stucks6_picture = 'create_picture/stucks6_picture.png'

                            self.stucks6_open = Image.open(self.stucks6_picture)

                            self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                            self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        else:
                            self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                            self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                        self.canvas_stucks6.place(x=720,y=310)

            elif self.before_card == '.!canvas13':    
                if 'stucks1' in l[0]:
                    self.stucks1_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks1,self.stucks1_count), width=110 , height= 170 + (self.stucks1_count - 1) * 30)

                    self.canvas_stucks1.create_image(7,3,image=self.stucks1_img, tags='stucks1',anchor=tk.NW)

                    self.canvas_stucks1.place(x=20,y=310)

                    if self.stucks7_count == 0:
                        self.stucks7_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        self.canvas_stucks7.place(x=860,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter7 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter7,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                            
                            self.stucks7_picture = 'create_picture/stucks7_picture.png'

                            self.stucks7_open = Image.open(self.stucks7_picture)

                            self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                            self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        else:
                            self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                            self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        self.canvas_stucks7.place(x=860,y=310)

                elif 'stucks2' in l[0]:
                    if self.counter2 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks2,self.stucks2_count,self.counter2,event)

                        backside_img = self.chain_backside_picture(self.counter2,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks2_picture.png')
                    
                        self.stucks2_picture = 'create_picture/stucks2_picture.png'

                        self.stucks2_open = Image.open(self.stucks2_picture)

                        self.stucks2_img = tk.PhotoImage(file = self.stucks2_picture, width=110 , height=self.stucks2_open.height)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)
                        
                    else:
                        self.stucks2_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks2,self.stucks2_count), width=110 , height= 170 + (self.stucks2_count - 1) * 30)

                        self.canvas_stucks2.create_image(7,3,image=self.stucks2_img, tags='stucks2',anchor=tk.NW)

                    self.canvas_stucks2.place(x=160,y=310)
                
                    if self.stucks7_count == 0:
                        self.stucks7_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        self.canvas_stucks7.place(x=860,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter7 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter7,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                            
                            self.stucks7_picture = 'create_picture/stucks7_picture.png'

                            self.stucks7_open = Image.open(self.stucks7_picture)

                            self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                            self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        else:
                            self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                            self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        self.canvas_stucks7.place(x=860,y=310)

                elif 'stucks3' in l[0]:
                    if self.counter3 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks3,self.stucks3_count,self.counter3,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter3,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks3_picture.png')
                        
                        self.stucks3_picture = 'create_picture/stucks3_picture.png'

                        self.stucks3_open = Image.open(self.stucks3_picture)

                        self.stucks3_img = tk.PhotoImage(file = self.stucks3_picture, width=110 , height=self.stucks3_open.height)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)
                    
                    else:
                        self.stucks3_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks3,self.stucks3_count), width=110 , height= 170 + (self.stucks3_count - 1) * 30)

                        self.canvas_stucks3.create_image(7,3,image=self.stucks3_img, tags='stucks3',anchor=tk.NW)

                    self.canvas_stucks3.place(x=300,y=310)

                    if self.stucks7_count == 0:
                        self.stucks7_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        self.canvas_stucks7.place(x=860,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter7 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter7,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                            
                            self.stucks7_picture = 'create_picture/stucks7_picture.png'

                            self.stucks7_open = Image.open(self.stucks7_picture)

                            self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                            self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        else:
                            self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                            self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        self.canvas_stucks7.place(x=860,y=310)

                elif 'stucks4' in l[0]:
                    if self.counter4 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks4,self.stucks4_count,self.counter4,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter4,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks4_picture.png')
                        
                        self.stucks4_picture = 'create_picture/stucks4_picture.png'

                        self.stucks4_open = Image.open(self.stucks4_picture)

                        self.stucks4_img = tk.PhotoImage(file = self.stucks4_picture, width=110 , height=self.stucks4_open.height)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)
                    
                    else:
                        self.stucks4_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks4,self.stucks4_count), width=110 , height= 170 + (self.stucks4_count - 1) * 30)

                        self.canvas_stucks4.create_image(7,3,image=self.stucks4_img, tags='stucks4',anchor=tk.NW)

                    self.canvas_stucks4.place(x=440,y=310)


                    if self.stucks7_count == 0:
                        self.stucks7_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        self.canvas_stucks7.place(x=860,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter7 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter7,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                            
                            self.stucks7_picture = 'create_picture/stucks7_picture.png'

                            self.stucks7_open = Image.open(self.stucks7_picture)

                            self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                            self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        else:
                            self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                            self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        self.canvas_stucks7.place(x=860,y=310)
                
                elif 'stucks5' in l[0]:
                    if self.counter5> 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks5,self.stucks5_count,self.counter5,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter5,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks5_picture.png')
                        
                        self.stucks5_picture = 'create_picture/stucks5_picture.png'

                        self.stucks5_open = Image.open(self.stucks5_picture)

                        self.stucks5_img = tk.PhotoImage(file = self.stucks5_picture, width=110 , height=self.stucks5_open.height)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                    
                    else:
                        self.stucks5_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks5,self.stucks5_count), width=110 , height= 170 + (self.stucks5_count - 1) * 30)

                        self.canvas_stucks5.create_image(7,3,image=self.stucks5_img, tags='stucks5',anchor=tk.NW)
                    
                    self.canvas_stucks5.place(x=580,y=310)

                    if self.stucks7_count == 0:
                        self.stucks7_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        self.canvas_stucks7.place(x=860,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter7 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter7,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                            
                            self.stucks7_picture = 'create_picture/stucks7_picture.png'

                            self.stucks7_open = Image.open(self.stucks7_picture)

                            self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                            self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        else:
                            self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                            self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        self.canvas_stucks7.place(x=860,y=310)

                elif 'stucks6' in l[0]:
                    if self.counter6 > 0:
                        openstucks_img = self.create_chain_stucks(self.card_stucks6,self.stucks6_count,self.counter6,event)
                                                                
                        backside_img = self.chain_backside_picture(self.counter6,event)

                        self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks6_picture.png')
                        
                        self.stucks6_picture = 'create_picture/stucks6_picture.png'

                        self.stucks6_open = Image.open(self.stucks6_picture)

                        self.stucks6_img = tk.PhotoImage(file = self.stucks6_picture, width=110 , height=self.stucks6_open.height)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    else:
                        self.stucks6_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks6,self.stucks6_count), width=110 , height= 170 + (self.stucks6_count - 1) * 30)

                        self.canvas_stucks6.create_image(7,3,image=self.stucks6_img, tags='stucks6',anchor=tk.NW)

                    self.canvas_stucks6.place(x=720,y=310)


                    if self.stucks7_count == 0:
                        self.stucks7_img = tk.PhotoImage(file = 'tramp_picture/start.png', width=120 , height=170)

                        self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        self.canvas_stucks7.place(x=860,y=310)
                        #受付の解除
                        self.canvas_arrow_stuck_img = None
                        
                        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

                        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

                        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

                        self.canvas_club.tag_unbind('club','<ButtonPress>')

                        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

                        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

                        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

                        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

                        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

                        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

                        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

                        #再受付
                        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

                        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

                        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

                        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

                    else:
                        if self.counter7 > 0:
                            openstucks_img = self.create_chain_stucks(self.card_stucks7,self.stucks7_count,self.counter7,self.before_card)
                                                                    
                            backside_img = self.chain_backside_picture(self.counter7,self.before_card)

                            self.create_stucks_picture(openstucks_img,backside_img).save('create_picture/stucks7_picture.png')
                            
                            self.stucks7_picture = 'create_picture/stucks7_picture.png'

                            self.stucks7_open = Image.open(self.stucks7_picture)

                            self.stucks7_img = tk.PhotoImage(file = self.stucks7_picture, width=110 , height=self.stucks7_open.height)

                            self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        else:
                            self.stucks7_img = tk.PhotoImage(file = self.create_chain_stucks(self.card_stucks7,self.stucks7_count), width=110 , height= 170 + (self.stucks7_count - 1) * 30)

                            self.canvas_stucks7.create_image(7,3,image=self.stucks7_img, tags='stucks7',anchor=tk.NW)

                        self.canvas_stucks7.place(x=860,y=310)

        #受付の解除
        self.canvas_arrow_stuck_img = None

        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

        self.canvas_club.tag_unbind('club','<ButtonPress>')

        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

        #再受付
        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))     

    def create_first_stucks_picture(self,open_img, n, picture_count):
        im1 = Image.open(open_img)
        chain_back_side_picture = self.first_chain_backside_picture(n,picture_count)
        im2 = Image.open(chain_back_side_picture)
        dst = Image.new('RGB', (im1.width, im1.height + im2.height))
        dst.paste(im2, (0, 0))
        dst.paste(im1, (0, im2.height))
        return dst
    
    def create_stucks_picture(self,open_img,backside_img):
        im1 = Image.open(open_img)
        im2 = Image.open(backside_img)
        dst = Image.new('RGB', (im1.width, im1.height + im2.height))
        dst.paste(im2, (0, 0))
        dst.paste(im1, (0, im2.height))
        return dst
        
    
    def create_chain_stucks(self,card_stucks,stucks_count,backside_num = None,event = None):
        if backside_num == None:

            i = 0 

            j = 0

            n = stucks_count - 1

            img_width = 110

            img_height = (stucks_count - 1) * 30 + 155

            img = Image.new('RGB',(img_width,img_height))

            for t in range(n):

                cropped_image = Image.open('cropped_picture/' + card_stucks[i] + '.png')

                img.paste(cropped_image,(0,j))

                j = j + cropped_image.height

                i = i + 1

            ''' while i < stucks_count-1:

                    cropped_image = Image.open('cropped_picture/' + card_stucks[i] + '.png')

                    img.paste = (cropped_image,(0,j))

                    j = j + cropped_image.height

                    i = i + 1
            '''

            open_stucks_image = Image.open('tramp_picture/' + card_stucks[i] + '.png')

            img.paste(open_stucks_image,(0,j))

            img.save('create_picture/chain_stucks1.png')

            open_stucks_picture = 'create_picture/chain_stucks1.png'

            return open_stucks_picture
        
        else:
            i = backside_num 

            j = 0

            n = stucks_count - (backside_num+1)

            img_width = 110

            img_height = n * 30 + 155

            img = Image.new('RGB',(img_width,img_height))

            if n > 0:
                for t in range(n):

                    cropped_image = Image.open('cropped_picture/' + card_stucks[i] + '.png')

                    img.paste(cropped_image,(0,j))

                    j = j + cropped_image.height

                    i = i + 1

                ''' while i < stucks_count-1:

                        cropped_image = Image.open('cropped_picture/' + card_stucks[i] + '.png')

                        img.paste = (cropped_image,(0,j))

                        j = j + cropped_image.height

                        i = i + 1
                '''
            open_stucks_image = Image.open('tramp_picture/' + card_stucks[i] + '.png')

            img.paste(open_stucks_image,(0,j))

            if event == '.!canvas8':

                img.save('create_picture/chain_stucks2.png')

                open_stucks_picture = 'create_picture/chain_stucks2.png'

            elif event== '.!canvas9':

                img.save('create_picture/chain_stucks3.png')

                open_stucks_picture = 'create_picture/chain_stucks3.png'

            elif event == '.!canvas10':

                img.save('create_picture/chain_stucks4.png')

                open_stucks_picture = 'create_picture/chain_stucks4.png'

            elif event == '.!canvas11':

                img.save('create_picture/chain_stucks5.png')

                open_stucks_picture = 'create_picture/chain_stucks5.png'

            elif event == '.!canvas12':

                img.save('create_picture/chain_stucks6.png')

                open_stucks_picture = 'create_picture/chain_stucks6.png'

            elif event == '.!canvas13':

                img.save('create_picture/chain_stucks7.png')

                open_stucks_picture = 'create_picture/chain_stucks7.png'
            
            elif str(event.widget) == '.!canvas8':

                img.save('create_picture/chain_stucks2.png')

                open_stucks_picture = 'create_picture/chain_stucks2.png'

            elif str(event.widget) == '.!canvas9':

                img.save('create_picture/chain_stucks3.png')

                open_stucks_picture = 'create_picture/chain_stucks3.png'

            elif str(event.widget) == '.!canvas10':

                img.save('create_picture/chain_stucks4.png')

                open_stucks_picture = 'create_picture/chain_stucks4.png'

            elif str(event.widget) == '.!canvas11':

                img.save('create_picture/chain_stucks5.png')

                open_stucks_picture = 'create_picture/chain_stucks5.png'

            elif str(event.widget) == '.!canvas12':

                img.save('create_picture/chain_stucks6.png')

                open_stucks_picture = 'create_picture/chain_stucks6.png'

            elif str(event.widget) == '.!canvas13':

                img.save('create_picture/chain_stucks7.png')

                open_stucks_picture = 'create_picture/chain_stucks7.png'


            return open_stucks_picture


    def first_chain_backside_picture(self,n,picture_count):
        i = 0
        img2 = 'cropped_picture/back_side.png'
        cropped_image = Image.open(img2)
        img_width = 110
        img_height = 0
        for t in range(n):
            img_height = img_height + cropped_image.height
        img = Image.new('RGB',(img_width,img_height))
        for t in range(n):
            img.paste(cropped_image,(0,i))
            i = i + cropped_image.height
        if picture_count < 8:
                img.save('create_picture/chain_backside_picture' + str(picture_count) +'.png')
                chain_backside_picture = 'create_picture/chain_backside_picture' + str(picture_count) +'.png'

        return chain_backside_picture
    
    def chain_backside_picture(self,n,event):
        i = 0
        img2 = 'cropped_picture/back_side.png'
        cropped_image = Image.open(img2)
        img_width = 110
        img_height = 0
        for t in range(n):
            img_height = img_height + cropped_image.height
        img = Image.new('RGB',(img_width,img_height))
        for t in range(n):
            img.paste(cropped_image,(0,i))
            i = i + cropped_image.height
        
        if event == '.!canvas8':

            img.save('create_picture/chain_backside_picture2.png')

            chain_backside_picture = 'create_picture/chain_backside_picture2.png'

        elif event == '.!canvas9':

            img.save('create_picture/chain_backside_picture3.png')
            
            chain_backside_picture = 'create_picture/chain_backside_picture3.png'

        elif event == '.!canvas10':

            img.save('create_picture/chain_backside_picture4.png')
            
            chain_backside_picture = 'create_picture/chain_backside_picture4.png'

        elif event == '.!canvas11':

            img.save('create_picture/chain_backside_picture5.png')
            
            chain_backside_picture = 'create_picture/chain_backside_picture5.png'

        elif event == '.!canvas12':

            img.save('create_picture/chain_backside_picture6.png')
            
            chain_backside_picture = 'create_picture/chain_backside_picture6.png'

        elif event == '.!canvas13':

            img.save('create_picture/chain_backside_picture7.png')
            
            chain_backside_picture = 'create_picture/chain_backside_picture7.png'
            
        elif str(event.widget) == '.!canvas8':

            img.save('create_picture/chain_backside_picture2.png')

            chain_backside_picture = 'create_picture/chain_backside_picture2.png'

        elif str(event.widget) == '.!canvas9':

            img.save('create_picture/chain_backside_picture3.png')
            
            chain_backside_picture = 'create_picture/chain_backside_picture3.png'

        elif str(event.widget) == '.!canvas10':

            img.save('create_picture/chain_backside_picture4.png')
            
            chain_backside_picture = 'create_picture/chain_backside_picture4.png'

        elif str(event.widget) == '.!canvas11':

            img.save('create_picture/chain_backside_picture5.png')
            
            chain_backside_picture = 'create_picture/chain_backside_picture5.png'

        elif str(event.widget) == '.!canvas12':

            img.save('create_picture/chain_backside_picture6.png')
            
            chain_backside_picture = 'create_picture/chain_backside_picture6.png'

        elif str(event.widget) == '.!canvas13':

            img.save('create_picture/chain_backside_picture7.png')
            
            chain_backside_picture = 'create_picture/chain_backside_picture7.png'

        return chain_backside_picture
            
    def create_backside_image(self):
        backside_img = tk.PhotoImage(file = 'tramp_picture/back_side.png',width=120,height=170)
        return backside_img

    def create_stucks_image(self,stucks):
        image = Image.open(stucks)
        deck_stucks_img = tk.PhotoImage(file = stucks, width=110 , height=image.height)
        return deck_stucks_img

    def create_spade_image(self,master,event):
        print(event.widget)
        print(self.card_deck[self.deck_count-1])
        if not self.card_deck[self.deck_count-1].startswith('♠'):
            #受付の解除
            self.canvas_arrow_deck_open_img = None

            self.canvas_spade.tag_unbind('spade','<ButtonPress>')

            self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

            self.canvas_dia.tag_unbind('dia','<ButtonPress>')

            self.canvas_club.tag_unbind('club','<ButtonPress>')

            self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

            self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

            self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

            self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

            self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

            self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

            self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

            #再受付
            self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

            self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

            self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

            self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

            self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

        elif self.spade_suit[0] == '':
            if self.card_deck[self.deck_count-1].endswith('A'):
                self.spade_suit[self.spade_suit_count] = self.card_deck[self.deck_count-1]
                self.card_deck[self.deck_count-1] = ''
                self.spade_suit_count += 1

        else:
            if spade_table[self.spade_suit_count] == self.card_deck[self.deck_count-1]:
                self.spade_suit[self.spade_suit_count] = self.card_deck[self.deck_count-1]
                self.card_deck[self.deck_count-1] = ''
                self.spade_suit_count +=1

        if self.spade_suit_count > 0:
            self.spade = 'tramp_picture/' + self.spade_suit[self.spade_suit_count-1] + '.png'
            self.spade_img = tk.PhotoImage(file = self.spade, width=110 , height=155)
            self.canvas_spade.create_image(7,7.5,image=self.spade_img, tags='spade',anchor=tk.NW)
            self.canvas_spade.place(x=400,y=30)
            self.deck_open_img = None
            self.canvas_deck_open.tag_unbind('open','<ButtonPress>')

        if self.spade_suit[12] == '♠K' and self.hurt_suit[12] == '♥K' and self.dia_suit[12] == '♦K' and self.club_suit[12] == '♣K':
            sub_window = tk.Toplevel()
            sub_window.title('おめでとうございます！')
            sub_window.geometry("300x150+750+450")
            sub_window['bg'] = 'white'
            message = tk.Label(sub_window,text='ゲームクリア！',font=("MSゴシック","20","bold"),bg='white')
            message.place(x=60,y=50)

        #受付の解除
        self.canvas_arrow_deck_open_img = None

        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

        self.canvas_club.tag_unbind('club','<ButtonPress>')

        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

        #再受付
        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))
       
    def create_hurt_image(self,master,event):
        print(event.widget)
        print(self.card_deck[self.deck_count-1])
        if not self.card_deck[self.deck_count-1].startswith('♥'):
            #受付の解除
            self.canvas_arrow_deck_open_img = None

            self.canvas_spade.tag_unbind('spade','<ButtonPress>')

            self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

            self.canvas_dia.tag_unbind('dia','<ButtonPress>')

            self.canvas_club.tag_unbind('club','<ButtonPress>')

            self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

            self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

            self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

            self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

            self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

            self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

            self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

            #再受付
            self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

            self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

            self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

            self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

            self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

        elif self.hurt_suit[0] == '':
            if self.card_deck[self.deck_count-1].endswith('A'):
                self.hurt_suit[self.hurt_suit_count] = self.card_deck[self.deck_count-1]
                self.card_deck[self.deck_count-1] = ''
                self.hurt_suit_count += 1

        else:
            if hurt_table[self.hurt_suit_count] == self.card_deck[self.deck_count-1]:
                self.hurt_suit[self.hurt_suit_count] = self.card_deck[self.deck_count-1]
                self.card_deck[self.deck_count-1] = ''
                self.hurt_suit_count +=1

        if self.hurt_suit_count > 0:
            self.hurt = 'tramp_picture/' + self.hurt_suit[self.hurt_suit_count-1] + '.png'
            self.hurt_img = tk.PhotoImage(file = self.hurt, width=110 , height=155)
            self.canvas_hurt.create_image(7,7.5,image=self.hurt_img, tags='hurt',anchor=tk.NW)
            self.canvas_hurt.place(x=540,y=30)
            self.deck_open_img = None
            self.canvas_deck_open.tag_unbind('open','<ButtonPress>')

        if self.spade_suit[12] == '♠K' and self.hurt_suit[12] == '♥K' and self.dia_suit[12] == '♦K' and self.club_suit[12] == '♣K':
            sub_window = tk.Toplevel()
            sub_window.title('おめでとうございます！')
            sub_window.geometry("300x150+750+450")
            sub_window['bg'] = 'white'
            message = tk.Label(sub_window,text='ゲームクリア！',font=("MSゴシック","20","bold"),bg='white')
            message.place(x=60,y=50)

        #受付の解除
        self.canvas_arrow_deck_open_img = None

        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

        self.canvas_club.tag_unbind('club','<ButtonPress>')

        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

        #再受付
        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

    def create_dia_image(self,master,event):
        print(event.widget)
        print(self.card_deck[self.deck_count-1])
        if not self.card_deck[self.deck_count-1].startswith('♦'):
            #受付の解除
            self.canvas_arrow_deck_open_img = None

            self.canvas_spade.tag_unbind('spade','<ButtonPress>')

            self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

            self.canvas_dia.tag_unbind('dia','<ButtonPress>')

            self.canvas_club.tag_unbind('club','<ButtonPress>')

            self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

            self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

            self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

            self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

            self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

            self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

            self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

            #再受付
            self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

            self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

            self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

            self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

            self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

        elif self.dia_suit[0] == '':
            if self.card_deck[self.deck_count-1].endswith('A'):
                self.dia_suit[self.dia_suit_count] = self.card_deck[self.deck_count-1]
                self.card_deck[self.deck_count-1] = ''
                self.dia_suit_count += 1

        else:
            if dia_table[self.dia_suit_count] == self.card_deck[self.deck_count-1]:
                self.dia_suit[self.dia_suit_count] = self.card_deck[self.deck_count-1]
                self.card_deck[self.deck_count-1] = ''
                self.dia_suit_count +=1

        if self.dia_suit_count > 0:
            self.dia = 'tramp_picture/' + self.dia_suit[self.dia_suit_count-1] + '.png'
            self.dia_img = tk.PhotoImage(file = self.dia, width=110 , height=155)
            self.canvas_dia.create_image(7,7.5,image=self.dia_img, tags='dia',anchor=tk.NW)
            self.canvas_dia.place(x=680,y=30)
            self.deck_open_img = None
            self.canvas_deck_open.tag_unbind('open','<ButtonPress>')

        if self.spade_suit[12] == '♠K' and self.hurt_suit[12] == '♥K' and self.dia_suit[12] == '♦K' and self.club_suit[12] == '♣K':
            sub_window = tk.Toplevel()
            sub_window.title('おめでとうございます！')
            sub_window.geometry("300x150+750+450")
            sub_window['bg'] = 'white'
            message = tk.Label(sub_window,text='ゲームクリア！',font=("MSゴシック","20","bold"),bg='white')
            message.place(x=60,y=50)

        #受付の解除
        self.canvas_arrow_deck_open_img = None

        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

        self.canvas_club.tag_unbind('club','<ButtonPress>')

        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

        #再受付
        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

    def create_club_image(self,master,event):
        print(event.widget)
        print(self.card_deck[self.deck_count-1])
        if not self.card_deck[self.deck_count-1].startswith('♣'):
            #受付の解除
            self.canvas_arrow_deck_open_img = None

            self.canvas_spade.tag_unbind('spade','<ButtonPress>')

            self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

            self.canvas_dia.tag_unbind('dia','<ButtonPress>')

            self.canvas_club.tag_unbind('club','<ButtonPress>')

            self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

            self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

            self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

            self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

            self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

            self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

            self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

            #再受付
            self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

            self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

            self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

            self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

            self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

            self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))

        elif self.club_suit[0] == '':
            if self.card_deck[self.deck_count-1].endswith('A'):
                self.club_suit[self.club_suit_count] = self.card_deck[self.deck_count-1]
                self.card_deck[self.deck_count-1] = ''
                self.club_suit_count += 1

        else:
            if club_table[self.club_suit_count] == self.card_deck[self.deck_count-1]:
                self.club_suit[self.club_suit_count] = self.card_deck[self.deck_count-1]
                self.card_deck[self.deck_count-1] = ''
                self.club_suit_count +=1

        if self.club_suit_count > 0:
            self.club = 'tramp_picture/' + self.club_suit[self.club_suit_count-1] + '.png'
            self.club_img = tk.PhotoImage(file = self.club, width=110 , height=155)
            self.canvas_club.create_image(7,7.5,image=self.club_img, tags='club',anchor=tk.NW)
            self.canvas_club.place(x=820,y=30)
            self.deck_open_img = None
            self.canvas_deck_open.tag_unbind('open','<ButtonPress>')

        if self.spade_suit[12] == '♠K' and self.hurt_suit[12] == '♥K' and self.dia_suit[12] == '♦K' and self.club_suit[12] == '♣K':
            sub_window = tk.Toplevel()
            sub_window.title('おめでとうございます！')
            sub_window.geometry("300x150+750+450")
            sub_window['bg'] = 'white'
            message = tk.Label(sub_window,text='ゲームクリア！',font=("MSゴシック","20","bold"),bg='white')
            message.place(x=60,y=50)

        #受付の解除
        self.canvas_arrow_deck_open_img = None
        
        self.canvas_spade.tag_unbind('spade','<ButtonPress>')

        self.canvas_hurt.tag_unbind('hurt','<ButtonPress>')

        self.canvas_dia.tag_unbind('dia','<ButtonPress>')

        self.canvas_club.tag_unbind('club','<ButtonPress>')

        self.canvas_stucks1.tag_unbind('stucks1','<ButtonPress>')

        self.canvas_stucks2.tag_unbind('stucks2','<ButtonPress>')

        self.canvas_stucks3.tag_unbind('stucks3','<ButtonPress>')

        self.canvas_stucks4.tag_unbind('stucks4','<ButtonPress>')

        self.canvas_stucks5.tag_unbind('stucks5','<ButtonPress>')

        self.canvas_stucks6.tag_unbind('stucks6','<ButtonPress>')

        self.canvas_stucks7.tag_unbind('stucks7','<ButtonPress>')

        #再受付
        self.canvas_deck.tag_bind('deck','<ButtonPress>',partial(self.deck_click_event,self))

        self.canvas_stucks1.tag_bind('stucks1','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks2.tag_bind('stucks2','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks3.tag_bind('stucks3','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks4.tag_bind('stucks4','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks5.tag_bind('stucks5','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks6.tag_bind('stucks6','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_stucks7.tag_bind('stucks7','<ButtonPress>',partial(self.stucks_click_event,self))

        self.canvas_spade.tag_bind('spade','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_hurt.tag_bind('hurt','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_dia.tag_bind('dia','<ButtonPress>',partial(self.suit_click_event,self))

        self.canvas_club.tag_bind('club','<ButtonPress>',partial(self.suit_click_event,self))


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('ソリティア')

        self.configure(bg='green')

        self.geometry('1000x1080+910+0')

        self.resizable(False,False)

        game = game_field(self)

        game.mainloop()
            
        

if __name__ == '__main__':
    app = Application()