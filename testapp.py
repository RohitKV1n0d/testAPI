
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("rohitvinod92@gmail.com@gmail.com", "rkv#1357")
server.sendmail("rohitvinod92@gmail.com@gmail.com", "crizal501@gmail.com", "body")
server.quit()