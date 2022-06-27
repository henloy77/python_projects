import smtplib

# simple mail transport protocol
myemail = "healm.create@gmail.com"
password = "Vmet@18206"
connection = smtplib.SMTP("smtp.gmail.com")

to_email = "henloy77@gmail.com"

connection.starttls()
#tls = transport layer security secures connection to email server

# login
connection.login(user=myemail, password = password)

# send email
connection.send(from_addr=myemail,to_addrs = to_email, msg = "Hello")

# close connection
connection.close()
