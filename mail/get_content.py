import poplib
import email

SERVER = "infinitalk-srv.sakura.ne.jp"
USER = "vtruong@infinitalk.co.jp"
PASSWORD = "truong@1995"

server = poplib.POP3(SERVER)
server.user(USER)
server.pass_(PASSWORD)

numMessages = len(server.list()[1])


(server_msg, body, octets) = server.retr(numMessages)
for j in body:
    try:
        msg = email.message_from_string(j.decode("utf-8"))
        strtext = msg.get_payload()
        print (strtext)
    except:
        print("Can't read ")
        pass