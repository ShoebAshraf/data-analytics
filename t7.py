from turtle import*
s=Screen()
s.setup(500,500) #change screen size using x and y pixels
fillcolor('red')
pencolor('red')
for i in range(5):
    lt(72) #rotate 72 deg
    penup()
    fd(80)
    pendown()
    begin_fill() #set coloring
    circle(40)
    end_fill() #fill color in created circle
    penup()
    bk(80)
    pendown()
mainloop()
