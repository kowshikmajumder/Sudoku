import tkinter
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import Tk
from tkinter import Frame
import random
import os
import sys
'''
x=colomn
y=row
z=block
'''
levelnum=7

def aboutf():
    aboutw=tkinter.Tk()
    aboutw.title('ABOUT THE GAME')
    al=tkinter.Label(aboutw,text='ASK KOWSHIK MAJUMDER').pack(fill=tkinter.BOTH)
    aclose=tkinter.Button(aboutw,text='CLOSE',bg='black',fg='white',command=aboutw.destroy).pack(anchor=tkinter.E)
    aboutw.mainloop()

def helpf():
    helpw=tkinter.Tk()
    helpw.title('HELP')
    al=tkinter.Label(helpw,text='ASK HELP KOWSHIK MAJUMDER').pack(fill=tkinter.BOTH)
    aclose=tkinter.Button(helpw,text='CLOSE',bg='black',fg='white',command=helpw.destroy).pack(anchor=tkinter.E)

class newgame():
    def __init__(self):
        file = open("output.txt","w")
        global levelnum
        self.level=levelnum
        self.firsts=0
        self.selectednum=-1
        self.playwindow =Tk()
        color=['white','red','green','yellow','blue','black']
        # 6 colors
        self.win =0
        self.block=[
            
                #z=9
                                #z=9
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                
            ]

        self.solvef()
        a=0
        while(a<9):
            b=0
            while(b<9):
            
                file.write(str(self.block[b][a]))
                file.write(' ')
                #print(str(i)+'\n')
                b=b+1
            file.write('\n')    
            a=a+1
        file.close()   
        
        x=0
        y=0
        z=0
    
        zi=0
        self.number=0
        self.frame=Frame(self.playwindow)
        while(y<9):
            x=0
            while(x<9):
        
                #probability is used to set the difficulty ....
                proba=random.randrange(1,11)
                #st=str(x)+str(y)+str(z)+str(ra)
                #st=str(X)
                #st='  '+str(y)+'  '
                #st=str(ra)
                #test
                #st='1'
                #ch=is changable
                #st=the text in the cell
                ch=1
                z=self.zfunction(x,y)
                if(proba<self.level):
                    ch=0
                    st=str(self.block[x][y])
                else:
                    ch=1
                
                    st='?'
                #st=str(self.block[x][y])    
                self.block[x][y]=Button(self.frame,text=st,bg=color[z%6],fg=color[-(z%6+1)],command=lambda a=x ,b=y ,ch1=ch: self.logicfunction(a,b,ch1),font=8)
                #print(str(self.block[x][y]))
                if(ch==0):
                    self.block[x][y].config(underline=0)
                
            #command=lambda a=x ,b=y: self.logicfunction(a,b,1),
                self.block[x][y].grid(row=y,column=x)
                
                x=x+1
            y=y+1

            #print('x=',x,'y=',y,'z=',z,'\n')
        
        #x=0
        #y=0
        #i=0
        #while(x<9 or y<10)and i<81:
            #st=str(x)+str(y)+str(z)+str(ra)
            #st=str(X)
            #st='  '+str(y)+'  '
            #st=str(ra)
            #test
            #st='1'
            
            #if(self.block[x][y].cget('text')=='0'):
                #self.block[x][y].config(text=str(random.randrange(1,10)))
                #print('gwrgwr'+str((self.checker(x,y))))
                #while(self.checkself(x,y)==0):
                    #print('wffwffrwrfw')
                    #self.block[x][y].config(text=str(random.randrange(1,10)))
                
            #command=lambda a=x ,b=y: self.logicfunction(a,b,1),
            
            #if(x<8):
                #x=x+1
            #else:
                #x=0
                #y=y+1

            #print('x=',x,'y=',y,'z=',z,'\n')
               
        self.frame.pack()
        Label(text="THE UNDERLINED NUMBER CANNOT BE CHANGED.CLICK THE NUMDER BELOW AND THEN CLICK THE BUTTON IN THE SUDOCU THAT YOU WANT TO PLACE").pack(fill=tkinter.X)
        Label(text="DIFFICULTY LEVEL "+str(self.level)).pack(fill=tkinter.X)
        Label(text="STATUS").pack(fill=tkinter.X)
        self.b=[0,1,2,3,4,5,6,7,8,9]
        #the function is not create
        colorb=0
        Label(text ='NUMBER ROW').pack(side=tkinter.LEFT)
        while(colorb<9):
            self.b[colorb]=Button(text='  '+str(colorb+1)+'  ',font=15,command=lambda c1=colorb+1 : self.colorChange(c1))
            self.b[colorb].pack(side=tkinter.LEFT)
            colorb+=1
        #self.b[1]=Button(text='  2  ',font=15).pack(side=tkinter.LEFT)
        #self.b[2]=Button(text='  3  ',font=15).pack(side=tkinter.LEFT)
        #self.b[3]=Button(text='  4  ',font=15).pack(side=tkinter.LEFT)
        #self.b[4]=Button(text='  5  ',font=15).pack(side=tkinter.LEFT)
        #self.b[5]=Button(text='  6  ',font=15).pack(side=tkinter.LEFT)
        #self.b[6]=Button(text='  7  ',font=15).pack(side=tkinter.LEFT)
        #self.b[7]=Button(text='  8  ',font=15).pack(side=tkinter.LEFT)
        #self.b[8]=Button(text='  9  ',font=15).pack(side=tkinter.LEFT)
        self.status=Label()
        self.status.pack()

        
        self.playwindow.mainloop()
    def solvef(self):
        
        i = 0
        j = 0
    
    
        #print('1')
        # if board is full, there is no need to solve it any further
        if self.isfull() and self.firsts==0:
            print("Board Solved Successfully!")
            self.firsts =1
            #for e in self.block:
            #    print(str(e))
            return
        else:
            #print('2')    
            # find the first vacant spot
            for y in range (0, 9):
                for x in range (0, 9):
                    if self.block[y][x] == 0:
                        i = x
                        j = y
                        break
                else:
                    continue
                break
        if(self.isfull()==0):
            array=self.prossiblefun(x,y)
            index=0
            while(index<len(array) and self.firsts==0):
                self.block[j][i]=array[index]
                index=index+1
                            
                '''for q in self.block:    
                    print(str(q))
                print('\n;;'''
                                
                self.solvef()
                #print(str(self.block))
            if(self.isfull()==0) and self.firsts==0 :    
                self.block[y][x]=0
                            
    def isfull(self):
        '''
        this is the same code which was used in __init__ to create the block   
        '''
        x=0
        y=0
        while(y<9):
            x=0
            while(x<=8):
                #print(self.block[x][y].cget('text')+str(self.block[x][y].cget('text').isdigit()))
                if self.block[y][x] == 0 :
                
                    #print(self.block[x][y].cget('text')+'hdhdth')
                    return 0
                    #print(' '+self.block[x][y][z].cget('text'),end=' ') 
                x=x+1
                #print(' '+self.block[x][y][z].cget('text'))
            y=y+1
        return 1

            
    def zfunction(self,x,y):
        if(y<3):
                z=int(x/3)
        if(3<=y<6):
                z=int(x/3)+3
        if(y>5):
            z=int(x/3)+6    
        return z
            
        
        
        
    def colorChange(self,i):
        
        color=['white','red','green','yellow','blue','black']
        # 6 colors
        #self.selectednum
        if not(self.selectednum ==i):
        
            self.b[i-1].config(bg=color[2],fg=color[3])
            
            if not self.selectednum == -1:
                self.b[self.selectednum-1].config(bg=color[0],fg=color[5])
            self.selectednum=i
        #print(str(self.b[i]))

        #self.status
        #self.win =0    
    
    def fill(self):
        '''
        this is the same code which was used in __init__ to create the block   

        '''
        x=0
        y=0
        
        
        while(y<9):
            x=0
            while(x<=8):
                #print(self.block[x][y].cget('text')+str(self.block[x][y].cget('text').isdigit()))

                
                if (not(self.block[x][y].cget('text').isdigit())) or self.block[x][y].cget('text') == '0' :
                
                    #print(self.block[x][y].cget('text')+'hdhdth')
                    return 0
                    #print(' '+self.block[x][y][z].cget('text'),end=' ') 
                x=x+1
                #print(' '+self.block[x][y][z].cget('text'))
            y=y+1
                
            
        return 1
        '''a=0

        b=0
        c=0
        #self.block[x][y][z]
        # a=x b =y z=c 
        while(a<9):
            while(b<9):
                while (c<9):
                    try:
                        if not(1<=int(self.block[a][b][c].cget('text'))<=9):
                            print(self.block[a][b][c].cget('text'))
                            return 0
                    except:
                        print(self.block[a][b][c].cget('text'))
                        return 0
                    c=c+1
                b=b+1    
            a=a+1            
        return 1
        '''
    def checker(self,x,y):
        a=0
        b=y
        while(a<=8):
            #print(self.block[a][b])
            if(self.block[a][b].cget('text')==str(self.selectednum)):
                #print('same number in a,b,c'+str(x)+str(y)+str(self.zfunction(x,y)))
                self.status.config(text='same number in a,b,c'+str(x)+str(y)+str(self.zfunction(x,y)),bg='black',fg='red')
                return 0
            a=a+1
            
    
        b=0
        while(b<=8):
            a=x
            if(b==y):
                b=b+1
            if(b<9):    
                if(self.block[a][b].cget('text')==str(self.selectednum)):
                    #print('same number in a,b,c'+str(x)+str(y)+str(self.zfunction(x,y)))
                    return 0
            b=b+1
        zi=[[0,0],[3,0],[6,0],[0,3],[3,3],[6,3],[0,6],[3,6],[6,6]]    
        b=zi[self.zfunction(x,y)][1]
            
        bf=b+2
        af=zi[self.zfunction(x,y)][0]+2
        while(b<=bf):
            a=zi[self.zfunction(x,y)][0]
            while(a<=af):
                #print(str(a)+str(b)+str(self.zfunction(x,y)),end=' ')    
                if(self.block[a][b].cget('text')==str(self.selectednum)):
                    print('ghethertrthsame number in a,b,c'+str(x)+str(y)+str(self.zfunction(x,y)))
                    return 0
                a=a+1    
            b=b+1
        return 1    


    def checkarrayself(self,x,y,num):
        a=0
        b=y
        while(a<=8):
            if(a!=x):
                if(self.block[b][a]==num or num>9):
                    #print('same number in a,b,c'+str(x)+str(y)+str(self.zfunction(x,y)))
                
                    return 0
            a=a+1
            
    
        b=0
        while(b<=8):
            a=x
            
            if b!=y:    
                if(self.block[b][a]==num):
                    #print('same number in a,b,c'+str(x)+str(y)+str(self.zfunction(x,y)))
                    return 0
            b=b+1
        zi=[[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]    
        b=zi[self.zfunction(x,y)][0]
            
        bf=b+2
        af=zi[self.zfunction(x,y)][1]+2
        while(b<=bf):
            a=zi[self.zfunction(x,y)][1]
            while(a<=af):
                #print(str(a)+str(b)+str(self.zfunction(x,y)),end=' ')
                if(a!=x and b!=y):
                    if(self.block[b][a]==num):
                        #print('ghethertrthsame number in a,b,c'+str(x)+str(y)+str(self.zfunction(x,y)))
                        return 0
                a=a+1    
            b=b+1
        return 1    
    def prossiblefun(self,x,y):
        array=[]
        num=1
        while(num<=9):
            if(self.checkarrayself(x,y,num)==1):
                array.append(num)
            
                
            num+=1    
        #print(str(self.block[0]))
        #print(str(array)+'\n')
        mix=random.sample(array,len(array))
        #so that array sequiece is changed
        return mix

                
    def checkself(self,x,y):
        a=0
        b=y
        while(a<=8):
            if(a!=x):
                if(self.block[a][b].cget('text')==self.block[x][y].cget('text')):
                    #print('same number in a,b,c'+str(x)+str(y)+str(self.zfunction(x,y)))
                
                    return 0
            a=a+1
            
    
        b=0
        while(b<=8):
            a=x
            if(b==y):
                b=b+1
            if(b<9) and b!=y:    
                if(self.block[a][b].cget('text')==self.block[x][y].cget('text')):
                    #print('same number in a,b,c'+str(x)+str(y)+str(self.zfunction(x,y)))
                    return 0
            b=b+1
        zi=[[0,0],[3,0],[6,0],[0,3],[3,3],[6,3],[0,6],[3,6],[6,6]]    
        b=zi[self.zfunction(x,y)][1]
            
        bf=b+2
        af=zi[self.zfunction(x,y)][0]+2
        while(b<=bf):
            a=zi[self.zfunction(x,y)][0]
            while(a<=af):
                #print(str(a)+str(b)+str(self.zfunction(x,y)),end=' ')
                if(a!=x and b!=y):
                    if(self.block[a][b].cget('text')==self.block[x][y].cget('text')):
                        #print('ghethertrthsame number in a,b,c'+str(x)+str(y)+str(self.zfunction(x,y)))
                        return 0
                a=a+1    
            b=b+1
        return 1    
            
            
    def logicfunction(self,x,y,c):
        if self.checker(x,y)==1 and self.selectednum != -1 and c==1:
            self.block[x][y].config(text=str(self.selectednum))
            #print('etghetgrt')
        
        if(self.fill()==1):
            #print('hgehgvklgvklhnvbklds')
            w=Tk()
            Label(w,text = 'CONGRATULATION..YOU HAVE WON THE GAME',font=30).pack()
            
            Label(w,text = 'YOU HAVE WON THE GAME',font=25).pack()
            w.mainloop()
        if c==0:
            self.status.config(text='YOU CANNOT CHANGE THAT NUMBER..',bg='black',fg='red')
        if self.selectednum == -1:
            self.status.config(text='YOU MUST SELECT A NUMBER FROM THE NUMBER ROW FIRST..',bg='black',fg='red')
        if not(c==0) and  (self.selectednum !=-1)and (self.fill()) :
            
            pass





class home():
    def __init__(self):
        self.window=tkinter.Tk()
        tkinter.Tk.title(self.window,"SUDOKU")
        frame1=tkinter.Frame(self.window)
        frame2=tkinter.Frame(self.window)
        name1=tkinter.Label(frame1,text='SUDOKU',bg='red',font='100',fg='blue')
        name2=tkinter.Label(frame1,text='GAME',fg='red',font='100',bg='blue')
        newgame=tkinter.Button(frame2,text='NEW GAME',bg='yellow',font='10',fg='blue',command=self.newgamef)
        #score=tkinter.Button(frame2,text='SCORE ',bg='yellow',font='10',fg='blue',command=scoref)
        levelb=tkinter.Button(frame2,text='LEVEL',bg='yellow',font='10',fg='blue',command=self.levelf)
        about=tkinter.Button(frame2,text='ABOUT ',bg='yellow',font='10',fg='blue',command=aboutf)
        helpb=tkinter.Button(frame2,text='HELP  ',bg='yellow',font='10',fg='blue',command=helpf)
        quitf=tkinter.Button(frame2,text='QUIT ',bg='yellow',font='10',fg='blue',command=self.wquit)
        name1.pack(side='left',fill=tkinter.X)
        name2.pack(side='left',fill=tkinter.X)
        newgame.pack(anchor=tkinter.E)
        levelb.pack(anchor=tkinter.E)
        #score.pack(anchor=tkinter.E)
        about.pack(anchor=tkinter.E)
        helpb.pack(anchor=tkinter.E)
        quitf.pack(anchor=tkinter.E)
        frame1.pack(side='top')
        frame2.pack(side='right')
        #about.pack(anchor=w)
        #helpf.pack(anchor=w)
        #quite.pack(anchor=w)
        self.window.mainloop()


    def lb(self,a):
        global levelnum
        color=['green','yellow','red']
        la=[7,5,3]#level array
        s=['EASY','MEDIUM','HARD']
        levelnum=la[a]
        self.status.config(text=str(a)+'THE LEVEL IS SET TO '+s[a])
        self.bl[a].config(bg=color[a])
        for i in range(0,3):
            if(i!=a):
                self.bl[i].config(bg='white')






    def levelf(self):
        level=Tk()
        Label(level,text='SUDOKU',font=40).pack(fill=tkinter.X)
        self.bl=[0,0,0]
        self.bl[0]=Button(level,text='EASY',font=40,bg='green',command=lambda a=0:self.lb(a))
        self.bl[0].pack(fill=tkinter.X)
        self.bl[1]=Button(level,text='MEDIUM',font=40,command=lambda a=1:self.lb(a))
        self.bl[1].pack(fill=tkinter.X)
        self.bl[2]=Button(level,text='HARD',font=40,command=lambda a=2:self.lb(a))
        self.bl[2].pack(fill=tkinter.X)
        Label(level,text='STATUS',font=40).pack(fill=tkinter.X)
        self.status=Label(level,text ='THE LEVEL IS SET TO EASY',font=20)
        self.status.pack(fill=tkinter.X)
        #e=Button(text='EXIT',font=40)
        #e.pack(fill=tkinter.X)
        level.mainloop()

    
    def wquit(self):
        #the function to quit the programm

        v=tkinter.messagebox.askokcancel(title='QUIT',message='Are you sure you want to quit the game')
        if v==True:
            self.window.destroy()
            global playing
            playing=False
            sys.exit()
            os.system('exit')

    def newgamef(self):
        #the function to quit the programm
        self.window.destroy()
        newgame()
        
def main():
    home()



main()



