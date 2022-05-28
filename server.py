import socket
import sys
import time
import select
server='localhost'
port=5555


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
score=[0,0,0]
s.bind((server,port))
s.listen(3)
print("Server bound to:",server,":",port)
(conn1,addr1)=s.accept()
print("Connected to Player 1 at",addr1)
conn1.sendall(str.encode("You are Player 1 \nWaiting for other players"))
(conn2,addr2)=s.accept()
print("Connected to Player 2 at",addr2)
conn2.sendall(str.encode("You are Player 2 \nWaiting for other players"))
(conn3,addr3)=s.accept()
print("Connected to Player 3 at",addr3)
conn3.sendall(str.encode("You are Player 3"))
time.sleep(0.1)
conn1.sendall(str.encode("The game is ready to begin.."))
conn2.sendall(str.encode("The game is ready to begin.."))
conn3.sendall(str.encode("The game is ready to begin.."))
time.sleep(8)

conn_list=[conn1,conn2,conn3]
questions={}
for i in range(50):
    questions["1+"+str(i)+"=??"]=str(1+i)


def sendallScore(connlist):
    global score
    for i, conn in enumerate(connlist):
        time.sleep(0.1)
        conn.sendall(str.encode("\nPlayer "+str(i+1)+", your score is: "+str(score[i])+"\n"))
        time.sleep(0.1)

def sendallscores(connlist):
    global score
    for i in range(3):
        connlist[i].sendall(str.encode("\t|\tPLAYER-1     -->       "+ str(score[0]) + "\t|\n\t|\tPLAYER-2     -->       "+ str(score[1])+"\t|\n\t|\tPLAYER-3     -->       "+ str(score[2])+"\t|"))


for ques in questions.keys():
    if(score[0]<5 and score[1]<5 and score[2]<5):
        try:
            conn1.sendall(str.encode(ques))
            conn2.sendall(str.encode(ques))
            conn3.sendall(str.encode(ques))
            time.sleep(1)
            print("Sending:", ques)
            read_sockets, _, _ = select.select(conn_list, [], [],10)
            time.sleep(10)
            read_sockets_all, _, _ = select.select(conn_list, [], [],3)
            print(read_sockets)
            print(read_sockets_all)
            for conn in read_sockets_all:
                conn.recv(1024)

            if(read_sockets==[]):
                print("No one pressed the buzzer\nMoving on to next question.")
                conn1.sendall(str.encode("No one pressed the buzzer\nMoving on to next question."))
                conn2.sendall(str.encode("No one pressed the buzzer\nMoving on to next question."))
                conn3.sendall(str.encode("No one pressed the buzzer\nMoving on to next question."))
                time.sleep(2)
                sendallScore(conn_list)
                time.sleep(3)

            elif(read_sockets[-1]==conn_list[0]):
                player=conn1
                conn1.sendall(str.encode("You can answer the question"))
                conn2.sendall(str.encode("Player 1 has pressed the buzzer.."))
                conn3.sendall(str.encode("Player 1 has pressed the buzzer.."))
                time.sleep(10)
                answer = player.recv(1024).decode('utf-8')
                print(answer)
                if (questions[ques] == answer):
                    score[0] += 1
                    player.sendall(str.encode("You gave the right answer"))
                else:
                    score[0] -= 0.5
                    player.sendall(str.encode("You gave the wrong answer"))
                sendallScore(conn_list)
                time.sleep(3)

            elif(read_sockets[-1]==conn_list[1]):
                player=conn2
                conn2.sendall(str.encode("You can answer the question"))
                conn1.sendall(str.encode("Player 2 has pressed the buzzer.."))
                conn3.sendall(str.encode("Player 2 has pressed the buzzer.."))
                time.sleep(10)
                answer = player.recv(1024).decode('utf-8')
                print(answer)
                if (questions[ques] == answer):
                    score[1] += 1
                    player.sendall(str.encode("You gave the right answer"))
                else:
                    score[1] -= 0.5
                    player.sendall(str.encode("You gave the wrong answer"))
                sendallScore(conn_list)
                time.sleep(3)

            elif(read_sockets[-1]==conn_list[2]):
                player=conn3
                conn3.sendall(str.encode("You can answer the question"))
                conn2.sendall(str.encode("Player 3 has pressed the buzzer.."))
                conn1.sendall(str.encode("Player 3 has pressed the buzzer.."))
                time.sleep(10)
                answer = player.recv(1024).decode('utf-8')
                print(answer)
                if (questions[ques] == answer):
                    score[2] += 1
                    player.sendall(str.encode("You gave the right answer"))
                else:
                    score[2] -= 0.5
                    player.sendall(str.encode("You gave the wrong answer"))
                sendallScore(conn_list)
                time.sleep(3)

        except socket.error as e:
            print(e)
            break
    else:
        conn1.sendall(str.encode("The game has ended."))
        time.sleep(0.1)
        conn2.sendall(str.encode("The game has ended."))
        time.sleep(0.1)
        conn3.sendall(str.encode("The game has ended."))
        time.sleep(0.1)
        sendallscores(conn_list)
        time.sleep(1)
        if(score[0]>=3):
            winner="Player1"
        elif(score[1]>=3):
            winner="Player2"
        else:
            winner="Player3"
        conn1.sendall(str.encode("The winner is:"+ winner))
        time.sleep(0.1)
        conn2.sendall(str.encode("The winner is:"+ winner))
        time.sleep(0.1)
        conn3.sendall(str.encode("The winner is:"+ winner))
        conn1.shutdown(1)
        conn2.shutdown(1)
        conn3.shutdown(1)
        s.close()
        quit()

conn1.sendall(str.encode("The game has ended."))
time.sleep(0.1)
conn2.sendall(str.encode("The game has ended."))
time.sleep(0.1)
conn3.sendall(str.encode("The game has ended."))
time.sleep(0.1)
sendallscores(conn_list)
time.sleep(1)
conn1.sendall(str.encode("TIE GAME   -  Out of questions"))
time.sleep(0.1)
conn2.sendall(str.encode("TIE GAME   -  Out of questions"))
time.sleep(0.1)
conn3.sendall(str.encode("TIE GAME   -  Out of questions"))
conn1.shutdown(1)
conn2.shutdown(1)
conn3.shutdown(1)
s.close()
quit()