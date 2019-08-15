# Python code for Sending mail with attachments
# from  Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email( from_email_address,from_email_password,sender_mail_to,subjet_mail,message_mail,attachment_filename,path_of_file_toosend):

    try:

        # instance of MIMEMultipart
        msg = MIMEMultipart()

        # storing the senders email address
        msg['From'] = from_email_address

        # storing the receivers email address
        msg['To'] = sender_mail_to

        # storing the subject
        msg['Subject'] = subjet_mail

        # string to store the body of the mail
        body = message_mail

        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # open the file to be sent
        filename = attachment_filename
        attachment = open(path_of_file_toosend, "rb")

        # instance of MIMEBase and named as mmb
        mmb = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        mmb.set_payload((attachment).read())

        # encode into base64
        encoders.encode_base64(p)

        mmb.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        msg.attach(p)

        # creates SMTP session
        smtp_session = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        smtp_session.starttls()

        # Authentication
        smtp_session.login(from_email_address, from_email_password)

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        smtp_session.sendmail(from_email_address, sender_mail_to, text)

        # terminating the session
        smtp_session.quit()

        end_msg = "Email Sending Process Ends..."

    except NameError:
        end_msg = "Variable value not defined"

    except:
        end_msg = "Something else went wrong"
    finally:
        attachment.close()
        print(end_msg)
        return True

