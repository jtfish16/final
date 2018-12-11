import pandas
import config


dfs = pandas.read_html('https://rate.bot.com.tw/xrt/all/day')
# print(type(dfs))
# print(len(dfs))
currency = dfs[0]
# print(type(currency))
currency = currency.iloc[:,0:5]
# print(currency)
currency = currency.iloc[7:8,:]

# df.plot(kind = 'line', [y = 'currency2', 'cash'])

currency.columns = [u'Type', u'Cash_buyin', u'Cash_sellout', u'Period_buyin', u'Period_sellout']
currency[u'Type'] = currency[u'Type'].str.extract('\((\w+)\)')
currency.to_excel('currency.xlsx')

# print(currency)
from datetime import datetime

currency['Date'] = datetime.now().strftime('%Y-%m-%d')
currency['Date'] = pandas.to_datetime(currency['Date'])

# print(currency.info())
print(currency)

# import sqlite3

# with sqlite3.connect('\\') as db:
#     currency.to_sql('currency', con=db, if_exists='append')

# with sqlite3.connect('currency.sqlite') as db:
#     df = pandas.read_sql_query('select* from currency', con=db)
# print(df)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddar = config.fromemail
toaddr = config.toemail
passwd = config.passwd
msg = MIMEMultipart()
msg['From'] = fromaddar
msg['To'] = toaddr
msg['Subject'] = '[Notification]'

body = 'hello world'
msg.attach(MIMEText(body, 'plain'))


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddar, passwd)
text = msg.as_string()
server.sendmail(fromaddar, toaddr, text)
server.quit()

