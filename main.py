import boto3
client = boto3.client(
    'ses',
    region_name='us-west-2',
    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
)
response = client.send_email(
    Destination={
        'ToAddresses': ['nitin.gadekar.prime@gmail.com', 'niteengadekar@gmail.com'],
    },
    Message={
        'Body': {
            'Text': {
                'Charset': 'UTF-8',
                'Data': 'THis is mail from AWS SES smtp client',
            },
        },
        'Subject': {
            'Charset': 'UTF-8',
            'Data': 'Python SES test email',
        },
    },
    Source='nitin.gadekar@gmail.com',
)
