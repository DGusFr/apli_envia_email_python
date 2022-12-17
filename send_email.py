import email.message
import smtplib
import pandas as pd

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders

corpo = """Olá
 <p>Prezado Contador</p>

 <p>Segue o Demonstrativo das minhas despesas, do mes de Janeiro,</p>
 <p>em anexo, para declaração do Imposto de Renda</p>
  

 <p>Qualquer dúvida estou à disposição.</p>

 <p>Att.</p> """

msg = MIMEMultipart()
msg['Subject'] = "Assunto"
msg['From'] = 'seuemail@email.com'
msg['To'] = 'destinatario@email.com'
password = 'senhadeappdogoogle'
msg.add_header('Content-Type', 'text/html')
msg.attach(MIMEText(corpo, 'html'))

cam_arquivo = "caminho_do_arquivo\despesas.pdf"
attachment  = open(cam_arquivo, 'rb')

att = MIMEBase('application', 'octet-stream')
att.set_payload(attachment.read())
encoders.encode_base64(att)

att.add_header('Content-Disposition', f'attachment; filename= despesas.pdf')
attachment.close()

msg.attach(att)

s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()
s.login(msg['From'], password)
s.sendmail(msg['From'], [msg['To']], msg.as_string())
s.quit()



