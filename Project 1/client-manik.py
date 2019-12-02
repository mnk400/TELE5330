from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)

#function to calculate the mathematical question
def mathcal(data):
    ans_data = data.split(" ")
    if(ans_data[0] == "MATH"):     #checking if we're done with math questions
        calvar = ans_data[1] + ans_data[2] + ans_data[3]
        answer_calvar = int(eval(calvar))
        return str(answer_calvar)
    else:
        return "DONE"

saddr = ('127.0.0.1', 8888)
s.connect(saddr)

data = s.recv(1024).decode()
print(data)
str_hello = "HELLO kumar.man\n"
s.send(str_hello.encode())

while True:
    data = s.recv(1024).decode()
    print(data)
    answer = mathcal(data)
    if(answer == "DONE"):
        s.close()
        exit()
      
    else:
        print(answer)
        str_answer = "ANSWER " + answer + "\n"
        s.send(str_answer.encode())
