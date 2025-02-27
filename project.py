import  tkinter as tk
import turtle
window=tk.Tk()
window.title("জ্যামিতি শেখার আয়োজনে স্বাগতম")
canvas=tk.Canvas(master=window,height=1000,width=1200)
canvas.grid(row=2,column=2,rowspan=10,columnspan=10)

draw=turtle.RawTurtle(canvas)

def point():
    draw.reset()
    draw.speed(2)
    draw.pensize(5)
    draw.penup()
    draw.setpos(-20,150)
    draw.color("red")
    draw.pendown()
    draw.forward(1)
    draw.penup()
    draw.hideturtle() 
    draw.setpos(-180,30)
    def file1():
        f1=open("D:\project work\\point.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,15")
def point_b2():
    button=tk.Button(master=window,text="বিন্দু",font=15,bg="red",fg="white",command=point)
    button.grid(row=1,column=1,sticky="nsew")
    button=tk.Button(master=window)
    button.grid(row=1,column=2,sticky="nsew")
    button=tk.Button(master=window)
    button.grid(row=1,column=3,sticky="nsew")
    button=tk.Button(master=window)
    button.grid(row=1,column=4,sticky="nsew")
    button=tk.Button(master=window)
    button.grid(row=1,column=5,sticky="nsew")

def point_b ():
    button_line=tk.Button(master=window,text="বিন্দু",font=15,bg="red",fg="white",command=point_b2)
    button_line.grid(row=1,column=0,sticky="nsew")
point_b()



def line():                      # for drawing line
    draw.reset()
    draw.speed(2)
    draw.pensize(3)
    draw.color("blue")
    draw.penup()
    draw.setpos(-150,150)
    draw.pendown()              
    draw.forward(150)
    draw.penup()
    draw.hideturtle() 
    draw.setpos(-180,30)
    def file1():
        f1=open("D:\project work\\line.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,10")
def d_line():
    draw.reset()
    draw.speed(2)
    draw.color("red")
    draw.pensize(3)
    draw.penup()
    draw.setpos(-50,100)
    draw.right(90)
    draw.pendown()
    draw.circle(-100,-180)
    draw.penup()
    draw.hideturtle() 
    draw.setpos(-250,0)
    def file1():
        f1=open("D:\project work\\curve_line.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,10")

def line_b():
    button=tk.Button(master=window,text=" সরলরেখা",font=15,bg="navy blue",fg="white",command=line)
    button.grid(row=1,column=1,sticky="nsew")
    button=tk.Button(master=window,text="বক্ররেখা",font=15,bg="navy blue",fg="white",command=d_line)
    button.grid(row=1,column=2,sticky="nsew")
    button=tk.Button(master=window)
    button.grid(row=1,column=3,sticky="nsew")
    button=tk.Button(master=window)
    button.grid(row=1,column=4,sticky="nsew")
    button=tk.Button(master=window)
    button.grid(row=1,column=5,sticky="nsew")

def line_shape():
    button_line=tk.Button(master=window,text="রেখা",font=15,bg="navy blue",fg="white",command=line_b)
    button_line.grid(row=2,column=0,sticky="nsew")


line_shape()               #line funtion calling


def angle():               # for drawing angle                   
    draw.reset()
    draw.speed(2)
    draw.pensize(3)
    draw.penup()
    draw.setpos(-160,70)     #this is for turtle position     
    draw.pendown()
    draw.color("blue")
    draw.pensize(3)         
    draw.forward(150)
    draw.left(140)
    draw.forward(150)
    draw.penup()
    draw.hideturtle() 
    draw.setpos(-220,-10)
    def file1():
        f1=open("D:\project work\\angle.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,10")

def right_angle():
    draw.reset()
    draw.speed(2)
    draw.penup()
    draw.setpos(-160,70)     #this is for turtle position     
    draw.pendown()
    draw.color("blue")
    draw.pensize(3)                    
    draw.pendown()
    draw.forward(200)
    draw.left(180)
    draw.forward(100)
    draw.right(90)
    draw.forward(200)
    draw.penup()
    draw.hideturtle() 
    draw.setpos(-190,-110) 
    draw.pendown()
    
    def file1():
        f1=open("D:\project work\\right_angle.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,10")
    
