# import python poplib module
import poplib
from email.parser import Parser
import base64
# input email address, password and pop3 server domain or ip address
email = "vtruong@infinitalk.co.jp"
password = "truong@1995"
pop3_server = "infinitalk-srv.sakura.ne.jp"

# connect to pop3 server:
server = poplib.POP3(pop3_server)
# open debug switch to print debug information between client and pop3 server.
server.set_debuglevel(1)
# get pop3 server welcome message.
pop3_server_welcome_msg = server.getwelcome().decode('utf-8')
# print out the pop3 server welcome message.
print(server.getwelcome().decode('utf-8'))

# user account authentication
server.user(email)
server.pass_(password)

# stat() function return email count and occupied disk size
print('Messages: %s. Size: %s' % server.stat())
# list() function return all email list
resp, mails, octets = server.list()
print(mails)

# retrieve the newest email index number
index = len(mails)
# server.retr function can get the contents of the email with index variable value index number.
resp, lines, octets = server.retr(index-1)

# lines stores each line of the original text of the message
# so that you can get the original text of the entire message use the join function and lines variable.
msg_content = b'\r\n'.join(lines).decode('iso-2022-jp')
print(len(lines))
print("Msg content: %s" % msg_content)
# now parse out the email object.
msg = Parser().parsestr(msg_content)

# get email from, to, subject attribute value.
email_from = msg.get('From')
email_to = msg.get('To')
email_subject = msg.get('Subject')
email_content = msg.get('Content')
print('From ' + email_from)
print('To ' + email_to)
print('Subject ' + email_subject)
email_payload = msg.get_payload(decode=True)
if msg.is_multipart():
    for part in msg.get_payload():
        print(part.get_payload())
else:
    print(msg.get_payload())
text = msg.get_payload()

# delete the email from pop3 server directly by email index.
# server.dele(index)
# close pop3 server connection.
server.quit()