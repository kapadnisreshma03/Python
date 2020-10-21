
def main():##main function
    import subprocess as s##importing subprocess to use the system pink command
    import turtle##importing turtle graphics
    ######using existing class for the system ping command####
    class PING:
        def __init__(self, ip):
            self.ip = str(ip)
        def getstatus(self):
            if(s.call(["ping",self.ip])==0):
                return True
            else:
                return False
    ####################################################
    window = turtle.Screen()
    window.title("Network-pinger")
    window.clear()
    window.setup(700,400)##screen setup
    window.bgcolor("black")
    pen=turtle.Turtle()
    pen.pencolor("red")
    pen.hideturtle()
    pen.pu()
    pen.setpos(-200,-80)
    pen.pd()
    
    def quit():#fuction for quiting the tool
        turtle.bye()
    def restart():##tunction to restart the tool
        main()
    ip=window.textinput("Device","Enter the IP/Domain name: ")##onscreen user input window
    pen.write("Working....", font =("Arial",30,"italic"))
    c= PING(ip)###calling class PING
    if c.getstatus() == True:##if else loop to check and print if server reachable or unreachable
        window.clear()
        window.bgcolor("black")
        print ("your IP is alive")
        pen.pencolor("#29cf01")
        pen.write(    ip + " is online !!! \n \n \nHit 'r' to check another server \n     or\n 'q' to Quit",font=("Arial",25, "bold"))
        window.listen()
        window.onkey(quit,"q")
        window.onkey(restart,"r")
        while True:
            for i in range (50):
                pen.penup()
                pen.hideturtle()
                pen.fd(100)
                pen.left(90)
    else:
        window.clear()
        window.bgcolor("black")        
        pen.write(ip + " is unreachable by icmp !!! \n\n\n Hit r to check another server or q to Quit",font=("Arial",15, "bold"))
        window.listen()
        window.onkey(quit,"q")
        window.onkey(restart,"r")
        while True:
            for i in range (50):
                pen.penup()
                pen.hideturtle()
                pen.fd(100)
                pen.left(90)
main()###calling the main function

