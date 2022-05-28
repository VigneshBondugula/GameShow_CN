# GameShow_CN

The project is a game show. There is a host who conducts the show and
participants/players who provide answers. Three participants are required to play the game.
The host has a long list of questions and correct answers with him. He randomly chooses
one of the questions (making sure it is not a repeat of previous questions) and sends to all
three players. The players receive the question, think about the answer for a while and press
the buzzer. There is a timer for 10 seconds for buzzer to be pressed. Otherwise, the host
moves on to the next question. The first one to press the buzzer is given a chance to provide
the answer within 10 seconds. If the answer is correct, he is given 1 point, otherwise -0.5.
Nobody gets chance to answer this question again. The host then proceeds with the next
question. The game stops when any player gets 5 points and that player is declared the
winner. If the number of questions are completed the game is declared to be tied and the
scores are displayed.

INSTRUCTIONS TO RUN:-

1) Open terminal and go to the directory in which the project files are present.
2) Run python3 server.py
3) Then open 3 other terminals in the same directory.
4) Run python3 client .py in all the three terminals and play the quiz.
