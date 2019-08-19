# PythonEmailSender
The following code is made to help the beginner in python to send an email with attachments to any mail id

## Required imports for the code are 
import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

from email.mime.base import MIMEBase

from email import encoders


## Parameter for the function
```
send_email(from_email_address,from_email_password,sender_mail_to,subjet_mail,message_mail,attachment_filename,path_of_file_toosend)
```
### 7 Parameter 
**from_email_address** : Mail id from which mail is to be sent
"XXXXXXX@gmail.com"

**from_email_password** : Password of the mail which is to be used for sending mail
"XXXXXXXXXXXXXX"

**sender_mail_to** : Email id of the user mail is to be sent to
"XXXXXX@gmail.com"

**subjet_mail** : Text to be displayed on the Subject of the mail.
"Pyhton Mail"

**message_mail** : Message to be send in the mail is to be displyed in the mail 
"Hi \n User"

**attachment_filename** : File name to be displayed for the send file 
"Test_Attached File"

**path_of_file_toosend** : The absoulute file path of the file to be send
"E:&#92;&#92;Test&#92;&#92;gradlew.bat" for windows

