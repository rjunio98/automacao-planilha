import smtplib
import ssl
import mimetypes
from email.message import EmailMessage

password = open("senha", "r").read()
from_email = "robledorjunior1@gmail.com"
to_email = "robledorjunior1@gmail.com"
subject = "Automação Planilha"
body = """
Olá,
Segue em anexo a automação da planilha para a empresa XYZ.
Abs
"""

message = EmailMessage()
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subject

message.set_content(body)
safe = ssl.create_default_context()

anexo = "test.ods"
mime_type, mimesubtype = mimetypes.guess_type(anexo)[0].split("/")
with open(anexo, "rb") as a:
    message.add_attachment(
        a.read(),
        maintype=mime_type,
        subtype=mimesubtype,
        filename=anexo
    )

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.send_email(
        from_email,
        to_email,
        message.as_string()
    )
