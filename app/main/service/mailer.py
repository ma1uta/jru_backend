import smtplib
import os

from email.message import EmailMessage
from jinja2 import Environment, FileSystemLoader

from ..config import config

env = Environment(loader=FileSystemLoader('%s/../templates/' % os.path.dirname(__file__)))


class EmailData:
    to = None
    login = None
    subject = None
    link = None

    def __init__(self, email, username, subject, link):
        self.to = email
        self.login = email
        self.subject = subject
        self.link = link


def send_email(kind, data):
    cfg = config()

    msg = EmailMessage()

    template = env.get_template('%s.txt' % kind)
    msg.set_content(template.render(data=data))

    msg['Subject'] = data.subject
    msg['From'] = cfg.email_sender
    msg['To'] = data.to
    smtp = smtplib.SMTP(cfg.email_server)
    smtp.send_message(msg)
    smtp.quit()
