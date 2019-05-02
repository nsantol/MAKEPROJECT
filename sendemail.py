import smtplib #module for sending email
import sched, time   #Sched module to schedule the program to run every certani time
import xlrd
import datetime
import config #module we created with login information. 
import math

schedule.every().monday.at("08:00").do(send_email, subject, msg) #You can put any day and time, and module will work.
schedule.every().tuesday.at("08:00").do(send_email, subject, msg) #We want the program to send an email every day in the morning, so we added every day.
schedule.every().wednesday.at("08:00").do(send_email, subject, msg)
schedule.every().thursday.at("08:00").do(send_email, subject, msg)
schedule.every().friday.at("08:00").do(send_email, subject, msg)
schedule.every().saturday.at("08:00").do(send_email, subject, msg)
schedule.every().sunday.at("08:00").do(send_email, subject, msg)


while True:  #Program need to be constantly running. But need to add sleep because computer can crash.

    schedule.run_pending() #imported from module "schedule"
    time.sleep(2)  #Module will run every 2 seconds. Can put a longer time if you want the module to send you email only once a day.


#if localtime.startswith("Tue"):
    #send_email(subject, msg)

#localtime= localtime+604800

#df = pd.read_excel ('tasks.xlsx')
#print(df)


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = "Subject: {}\n\n{}".format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.RECEIVER_ADDRESS, message)
        server.quit()
        print("Success Email sent!")
    except:
        print("Email failed to send.")

subject = "Things to do today"
msg=""

def excel_date(date1):
    temp = datetime.datetime(1899, 12, 30)
    delta = date1 - temp
    return(math.floor((delta.days) + (float(delta.seconds) / 86400)))

workbook= xlrd.open_workbook("tasks.xlsx")
sheet=workbook.sheet_by_index(0)

now = datetime.datetime.now()

for i in range(sheet.nrows):
    if sheet.cell_value(i, 1)==int(excel_date(now)):
        msg="Your tasks for today are: \n"+ str(sheet.cell_value(i, 0))
        print(msg)
        send_email(subject, msg)
    else:
        print('not today')
