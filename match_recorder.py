from tkinter import *
import numpy as np
import os

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("player", help="The Player whose game has to analysed")
parser.add_argument("opponent", help="Name of the Opponent whose game need to be analysed")
args = parser.parse_args()

playername = args.player
opponentname = args.opponent


class Window(Frame):
    
    
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        
        self.pos = ['a','b','c','d','e','f','g','h','i'] 
        self.pla = ['3','2','1','6','5','4','9','8','7']
        
        self.prev_highlight = None
        
        self.player = playername
        self.opponent = opponentname
        
        #Check if folder exists,if not create folder
        
        directory = "data/"+playername
        if not os.path.exists(directory):
            os.makedirs(directory)
            print("Folder created")
            
        #check if file exists if not create file
        file = directory+"/"+opponentname+".txt"
        try:
            self.file = open(file, 'ab+')
            print("File Opened")
        except IOError:
            print("File Does not exist")
            #file = open(file, 'w')
            #print("File created")
        
        
        self.previous_word = "hee haw"
        self.init_window()
    
    def init_window(self):
        self.pack(fill=BOTH, expand=1)
        w = 15
        h = 6
        
        
        
        Button1 = Button(self, text="",height = h,width=w,bg="white")
        Button1.text = self.pos[6]
        Button1.bind('<Button-1>', self.click)
        Button1.bind('<Button-3>',self.rightClick)
        Button1.grid(row=0,column=1)
        
        Button2 = Button(self, text="",height = h,width=w,bg="white")
        Button2.text = self.pos[7]
        Button2.bind('<Button-1>', self.click)
        Button2.bind('<Button-3>',self.rightClick)
        Button2.grid(row=0,column=2)
        
        Button3 = Button(self, text="",height = h,width=w,bg="white")
        Button3.text = self.pos[8]
        Button3.bind('<Button-1>', self.click)
        Button3.bind('<Button-3>',self.rightClick)
        Button3.grid(row=0,column=3)
        
        Button4 = Button(self, text="",height = h,width=w,bg="white")
        Button4.text = self.pos[3]
        Button4.bind('<Button-1>', self.click)
        Button4.bind('<Button-3>',self.rightClick)
        Button4.grid(row=1,column=1)
        
        
        Button5 = Button(self, text=self.player,height = h,width=w,bg="white")
        Button5.text = self.pos[4]
        Button5.bind('<Button-1>', self.click)
        Button5.bind('<Button-3>',self.rightClick)
        Button5.grid(row=1,column=2)
        
        Button6 = Button(self, text="",height = h,width=w,bg="white")
        Button6.text = self.pos[5]
        Button6.bind('<Button-1>', self.click)
        Button6.grid(row=1,column=3)
        Button6.bind('<Button-3>',self.rightClick)
        
        Button7 = Button(self, text="",height = h,width=w,bg="white")
        Button7.text = self.pos[0]
        Button7.bind('<Button-1>', self.click)
        Button7.bind('<Button-3>',self.rightClick)
        Button7.grid(row=2,column=1)
        
        
        Button8 = Button(self, text="",height = h,width=w,bg="white")
        Button8.text = self.pos[1]
        Button8.bind('<Button-1>', self.click)
        Button8.bind('<Button-3>',self.rightClick)
        Button8.grid(row=2,column=2)
        
        Button9 = Button(self, text="",height = h,width=w,bg="white")
        Button9.text = self.pos[2]
        Button9.bind('<Button-1>', self.click)
        Button9.bind('<Button-3>',self.rightClick)
        Button9.grid(row=2,column=3)
        
        Button10 = Button(self, text="",height = h,width=w,bg="white")
        Button10.text = self.pla[2]
        Button10.bind('<Button-1>', self.click)
        Button10.bind('<Button-3>',self.rightClick)
        Button10.grid(row=3,column=1)
        
        
        Button11 = Button(self, text="",height = h,width=w,bg="white")
        Button11.text = self.pla[1]
        Button11.bind('<Button-1>', self.click)
        Button11.bind('<Button-3>',self.rightClick)
        Button11.grid(row=3,column=2)
    
        Button12 = Button(self, text="",height = h,width=w,bg="white")
        Button12.text = self.pla[0]
        Button12.bind('<Button-1>', self.click)
        Button12.bind('<Button-3>',self.rightClick)
        Button12.grid(row=3,column=3)
        
        Button13 = Button(self, text="",height = h,width=w,bg="white")
        Button13.text = self.pla[5]
        Button13.bind('<Button-1>', self.click)
        Button13.bind('<Button-3>',self.rightClick)
        Button13.grid(row=4,column=1)
        
        
        Button14 = Button(self, text=self.opponent,height = h,width=w,bg="white")
        Button14.text = self.pla[4]
        Button14.bind('<Button-1>', self.click)
        Button14.bind('<Button-3>',self.rightClick)
        Button14.grid(row=4,column=2)
        
        Button15 = Button(self, text="",height = h,width=w,bg="white")
        Button15.text = self.pla[3]
        Button15.bind('<Button-1>', self.click)
        Button15.bind('<Button-3>',self.rightClick)
        Button15.grid(row=4,column=3)
        
        Button16 = Button(self, text="",height = h,width=w,bg="white")
        Button16.text = self.pla[8]
        Button16.bind('<Button-1>', self.click)
        Button16.bind('<Button-3>',self.rightClick)
        Button16.grid(row=5,column=1)
        
        
        Button17 = Button(self, text="",height = h,width=w,bg="white")
        Button17.text = self.pla[7]
        Button17.bind('<Button-1>', self.click)
        Button17.bind('<Button-3>',self.rightClick)
        Button17.grid(row=5,column=2)
        
        Button18 = Button(self, text="",height = h,width=w,bg="white")
        Button18.text = self.pla[6]
        Button18.bind('<Button-1>', self.click)
        Button18.bind('<Button-3>',self.rightClick)
        Button18.grid(row=5,column=3)
        
        Button_switch = Button(self,text="SWITCH SIDES",height=h,width=w)
        Button_switch.bind('<Button-1>',self.switch)
        Button_switch.grid(row=0,column=4)
        
        
        Button_won = Button(self,text="WON",height=h,width=w)
        Button_won.bind('<Button-1>',self.click)
        Button_won.bind('<Button-3>',self.rightClick)
        Button_won.text = "won"
        Button_won.grid(row=2,column=4)
        
        Button_lost = Button(self,text="LOST",height=h,width=w)
        Button_lost.bind('<Button-1>',self.click)
        Button_lost.bind('<Button-3>',self.rightClick)
        Button_lost.text = "lost"
        Button_lost.grid(row=3,column=4)
        
        Button_save = Button(self,text="SAVE",height=h,width=w)
        Button_save.bind('<Button-1>',self.save)
        Button_save.grid(row=1,column=4)
        
        
    def click(self,event):
        
        self.write_to_file(event.widget.text)
        
        if self.prev_highlight:
            self.prev_highlight.configure(bg="white")
        event.widget.configure(bg="green")
        self.prev_highlight = event.widget
        
    def rightClick(self,event):
        self.write_to_file(event.widget.text,rightclick=True)
    
        if self.prev_highlight:
            self.prev_highlight.configure(bg="white")
        event.widget.configure(bg="green")
        self.prev_highlight = event.widget
        
    def switch(self,event):
        #switching button ids
        temp = self.pla
        self.pla = self.pos
        self.pos = temp
        #switching player names
        temp = self.player
        self.player = self.opponent
        self.opponent = temp
        
        print("switched")
        self.init_window()
        
        
    def save(self,event):
        self.file.close()
        
    def write_to_file(self,word,rightclick=False):
        pos = ['a','b','c','d','e','f','g','h','i'] 
        pla = ['3','2','1','6','5','4','9','8','7']
        if self.previous_word in pla:
            x = "pla"
        elif self.previous_word in pos:
            x = "pos"
        
        if not rightclick:
            if word in self.pos or word in self.pla:
                
                if self.previous_word==word:
                    self.file.write(("_").encode('ascii'))
                else:
                    self.file.write((" "+word).encode('ascii'))

            else:
                self.file.write((" "+x+"fo"+word+"\n").encode('ascii'))#this is forced error
        else:
            if word in self.pos or word in self.pla:
                
                if self.previous_word==word:
                    self.file.write(("_").encode('ascii'))
                else:
                    self.file.write((" "+word+"b").encode('ascii'))
    
                    
            else:
                self.file.write((" "+x+"ufo"+word+"\n").encode('ascii'))#this is unforced error
                
        self.previous_word = word  

root = Tk()

#size of the window
root.geometry("500x600")

app = Window(root)

root.mainloop()
