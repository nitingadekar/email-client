import boto3
import os
import sys
client = boto3.client(
    'ses',
    region_name='us-west-2',
    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
)

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


commit_hash = os.environ.get("CI_COMMIT_SHORT_SHA") or "manual trigger"
build_id = os.environ.get("CI_JOB_ID") or "sample trigger"
user_mail = os.environ.get("GITLAB_USER_EMAIL") or "nitin.gadekar@talentica.com"

mail_list = list(sys.argv[2:]) or ['nitin.gadekar.patil@gmail.com']
attachment_file = sys.argv[1] or "index.html"
message = MIMEMultipart()
message['Subject'] = "Mail with attachment report"
message['From'] = 'niteengadekar@gmail.com'
message['To'] = ', '.join(mail_list)

# message body
part = MIMEText('PFA attached report', 'html')

message.attach(part)
attachment_string = 'false'

# attachment
if attachment_string:   # if bytestring available
    part = MIMEApplication(open(attachment_file, 'rb').read())
else:    # if file provided
    part = MIMEApplication(str.encode('attachment_string'))
part.add_header('Content-Disposition', 'attachment', filename=attachment_file)
message.attach(part)

# send email  
response = client.send_raw_email(
    Source=message['From'],
    Destinations= mail_list ,
    RawMessage={
        'Data': message.as_string()
    }
)
print (response, mail_list)
