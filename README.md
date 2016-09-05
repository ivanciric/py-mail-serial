# py-mail-serial
Check email count and send notification to serial.

Connect to Gmail IMAP server and check the count of unread messages.
Every time the count is bigger than the last reading, it means that you have new mail.
If that is the case, script will output 'y' to serial port, otherwise 'n'.

You can listen to the serial port specified in the code with microcontroller of your choice,
and react accordingly.