def straight_angle():
    draw.reset()
    draw.speed(2)
    draw.color("blue")
    draw.pensize(3)
    draw.penup()
    draw.setpos(-160,90)     #this is for turtle position     
    draw.pendown() 
    draw.forward(220)
    draw.left(180)
    draw.forward(90)
    draw.right(90)
    draw.circle(30,180)
    draw.penup()
    draw.setpos(-150,-30) 
    draw.penup()
    draw.hideturtle() 
    draw.setpos(-210,-70)
    def file1():
        f1=open("D:\project work\\straight_angle.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,10")
def acute_angle():
    draw.reset()
    draw.speed(2)
    draw.color("blue")
    draw.pensize(3)
    draw.penup()
    draw.setpos(-160,90)     #this is for turtle position     
    draw.pendown()  
    draw.forward(180)
    draw.left(130)
    draw.forward(180)
    draw.penup()
    draw.hideturtle() 
    draw.setpos(-200,-45) 
    draw.pendown()
    def file1():
        f1=open("D:\project work\\acute_angle.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,10")
    

def obtuse_angle():
    draw.reset()
    draw.speed(2)
    draw.color("blue")
    draw.penup()
    draw.setpos(-160,70)     #this is for turtle position     
    draw.pendown() 
    draw.pensize(3) 
    draw.forward(180)
    draw.left(60)
    draw.forward(180)
    draw.penup()
    draw.setpos(-220,-50)
    draw.hideturtle()  
    draw.pendown()
    def file1():
        f1=open("D:\project work\\obtuse_angle.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,10")
    
    
def showing_button_1():
    button=tk.Button(master=window,text="কোণ",font=15,bg="light green",fg="black",command=angle)
    button.grid(row=1,column=1,sticky="nsew")
    button=tk.Button(master=window,text=" সমকোণ",font=15,bg="light green",fg="black",command=right_angle)
    button.grid(row=1,column=2,sticky="nsew")
    button=tk.Button(master=window,text=" সরলকোণ",font=15,bg="light green",fg="black",command=straight_angle)
    button.grid(row=1,column=3,sticky="nsew")
    button=tk.Button(master=window,text=" সূক্ষ্মকোণ",font=15,bg="light green",fg="black",command=acute_angle)
    button.grid(row=1,column=4,sticky="nsew")
    button=tk.Button(master=window,text="স্থূলকোণ ",font=15,bg="light green",fg="black",command=obtuse_angle)
    button.grid(row=1,column=5,sticky="nsew")


def angle_shape():
    button3=tk.Button(master=window,text="কোণ",font=15,bg="light green",fg="black",command=showing_button_1)
    button3.grid(row=3,column=0,sticky="nsew")

angle_shape()              #for calling angle

def triangle():            #for drawing triangle
    draw.reset()
    draw.speed(2)
    draw.pensize(3)
    draw.penup()
    draw.fillcolor("yellow")   #declaring color
    draw.begin_fill()    #start filling color
    draw.setpos(-180,0)
    draw.pendown()
    draw.forward(250)
    draw.left(120)
    draw.forward(250)
    draw.left(120)
    draw.forward(250)
    draw.left(120)
    draw.penup()
    draw.end_fill()  # end filling color
    draw.setpos(-200,-150)
    draw.hideturtle()  
    draw.pendown()
    
    def file1():
        f1=open("D:\project work\\triangle.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,10")

def right_triangle():
    draw.reset()
    draw.speed(2)
    draw.pensize(3)
    draw.penup()
    draw.setpos(-180,50)
    draw.fillcolor("orange")   #declaring color
    draw.begin_fill()    #start filling color
    draw.pendown() 
    draw.forward(160)
    draw.left(90)
    draw.forward(130)
    draw.left(129)
    draw.forward(205)
    draw.penup()
    draw.end_fill()
    draw.setpos(-200,-150)
    draw.hideturtle()  
    draw.pendown()
    
    def file1():
        f1=open("D:\project work\\right_triangle.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,10")
   
