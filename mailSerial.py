import imaplib
import serial
import base64
import time
import re

initialCount = 0

# serial port that micro controller is listening (ex. arduino)
serialPort = '/dev/cu.wchusbserial1410'

# your Gmail username - full email
gmailUsername = ''

# your Gmail password - base64 encoded. Use this service to encode your password: https://www.base64encode.org/
gmailPassword = ''

# mailbox you wish to track
mailbox = 'inbox'

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(gmailUsername, base64.b64decode(gmailPassword))
mail.select(mailbox)

ser = serial.Serial(serialPort, 9600)

while True:
    unreadCount = re.search("UNSEEN (\d+)", mail.status("INBOX", "(UNSEEN)")[1][0]).group(1)

    if unreadCount > initialCount:
        ser.write('y')
    else:
        ser.write('n')

    initialCount = unreadCount

    time.sleep(5)
