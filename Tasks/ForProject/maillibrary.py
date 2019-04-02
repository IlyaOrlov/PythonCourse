#  -*- coding: utf-8 -*-
import time
import email
from email.mime.text import MIMEText
#from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename
from imaplib import IMAP4_SSL
from smtplib import SMTP_SSL
from poplib import POP3_SSL


class MailLibrary(object):

    def __init__(self):
        self.imap_ssl_gm_host = 'imap.gmail.com'
        self.imap_ssl_gm_port = 993  # imap port
        self.imap_gm_username = 'mymaillogin'  # username or e-mail address
        self.imap_gm_password = 'mypassword'  # password
        self.imap_gm_server = None

        self.imap_ssl_ya_host = 'imap.yandex.ru'
        self.imap_ssl_ya_port = 993  # imap port
        self.imap_ya_username = 'mymaillogin'  # username or e-mail address
        self.imap_ya_password = 'mypassword'  # password
        self.imap_ya_server = None

        self.pop3_ssl_host = 'pop3.mail.ru'
        self.pop3_ssl_port = 995  # imap port
        self.pop3_username = 'mymaillogin'  # username or e-mail address
        self.pop3_password = 'mypassword'  # password
        self.pop3_server = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.imap_gm_server:
            self.imap_gm_server.close()
            self.imap_gm_server.logout()
            self.imap_gm_server = None
        if self.imap_ya_server:
            self.imap_ya_server.close()
            self.imap_ya_server.logout()
            self.imap_ya_server = None
        if self.pop3_server:
            self.pop3_server.quit()
            self.pop3_server = None

    @staticmethod
    def get_first_text_block(msg):
        type = msg.get_content_maintype()

        if type == 'multipart':
            for part in msg.get_payload():
                if part.get_content_maintype() == 'text':
                    return part.get_payload()
        elif type == 'text':
            return msg.get_payload()

    def get_imap_gm_mail(self, stop_function=lambda: False, timeout=10):
        criteria = u'Важный заголовок'.encode('utf-8')

        while True:
            if stop_function():
                yield None

            try:
                self.imap_gm_server = IMAP4_SSL(self.imap_ssl_gm_host,
                                                self.imap_ssl_gm_port)
                self.imap_gm_server.login(self.imap_gm_username,
                                          self.imap_gm_password)
                self.imap_gm_server.select('INBOX')
                self.imap_gm_server.literal = criteria
                res, data = self.imap_gm_server.uid('SEARCH', 'CHARSET',
                                                    'UTF-8', 'SUBJECT')
                uids = [int(s) for s in data[0].split()]
                for uid in uids:
                    # Fetch entire message
                    res, data = self.imap_gm_server.uid('FETCH', uid,
                                                        '(RFC822)')
                    msg = email.message_from_string(data[0][1])
                    text = self.get_first_text_block(msg)
                    self.imap_gm_server.uid('STORE', uid, '+FLAGS',
                                            '(\\Deleted)')
                    self.imap_gm_server.expunge()
                    yield text

                self.imap_gm_server.close()
                self.imap_gm_server.logout()
                self.imap_gm_server = None
                if len(uids) == 0:
                    time.sleep(timeout)
            except Exception as err:
                print(err)

    def get_imap_ya_mail(self, stop_function=lambda: False, timeout=10):
        criteria = u'Важный заголовок'.encode('utf-8')

        while True:
            if stop_function():
                yield None

            try:
                self.imap_ya_server = IMAP4_SSL(self.imap_ssl_ya_host,
                                                self.imap_ssl_ya_port)
                self.imap_ya_server.login(self.imap_ya_username,
                                          self.imap_ya_password)
                self.imap_ya_server.select('INBOX')
                self.imap_ya_server.literal = criteria
                res, data = self.imap_ya_server.uid('SEARCH', 'CHARSET',
                                                    'UTF-8', 'SUBJECT')

                uids = [int(s) for s in data[0].split()]
                for uid in uids:
                    # Fetch entire message
                    result, data = self.imap_ya_server.uid('FETCH', uid,
                                                           '(RFC822)')
                    msg = email.message_from_string(data[0][1])
                    text = self.get_first_text_block(msg)
                    self.imap_ya_server.uid('STORE', uid, '+FLAGS',
                                            '(\\Deleted)')
                    self.imap_ya_server.expunge()
                    yield text

                self.imap_ya_server.close()
                self.imap_ya_server.logout()
                self.imap_ya_server = None
                if len(uids) == 0:
                    time.sleep(timeout)
            except Exception as err:
                print(err)

    def get_pop3_mail(self, stop_function=lambda: False, timeout=10):
        criteria = 'Important subject'
        # Effective payload is placed from
        min_line = 18
        # to
        max_line = 24
        # in message body.

        while True:
            if stop_function():
                yield None

            try:
                self.pop3_server = POP3_SSL(self.pop3_ssl_host,
                                            self.pop3_ssl_port)
                self.pop3_server.user(self.pop3_username)
                self.pop3_server.pass_(self.pop3_password)

                stat = self.pop3_server.stat()
                for i in range(stat[0]):
                    msgnum = i + 1
                    # Retrieve headers
                    response, lines, bytes = self.pop3_server.top(msgnum, 10)
                    one_line = ' '.join(lines)
                    if one_line.find(criteria) != -1:
                        (server_msg, body, octets) = \
                            self.pop3_server.retr(msgnum)
                        text = '\n'.join(body[min_line:max_line])
                        self.pop3_server.dele(msgnum)
                        yield text
                self.pop3_server.quit()
                self.pop3_server = None
                if stat[0] == 0:
                    time.sleep(timeout)
            except Exception as err:
                print(err)

    def send_message(self, subject, msg_text, targets=None,
                     mailserver='gmail', attach_file=None):
        smtp_ssl_port = 465
        if mailserver == 'gmail':
            smtp_ssl_host = 'smtp.gmail.com'
            username = 'mymaillogin'
            password = 'mypassword'
            sender = 'mymaillogin@gmail.com'
        elif mailserver == 'yandex':
            smtp_ssl_host = 'smtp.yandex.ru'
            username = 'ya.mymaillogin'
            password = 'mypassword'
            sender = 'mymaillogin@yandex.ru'
        elif mailserver == 'mail':
            smtp_ssl_host = 'smtp.mail.ru'
            username = 'mymaillogin'
            password = 'mypassword'
            sender = 'mymaillogin@mail.ru'
        else:
            raise Exception('Incorrect mailserver "{}". '
                            'Expected imap_gmail, '
                            'imap_yandex or pop3_mail.'.format(mailserver))
        if not targets:
            targets = [sender]

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(targets)
        msg.attach(MIMEText(msg_text))
        if attach_file:
            with open(attach_file, "rb") as af:
                part = MIMEApplication(
                    af.read(),
                    Name=basename(attach_file)
                )
            # After the file is closed
            part['Content-Disposition'] = \
                'attachment; filename="%s"' % basename(attach_file)
            msg.attach(part)

        server = SMTP_SSL(smtp_ssl_host, smtp_ssl_port, timeout=60)

        server.login(username, password)
        server.sendmail(sender, targets, msg.as_string())
        server.quit()

        logmsg = '\nMessage {}:\n{}\n' \
                 'from {} is sent to {} successfully'.format(
            msg['Subject'], msg, msg['From'], msg['To'])
        print(logmsg)