def obese_triangle():
    draw.reset()
    draw.speed(2)
    draw.pensize(3)
    draw.penup()
    draw.setpos(-180,50)
    draw.fillcolor("red")   #declaring color
    draw.begin_fill()    #start filling color
    draw.pendown() 
    draw.forward(200)
    draw.left(60)
    draw.forward(150)
    draw.left(145)
    draw.forward(309)
    draw.penup()
    draw.end_fill()
    draw.setpos(-210,-150)
    draw.hideturtle()  
    draw.pendown()
   
    def file1():
        f1=open("D:\project work\\obese_triangle.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,10")
   
def isosceles_triangle():
    draw.reset()
    draw.speed(2)
    draw.pensize(3)
    draw.penup()
    draw.setpos(-180,50)
    draw.fillcolor("green")   #declaring color
    draw.begin_fill()    #start filling color
    draw.pendown() 
    draw.forward(300)
    draw.left(120)
    draw.forward(150)
    draw.left(90)
    draw.forward(260)
    draw.penup()
    draw.end_fill()
    draw.setpos(-200,-180)
    draw.hideturtle()  
    draw.pendown()
   
    def file1():
        f1=open("D:\project work\\isoscelse_triangle.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,10")
   
def showing_button_1():
    button=tk.Button(master=window,text="সমবাহু ত্রিভুজ",font=15,bg="orange",fg="black",command=triangle)
    button.grid(row=1,column=1,sticky="nsew")
    button=tk.Button(master=window,text="সমকোণী ত্রিভুজ",font=15,bg="orange",fg="black",command=right_triangle)
    button.grid(row=1,column=2,sticky="nsew")
    button=tk.Button(master=window,text="স্থূলকোণী ত্রিভুজ",font=15,bg="orange",fg="black",command=obese_triangle)
    button.grid(row=1,column=3,sticky="nsew")
    button=tk.Button(master=window,text="বিষমবাহু ত্রিভুজ",font=15,bg="orange",fg="black",command=isosceles_triangle)
    button.grid(row=1,column=4,sticky="nsew")
    button=tk.Button(master=window,fg="white")
    button.grid(row=1,column=5,sticky="nsew")


def triangle_shape():
    button3=tk.Button(master=window,text="ত্রিভুজ",font=15,bg="orange",fg="black",command=showing_button_1)
    button3.grid(row=4,column=0,sticky="nsew")

triangle_shape()              #calling triangle




def square():
    draw.reset()
    draw.speed(2)
    draw.pensize(3)
    draw.penup()
    draw.setpos(-180,70)
    draw.fillcolor("green")   #declaring color
    draw.begin_fill()    #start filling color
    draw.pendown()                  #for drawing square shape
    draw.forward(150)
    draw.left(90)
    draw.forward(150)
    draw.left(90)
    draw.forward(150)
    draw.left(90)
    draw.forward(150)
    draw.end_fill()
    draw.penup()
    draw.setpos(-250,-20)
    draw.hideturtle()  
    draw.pendown()
    
    def file1():
        f1=open("D:\project work\\square.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,10")

def rectangle():
    draw.reset()
    draw.speed(2)
    draw.pensize(3)
    draw.penup()
    draw.setpos(-180,85)
    draw.fillcolor("red")   #declaring color
    draw.begin_fill()    #start filling color
    draw.pendown()            #for drawing rectangle shape
    draw.forward(250)
    draw.left(90)
    draw.forward(150)
    draw.left(90)
    draw.forward(250)
    draw.left(90)
    draw.forward(150)
    draw.penup()
    draw.end_fill()
    draw.hideturtle() 
    draw.setpos(-200,-85) 
    draw.pendown()
    
    def file1():
        f1=open("D:\project work\\rectangle.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,10")
    
    
def parallel ():
    draw.reset()
    draw.speed(2)
    draw.pensize(3)
    draw.penup()
    draw.setpos(-180,80)
    draw.fillcolor("coral")   #declaring color
    draw.begin_fill()    #start filling color
    draw.pendown()
    draw.forward(250)
    draw.left(60)
    draw.forward(150)
    draw.left(120)
    draw.forward(250)
    draw.left(60)
    draw.forward(150)    
    draw.penup()
    draw.end_fill()
    draw.hideturtle() 
    draw.setpos(-200,-70) 
    draw.pendown()
    
    def file1():
        f1=open("D:\project work\\parallel.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,10")
    
