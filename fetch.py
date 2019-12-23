from tkinter import *
from random import randint
'''
Bbox key
left, top, right, bottom
'''

#Setup
win = Tk()

xSize = win.winfo_screenwidth()
ySize = win.winfo_screenheight()

win.geometry('100x100')
win.title("Fetch!")
win.attributes("-fullscreen", True) #Make fullscreen

win.lift()
win.attributes("-topmost", True) #Make this the topmost window
win.after_idle(win.attributes, '-topmost', False)

canvas = Canvas(win, background='deep sky blue')
canvas.pack(fill=BOTH, expand=YES)


class LogIn: #Class for login screen
    def __init__(self):
        #Lots of tkinter stuff...
        self.fetchL = Label(text='Fetch', bg='deep sky blue',\
                           font=('helvetica', 40))
        self.fetchL.place(x=xSize//2-50, y=ySize//2-300)
        self.nameL = Label(text='Enter your Name', bg='deep sky blue',\
                           font=('helvetica', 20))
        self.nameL.place(x=xSize//2-80, y=ySize//2-200)
        self.nameE = Entry(justify=CENTER)
        self.nameE.place(x=xSize//2-86, y=ySize//2-150)

        self.passL = Label(text='Enter your Password', bg='deep sky blue',\
                           font=('helvetica', 20))
        self.passL.place(x=xSize//2-95, y=ySize//2-100)
        self.passE = Entry(justify=CENTER, show="●")
        self.passE.place(x=xSize//2-86, y=ySize//2-50)

        self.logB = Button(text='Login',bg='deep sky blue',command=self.log)
        self.logB.place(x=xSize//2-90, y=ySize//2)

        self.signB=Button(text='Sign Up',bg='deep sky blue',command=self.signUp)
        self.signB.place(x=xSize//2+10, y=ySize//2)

        self.errL = Label(text='', fg='red', bg='deep sky blue')

    def log(self): #Method to check if username and password for login are good.
        try: #Open file
            file = open('hs.txt', 'r')
        except Exception:
            file = open('hs.txt', 'w')
            file.close()
            file = open('hs.txt', 'r')
        fr = file.readlines()
        file.close()
        names = []
        passwords = []

        for i in range(0, len(fr)): #Store usernames and passwords in lists
            l = fr[i].split('HsU_hYj2HJQ?*&-[OjkL$=>B9*iLr#;j*f$')
            names.append(l[0])
            passwords.append(l[1])

        if self.nameE.get() in names:#Make sure username and password is correct
            i = names.index(self.nameE.get())
            if self.passE.get() == passwords[i]:
                self.start()
            else:
                self.errL.config(text='Error! Incorect Password')
                self.errL.place(x=xSize//2-80, y=ySize//2+50)
        else:
            self.errL.config(text='Error! "'+self.nameE.get()+'" does not exist')
            self.errL.place(x=xSize//2-100, y=ySize//2+50)

        if self.passE.get().lower() in c.colors:
            b.color = self.passE.get().lower()

    def signUp(self): #Method to create new account
        try: #Open file
            file = open('hs.txt', 'r')
        except Exception:
            file = open('hs.txt', 'w')
            file.close()
            file = open('hs.txt', 'r')
        fr = file.readlines()
        file.close()
        names = []
        passwords = []

        for i in range(0, len(fr)): #Store file content in lists
            l = fr[i].split('HsU_hYj2HJQ?*&-[OjkL$=>B9*iLr#;j*f$')
            names.append(l[0])
            passwords.append(l[1])

        if self.nameE.get() in names: #Makes sure username isnt already used
            self.errL.config(text='Error! Name already taken')
            self.errL.place(x=xSize//2-80, y=ySize//2+50)

        else: #Create account in file
            file = open('hs.txt', 'a')
            file.write(self.nameE.get() + 'HsU_hYj2HJQ?*&-[OjkL$=>B9*iLr#;j*f$' \
                       + self.passE.get() + 'HsU_hYj2HJQ?*&-[OjkL$=>B9*iLr#;j*f$0HsU_hYj2HJQ?*&-[OjkL$=>B9*iLr#;j*f$0' + '\n')
            self.start()

        if self.passE.get().lower() in c.colors:
            b.color = self.passE.get().lower()
            
    def start(self): #Method to open Start Screen
        s.player = self.nameE.get()
        s.liL.config(text='Logged in as ' + s.player)
        s.show()
        self.hide()

    def hide(self): #Method to hide login screen elements
        self.fetchL.place(x=0, y=-200)
        
        self.nameL.place(x=0, y=-200)
        self.nameE.place(x=0, y=-200)
        self.nameE.config(state=DISABLED)
        
        self.passL.place(x=0, y=-200)
        self.passE.place(x=0, y=-200)
        self.passE.config(state=DISABLED)

        self.logB.place(x=0, y=-200)
        self.signB.place(x=0, y=-200)

        self.errL.config(text='')

    def show(self): #Method to show login screen elements
        self.nameE.config(state=NORMAL)
        self.passE.config(state=NORMAL)
        self.nameE.delete(0, 'end')
        self.passE.delete(0, 'end')
        self.fetchL.place(x=xSize//2-50, y=ySize//2-300)
        self.nameL.place(x=xSize//2-80, y=ySize//2-200)
        self.nameE.place(x=xSize//2-86, y=ySize//2-150)
        
        self.passL.place(x=xSize//2-95, y=ySize//2-100)
        self.passE.place(x=xSize//2-86, y=ySize//2-50)

        self.logB.place(x=xSize//2-90, y=ySize//2)
        self.signB.place(x=xSize//2+10, y=ySize//2)

class StartScreen: #Class to create a start screen
    def __init__(self):
        #tkinter stuff...
        self.fetchL = Label(text='Fetch', bg='deep sky blue',\
                           font=('helvetica', 40))
        self.fetchL.place(x=xSize//2-50, y=ySize//2-300)

        self.startB = Button(text='Start', command = self.start)
        self.startB.place(x=xSize//2-70, y=ySize//2-200)
        self.loB = Button(text='Log Out', command = self.logOut)
        self.loB.place(x=xSize//2, y=ySize//2-200)

        self.instLL = Label(text='How to Play:', bg='deep sky blue',\
                           font=('helvetica', 30))
        self.instLL.place(x=xSize//2-450, y=ySize//2-200)
        self.hsLL = Label(text='High Scores:', bg='deep sky blue',\
                           font=('helvetica', 30))
        self.hsLL.place(x=xSize//2+280, y=ySize//2-200)

        self.instL=Label(text='The goal of Fetch is to catch as many balls\n'+\
                'as possible. Touch a ball to catch it. To return\n' + \
                'a ball, bring it to the left or rigth side of\n' + \
                'the screen. Every ball caught will add 1 point to\n' + \
                'your score and 3 seconds of time. Use A to move\n' + \
                'left and D to move right. Press or hold the\n' + \
                'spacebar to jump. Good Luck!', \
                bg='deep sky blue',font=('helvetica', 15))
        self.instL.place(x=xSize//2-520, y=ySize//2-150)

        self.hsL = Label(text=self.getTop3(),
                bg='deep sky blue', font=('helvetica', 15))

        self.hsL.place(x=xSize//2+350, y=ySize//2-150)

        self.liL = Label(text='Logged in as ______', bg='deep sky blue')
        self.liL.place(x=xSize//2-60, y=ySize//2-150)
        
        self.player = ''
        self.hide()

    def getTop3(self): #Method to display top 3 scores of all time
        try: #Open file
            file = open('hs.txt', 'r')
        except Exception:
            file = open('hs.txt', 'w')
            file.close()
            file = open('hs.txt', 'r')
        fr = file.readlines()
        file.close()
        names = []
        passwords = []
        scores = []

        for i in range(0, len(fr)): #Put content in list
            l = fr[i].split('HsU_hYj2HJQ?*&-[OjkL$=>B9*iLr#;j*f$')
            names.append(l[0])
            scores.append(int(l[2]))
        
        if len(names) < 3:
            m = len(names)
        else:
            m = 3
        t3 = ''
        for i in range(0, m): #Organize top three
            t3+=names[scores.index(max(scores))]+'     '+str(max(scores))+'\n'
            names.remove(names[scores.index(max(scores))])
            scores.remove(max(scores))

        return t3
    
    def start(self): #Method to begin game
        self.hide()

        active = []
        for _ in range(0, randint(3, 5)): #Create random platforms
            active.append(int(str(randint(0, 3))+str(randint(1, 2))))
            
        for row in range(0, 4):
            for column in range(1, 3):
                if int(str(row)+str(column)) in active:
                    p.append(Platform(randint(row*(xSize//4), row*(xSize//4)+\
                            xSize//8),randint(column*(ySize//4),column*\
                            (ySize//4)+ySize//8)))
        b.go = True
        c.timeL.config(text='20')
        c.scoreL.config(text='0')
        b.throw()
        canvas.after(1000, c.countLoop)
        
    def hide(self): #Method to hide start screen elements
        self.fetchL.place(x=0, y=-200)
        self.startB.place(x=0, y=-200)
        self.loB.place(x=0, y=-200)
        self.instLL.place(x=0, y=-200)
        self.hsLL.place(x=0, y=-200)
        self.instL.place(x=0, y=-200)
        self.hsL.place(x=0, y=-200)
        self.liL.place(x=xSize//2-60, y=-200)
        
    def show(self): #method to show start screen elements
        self.fetchL.place(x=xSize//2-50, y=ySize//2-300)
        self.startB.place(x=xSize//2-70, y=ySize//2-200)
        self.loB.place(x=xSize//2, y=ySize//2-200)
        self.instLL.place(x=xSize//2-450, y=ySize//2-200)
        self.hsLL.place(x=xSize//2+280, y=ySize//2-200)
        self.instL.place(x=xSize//2-520, y=ySize//2-150)
        self.hsL.place(x=xSize//2+320, y=ySize//2-150)
        self.liL.place(x=xSize//2-60, y=ySize//2-150)

    def logOut(self): #Method for logout button
        self.hide()
        l.show()

class Dog: #Class to represent the dog
    def __init__(self):
        #Prepare images
        self.dogLImg0 = PhotoImage(file = 'dogL.gif', format = 'gif -index 0')
        self.dogLImg1 = PhotoImage(file = 'dogL.gif', format = 'gif -index 1')
        self.dogRImg0 = PhotoImage(file = 'dogR.gif', format = 'gif -index 0')
        self.dogRImg1 = PhotoImage(file = 'dogR.gif', format = 'gif -index 1')
        self.dogLImg2 = PhotoImage(file = 'dogL.gif', format = 'gif -index 2')
        self.dogRImg2 = PhotoImage(file = 'dogR.gif', format = 'gif -index 2')
        
        self.img = 'dogLImg0'
        self.dogHasBall = False
        
        self.dog = canvas.create_image(xSize//2, ySize-150, image=self.dogLImg0)
        self.change = 0
        self.up = 0

    def moveChange(self, e): #Method to track key presses
        if e.keysym == 'a':
            self.change = -6

        if e.keysym == 'd':
            self.change = 6

        if e.keysym == 'space':
            canvas.move(self.dog, 0, -1)
            self.up = -10

    def moveOff(self, e): #Method to track key releases
        self.change = 0

    def moveLoop(self): #Method to move dog
        if b.go:#Make sure start screen is inactive
            
            self.dogB = canvas.bbox(self.dog)
            bBall = canvas.coords(b.ball)
            
            if self.dogB[3] < ySize-100: #See if dog is on ground
                self.up += 0.5

            else:
                self.up = 0
                canvas.move(self.dog, 0, (ySize-100)-self.dogB[3])

            #Check if dog has caught ball.
            if (bBall[0] < self.dogB[2] and bBall[2] > self.dogB[0] and \
                   bBall[1] < self.dogB[3] and bBall[3] > self.dogB[1]) or \
                   self.dogHasBall:
                if 'R' in self.img:
                    b.goto(self.dogB[2]-2, self.dogB[1]+15)
                else:
                    b.goto(self.dogB[0]+2, self.dogB[1]+15)
                self.dogHasBall = True
                    
            else:
                b.throwLoop() #Continue ball motion if dog doent have ball.
            
            if self.dogB[2] > xSize: #Keep dog onscreen
                self.change = 0
                canvas.move(self.dog, -1, 0)

            elif self.dogB[0] < 0:
                self.change = 0
                canvas.move(self.dog, 1, 0)

            #Throw ball if dog takes it to side.
            if (self.dogB[2] > xSize or self.dogB[0] < 0) and self.dogHasBall:
                c.scorePlus()
                b.throw()

            for platform in p: #Check if dog is on a platform
                if platform.platTop(self.dogB):
                    self.up = 0
                    canvas.move(self.dog, 0, platform.getY('t')-self.dogB[3])

                elif platform.platBottom(self.dogB):
                    self.up = 0
                    canvas.move(self.dog, 0, platform.getY('b')-self.dogB[1])
                    
            canvas.move(self.dog, self.change, self.up)
        canvas.after(5, self.moveLoop) #Continue loop

    def animate(self): #Method to animate dog motion.
        if b.go:
            if self.up != 0: #Check if dog is jumping
                if self.change<0:
                    canvas.itemconfig(self.dog, image=self.dogLImg2)
                    self.img = 'dogLImg2'
                else:
                    canvas.itemconfig(self.dog, image=self.dogRImg2)
                    self.img = 'dogRImg2'
                    
            elif self.change != 0: #Otherwise, do normal animation
                if self.img == 'dogLImg0':
                    canvas.itemconfig(self.dog, image=self.dogLImg1)
                    self.img = 'dogLImg1'
                elif self.change < 0:
                    canvas.itemconfig(self.dog, image=self.dogLImg0)
                    self.img = 'dogLImg0'
                elif self.img == 'dogRImg0':
                    canvas.itemconfig(self.dog, image=self.dogRImg1)
                    self.img = 'dogRImg1'
                elif self.change > 0:
                    canvas.itemconfig(self.dog, image=self.dogRImg0)
                    self.img = 'dogRImg0'

            else: #Stop animation if dog is not moving
                if self.img == 'dogLImg2':
                    canvas.itemconfig(self.dog, image=self.dogLImg0)
                    self.img = 'dogLImg0'
                elif self.img == 'dogRImg2':
                    canvas.itemconfig(self.dog, image=self.dogRImg0)
                    self.img = 'dogRImg0'
        
        canvas.after(100, self.animate) #Continue animation loop

class Platform: #Class to represent a platform.
    def __init__(self, x, y):
        self.plat = canvas.create_rectangle(x, y, x+randint(150, 350), y+40, \
                                            width=0, fill='dark green')

        self.platB = canvas.coords(self.plat)

    def platTop(self, other):#Method to check if something is on top of platform
        if other[3] > self.platB[1] and other[1] < self.platB[1] and \
                other[0] < self.platB[2] and other[2] > self.platB[0]:
            return True

        else:
            return False

    def platBottom(self, other):#Method to check if on bottom of platform
        if other[1] < self.platB[3] and other[3] > self.platB[3] and \
                other[0] < self.platB[2] and other[2] > self.platB[0]:
            return True

        else:
            return False

    def getY(self, side='t'): #Method to get y coordinate of platform
        if side=='t':
            return self.platB[1]+1
        elif side=='b':
            return self.platB[3]+1

    def delete(self):
        canvas.move(self.plat, 0, -1500)
        del self.plat
        del p[p.index(self)]
        
class Ball: #Class to represent a ball
    def __init__(self):
        self.ball = canvas.create_oval(-12, -12, 0, 0, \
                                         fill='red', width=0)
        self.xM = 0
        self.yM = 0
        self.go = True

        self.color = 'red'
        
    def throw(self): #Method to throw ball in the sky
        canvas.itemconfig(self.ball, fill=self.color)
        d.dogHasBall = False
        self.goto(randint(0, xSize), 0)
        
        self.xM = randint(-20, 20)
        self.yM = randint(-3, 4)

    def throwLoop(self): #Method to continue ball motion
        if self.go:
            canvas.move(self.ball, self.xM, self.yM)
            bBall = canvas.coords(self.ball)

            self.yM += 0.4
            
            if self.xM > 0:
                self.xM -= 0.02
            else:
                self.xM += 0.02

            if bBall[3] > ySize-100:
                self.yM = self.yM * -0.85
                self.goto((bBall[0]+bBall[2])//2, ySize-100)

            if bBall[0] < 0 or bBall[2] > xSize:
                self.xM = self.xM * -1

            for platform in p:
                if platform.platTop(bBall):
                    self.yM *= -0.85
                    self.goto((bBall[0]+bBall[2])//2,\
                              platform.getY('t')-6)

                if platform.platBottom(bBall):
                    self.yM *= -1
                    self.goto((bBall[0]+bBall[2])//2,\
                              platform.getY('b')+6)

    def goto(self, x, y): #Method to set ball position
        canvas.move(self.ball,\
                x-(canvas.coords(self.ball)[0]+canvas.coords(self.ball)[2])//2,\
                y-(canvas.coords(self.ball)[1]+canvas.coords(self.ball)[3])//2)

class Control: #Class to controll all proccess, scores, and timers
    def __init__(self):
        self.colors = ['snow', 'ghost white', 'white smoke', 'gainsboro', \
                       'floral white', 'old lace','linen', 'antique white', \
                       'papaya whip', 'blanched almond', 'bisque', 'peach puff'\
                       ,'navajo white', 'lemon chiffon', 'mint cream', 'azure', \
                       'alice blue', 'lavender','lavender blush', 'misty rose',\
                       'dark slate gray', 'dim gray', 'slate gray',\
                       'light slate gray', 'gray', 'light grey', \
                       'midnight blue', 'navy', 'cornflower blue', \
                       'dark slate blue','slate blue', 'medium slate blue', \
                       'light slate blue', 'medium blue', 'royal blue',  \
                       'blue','dodger blue', 'deep sky blue', 'sky blue', \
                       'light sky blue', 'steel blue', 'light steel blue',\
                       'light blue', 'powder blue', 'pale turquoise', \
                       'dark turquoise', 'medium turquoise', 'turquoise',\
                       'cyan', 'light cyan', 'cadet blue', 'medium aquamarine'\
                       , 'aquamarine', 'dark green', 'dark olive green',\
                       'dark sea green', 'sea green', 'medium sea green', \
                       'light sea green', 'pale green', 'spring green',\
                       'lawn green', 'medium spring green', 'green yellow', \
                       'lime green', 'yellow green','forest green', \
                       'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', \
                       'light goldenrod yellow','light yellow', 'yellow', \
                       'gold', 'light goldenrod', 'goldenrod', \
                       'dark goldenrod', 'rosy brown','indian red', \
                       'saddle brown', 'sandy brown','dark salmon', \
                       'salmon', 'light salmon', 'orange', 'dark orange',\
                       'coral', 'light coral', 'tomato', 'orange red', \
                       'red', 'hot pink', 'deep pink', 'pink', 'light pink',\
                       'pale violet red', 'maroon', 'medium violet red', \
                       'violet red','medium orchid', 'dark orchid', \
                       'dark violet', 'blue violet', 'purple', 'medium purple',\
                       'thistle']
        tL = Label(text='Time:', font=('Verdana', 60), bg='deep sky blue')
        tL.place(x=20, y=10)
        self.timeL = Label(text='20', font=('Verdana', 60), bg='deep sky blue')
        self.timeL.place(x=210, y=10)
        
        sL = Label(text='Score:', font=('Verdana', 60), bg='deep sky blue')
        sL.place(x=xSize-320, y=10)
        self.scoreL = Label(text='0', font=('Verdana', 60), bg='deep sky blue')
        self.scoreL.place(x=xSize-100, y=10)

    def countLoop(self): #Method to run timer
        self.timeL.config(text=str(int(self.timeL.cget('text'))-1))
        if self.timeL.cget('text') == '0':
            b.go = False
            s.show()
            self.updateHS()
            s.hsL.config(text=s.getTop3())
            for i in range(0, len(p)):
                p[0].delete()
        else:
            canvas.after(1000, self.countLoop)

    def scorePlus(self): #Method to add to score when dog earns point
        self.scoreL.config(text=str(int(self.scoreL.cget('text'))+1))
        self.timeL.config(text=str(int(self.timeL.cget('text'))+3))

    def updateHS(self): #Method to update high scores every round
        file = open('hs.txt', 'r')#Open file
        fr = file.readlines()
        file.close()
        names = []
        passwords = []
        hscores = []
        scores = []

        for i in range(0, len(fr)): #Organize into list
            l = fr[i].split('HsU_hYj2HJQ?*&-[OjkL$=>B9*iLr#;j*f$')
            names.append(l[0])
            passwords.append(l[1])
            hscores.append(l[2])
            scores.append(l[3])

        if int(self.scoreL.cget('text')) > int(hscores[names.index(s.player)]):
            hscores[names.index(s.player)] = self.scoreL.cget('text')
        scores[names.index(s.player)] = self.scoreL.cget('text')+'\n'
            
        fl = []
        for i in range(0, len(fr)): #Edit file
            fl.append(names[i] + 'HsU_hYj2HJQ?*&-[OjkL$=>B9*iLr#;j*f$' + passwords[i] \
                      + 'HsU_hYj2HJQ?*&-[OjkL$=>B9*iLr#;j*f$' + hscores[i] + 'HsU_hYj2HJQ?*&-[OjkL$=>B9*iLr#;j*f$' + scores[i])

        file = open('hs.txt', 'w') #Replace with new text
        for i in fl:
            file.write(i)
        file.close()

#Create instances
b = Ball()
d = Dog()
c = Control()
l = LogIn()
s = StartScreen()
b.go = False
d.moveLoop()
d.animate()
p = []

canvas.bind_all("<KeyPress>", d.moveChange) #Bind keys
# canvas.bind_all("<KeyRelease-a>", d.moveOff)
# canvas.bind_all("<KeyRelease-d>", d.moveOff)

canvas.create_rectangle(0, ySize-100, xSize, ySize, \
                        fill='dark green', outline='dark green')

win.mainloop()
