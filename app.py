import smtplib
import imaplib
# import pprint
import re
import email
from difflib import get_close_matches
from email.message import EmailMessage

smtp_host = "smtp.gmail.com"
imap_host = "imap.gmail.com"
smtp_port = 587
imap_port = 993
sender = "vickyboston20@gmail.com"
dummy_receiver = "perficient@emailna.co"
tester = "dee77pak@gmail.com"
password = "Vickybeema@20"

try:
    # connect(smtp) to host using port
    smtpObj = smtplib.SMTP(smtp_host, smtp_port)
    # connect(imap) to host using SSL
    imapObj = imaplib.IMAP4_SSL(imap_host, imap_port)

    print(smtpObj.ehlo())
    print(smtpObj.starttls())
    # login to server(smtp)
    print(smtpObj.login(sender, password))
    # login to server(imap)
    print(imapObj.login(sender, password))
    # select the Folder Inbox in gmail
    print(imapObj.select('Inbox'))
    imapObj.select('INBOX', readonly=True)
    # select the unread email from particular user
    status, response = imapObj.search(None, '(UNSEEN)', '(FROM {tester})'.format(tester=tester))
    unread_msg_nums = response[0].split()
    print(unread_msg_nums)
    for i in unread_msg_nums:
        # read the mail body
        # rawMessages = imapObj.fetch(i, 'BODY[]')
        rawMessages = imapObj.fetch(i, '(RFC822)')
        print('\nMessage: {0}'.format(i))
        # pprint.pprint(rawMessages[1][0][1])
        msg = email.message_from_bytes(rawMessages[1][0][1])
        msg_subject = msg["Subject"]
        print(msg_subject)
        msg_receiver = msg["From"]
        # regex for email id
        msg_receiver = re.search(r"(\W|^)[\w.+\-]*@gmail\.com(\W|$)", msg_receiver)
        print(msg_receiver.group(0))
        # remove the first and last character from email id
        receiver = msg_receiver.group(0)[1:-1]
        print(receiver)
        # Template for message 1
        # Create the base text message.
        msg = EmailMessage()
        msg['Subject'] = "Automation project"
        msg['From'] = sender
        msg['To'] = receiver
        msg.set_content("""\
        This is a test e-mail message
        """)

        # Template for message 2
        message2 = """From: vickyboston20 <{sender}>
        To: perficient <{receiver}>
        Subject: SMTP e-mail test
        
        This is a test e-mail message auth token for home automation.""".format(sender=sender, receiver=receiver)

        # Template for message 3
        msg3 = EmailMessage()
        msg3['Subject'] = "Steam Access"
        msg3['From'] = sender
        msg3['To'] = receiver
        msg3.set_content("""\
        This is a test e-mail message for steam access
        """)

        # send the mail
        msg_subject = msg_subject.lower()
        print(msg_subject)
        match1 = ["fwd: auth token for smart home project and device smart home"]
        match2 = ["fwd: auth token for home automation project and device home automation"]
        match3 = ["fwd: your steam account: access from new computer"]
        print(len(get_close_matches(msg_subject, match1)))
        print(len(get_close_matches(msg_subject, match2)))
        print(len(get_close_matches(msg_subject, match3)))
        if len(get_close_matches(msg_subject, match1)) > 0:
            smtpObj.send_message(msg)
            print("Successfully sent email1\n")
        elif len(get_close_matches(msg_subject, match2)) > 0:
            smtpObj.sendmail(sender, receiver, message2)
            print("Successfully sent email2\n")
        elif len(get_close_matches(msg_subject, match3)) > 0:
            smtpObj.send_message(msg3)
            print("Successfully sent email3\n")
        else:
            print("mail not yet received\n")
    # close the connection
    smtpObj.quit()
except smtplib.SMTPException:
    print("Error: unable to send email")