def rhombous():
    draw.reset()
    draw.speed(2)
    draw.pensize(3)
    draw.penup()
    draw.setpos(-180,70)
    draw.fillcolor("yellow")   #declaring color
    draw.begin_fill()    #start filling color
    draw.pendown()
    draw.forward(150)
    draw.left(120)
    draw.forward(150)
    draw.left(60)
    draw.forward(150)
    draw.left(120)
    draw.forward(150)
    draw.penup()
    draw.end_fill()
    draw.hideturtle() 
    draw.setpos(-250,-80) 
    draw.pendown()
    
    def file1():
        f1=open("D:\project work\\rhombous.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,10")
    
def trapezium():
    draw.reset()
    draw.speed(2)
    draw.pensize(3)
    draw.penup()
    draw.setpos(-180,85)
    draw.fillcolor("blue")   #declaring color
    draw.begin_fill()    #start filling color
    draw.pendown()
    draw.forward(250)
    draw.left(120)
    draw.forward(120)
    draw.left(60)
    draw.forward(130)
    draw.left(60)
    draw.forward(120)
    draw.penup()
    draw.end_fill()
    draw.hideturtle() 
    draw.setpos(-200,-10)
    def file1():
        f1=open("D:\project work\\trapezium.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,10")
    
    
def showing_button():
    button=tk.Button(master=window,text="বর্গক্ষেত্র",font=15,bg="green",fg="white",command=square)
    button.grid(row=1,column=1,sticky="nsew")
    button2=tk.Button(master=window,text="আয়তক্ষেত্র ",font=15,bg="green",fg="white",command=rectangle)
    button2.grid(row=1,column=2,sticky="nsew")
    button_parallel=tk.Button(master=window,text="সামান্তরিক",font=15,bg="green",fg="white",command=parallel)
    button_parallel.grid(row=1,column=3,sticky="nsew")
    button_rhombous=tk.Button(master=window,text="রম্বস",font=15,bg="green",fg="white",command=rhombous)
    button_rhombous.grid(row=1,column=4,sticky="nsew")
    button_trapezium=tk.Button(master=window,text="ট্রাপিজিয়াম",font=15,bg="green",fg="white",command=trapezium)
    button_trapezium.grid(row=1,column=5,sticky="nsew")

def Quadrilateral_shape():
    button2=tk.Button(master=window,text="চতুর্ভুজ",font=15,bg="green",fg="white",command=showing_button)
    button2.grid(row=5,column=0,sticky="nsew")

Quadrilateral_shape()          #quadrilateral shape funtion calling

def circle():                   #for drawing circle  
    draw.reset()
    draw.pensize(3)
    draw.speed(2)
    draw.color("blue")
    draw.penup()
    draw.setpos(-40,100)
    draw.pendown()
    draw.circle(100)
    draw.left(90)
    draw.penup()
    draw.forward(99)
    draw.pendown()
    draw.forward(1)
    draw.penup()
    draw.color("black")
    draw.hideturtle() 
    draw.setpos(-220,-50)
    def file1():
        f1=open("D:\project work\\circle.txt","r",encoding="utf-8")
        global m1
        m1=f1.read()
        f1.close()
    file1()
    draw.write(m1,font="arial,15")
   

def circle_b():
    button=tk.Button(master=window,text="বৃত্ত",font=15,bg="violet",fg="black",command=circle)
    button.grid(row=1,column=1,sticky="nsew")
    button=tk.Button(master=window)
    button.grid(row=1,column=2,sticky="nsew")
    button=tk.Button(master=window)
    button.grid(row=1,column=3,sticky="nsew")
    button=tk.Button(master=window)
    button.grid(row=1,column=4,sticky="nsew")
    button=tk.Button(master=window)
    button.grid(row=1,column=5,sticky="nsew")

def circle_shape():
    button2=tk.Button(master=window,text="বৃত্ত",font=15,bg="violet",fg="black",command=circle_b)
    button2.grid(row=6,column=0,sticky="nsew")
   

circle_shape()                 #for calling circle


window.mainloop()