import socket
import sys
import time
import select
import termios
import os

server='localhost'
port=5555
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((server,port))
print(c.recv(2048).decode())
time.sleep(1)
print(c.recv(2048).decode())
time.sleep(5)
flag=True
count=0
while flag:
    time.sleep(3)
    os.system('clear')
    question=c.recv(2048).decode()
    if(question!="The game has ended."):
        count+=1
        print("--------------------------GAME SHOW-------------------------\n")
        print("QUESTION-"+str(count),"---->",question)
        buzzer=""
        print("Press 1 and enter to press the buzzer..You have 10 seconds:")
        i, o, e = select.select([sys.stdin], [], [], 10)
        if (i):
            buzzer = sys.stdin.readline().strip()
        else:
            print("You said nothing!")
        c.send(str.encode(buzzer))
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
        reply=c.recv(2048).decode()

        if(reply=="You can answer the question"):
            print(reply,"\nYou have 10 seconds to answer..")
            i, o, e = select.select([sys.stdin], [], [], 10)
            answer=" "
            if(i):
                answer=sys.stdin.readline().strip()
                print("Your ans:",answer)
            else:
                print("You said nothing!")
            c.send(str.encode(answer))
            print(c.recv(2048).decode())
            termios.tcflush(sys.stdin, termios.TCIFLUSH)

        elif(reply=="No one pressed the buzzer\nMoving on to next question."):
            print(reply)
            time.sleep(2)
            termios.tcflush(sys.stdin, termios.TCIFLUSH)

        else:
            print(reply)
            time.sleep(10)
            termios.tcflush(sys.stdin, termios.TCIFLUSH)

        print(c.recv(2048).decode())

    else:
        flag=False
        print("----------------------------THE END-----------------------------.\v")
        print("\t-----------------------------------------")
        print(c.recv(4096).decode())
        print("\t-----------------------------------------")
        print(c.recv(2048).decode())
        time.sleep(5)






