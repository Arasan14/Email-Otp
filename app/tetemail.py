import smtplib

fromaddr = 'johancatteraz@gmail.com'  
toaddrs  = 'karthicatter@gmail.com'  
msg = 'Spam email Test'  
      
username = 'karthi'  
password = 'me_pass'

server = smtplib.SMTP('smtp.gmail.com', 587)  
server.ehlo()
server.starttls()
server.login(username, password)  
server.sendmail(fromaddr, toaddrs, msg)  
server.quit()