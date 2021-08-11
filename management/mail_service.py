import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
from datetime import datetime
from datetime import timedelta



def send_invoice_and_credentials(username, password, shop_name, email_address):
    subject = "BharatOff - Invoice Mailer"
    body = "Welcome to BharatOff family, \n\nThank you for choosing BharatOff to reach your customers. Please find your username and password along with the Invoice of your Transaction.\nUsername - "+username+"\nPassword - "+password+"\n\nWe wish you a great sale ahead.\n\nRegards,\nTeam BharatOff"
    sender_email = "Info@bharatoff.com"
    receiver_email = email_address
    password = "jtyrjtclwsizuxom" #"@Info8602950609"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "./invoice/"+shop_name+".pdf"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

def send_credentials(name ,username_client, password_client, email):
    sender_email = "Info@bharatoff.com"
    receiver_email = email
    password = "jtyrjtclwsizuxom"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Welcome to BharatOff"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = """\
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
    <head>
    <!--[if gte mso 9]>
    <xml>
    <o:OfficeDocumentSettings>
        <o:AllowPNG/>
        <o:PixelsPerInch>96</o:PixelsPerInch>
    </o:OfficeDocumentSettings>
    </xml>
    <![endif]-->
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="x-apple-disable-message-reformatting">
    <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->
    <title></title>
    
        <style type="text/css">
        table, td { color: #000000; } @media only screen and (min-width: 570px) {
    .u-row {
        width: 550px !important;
    }
    .u-row .u-col {
        vertical-align: top;
    }

    .u-row .u-col-100 {
        width: 550px !important;
    }

    }

    @media (max-width: 570px) {
    .u-row-container {
        max-width: 100% !important;
        padding-left: 0px !important;
        padding-right: 0px !important;
    }
    .u-row .u-col {
        min-width: 320px !important;
        max-width: 100% !important;
        display: block !important;
    }
    .u-row {
        width: calc(100% - 40px) !important;
    }
    .u-col {
        width: 100% !important;
    }
    .u-col > div {
        margin: 0 auto;
    }
    }
    body {
    margin: 0;
    padding: 0;
    }

    table,
    tr,
    td {
    vertical-align: top;
    border-collapse: collapse;
    }

    p {
    margin: 0;
    }

    .ie-container table,
    .mso-container table {
    table-layout: fixed;
    }

    * {
    line-height: inherit;
    }

    a[x-apple-data-detectors='true'] {
    color: inherit !important;
    text-decoration: none !important;
    }

    </style>
    
    

    <!--[if !mso]><!--><link href="https://fonts.googleapis.com/css?family=Lato:400,700&display=swap" rel="stylesheet" type="text/css"><!--<![endif]-->

    </head>

    <body class="clean-body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #f7f7f7;color: #000000">
    <!--[if IE]><div class="ie-container"><![endif]-->
    <!--[if mso]><div class="mso-container"><![endif]-->
    <table style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #f7f7f7;width:100%" cellpadding="0" cellspacing="0">
    <tbody>
    <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #f7f7f7;"><![endif]-->
        

    <div class="u-row-container" style="padding: 0px;background-color: transparent">
    <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 550px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:550px;"><tr style="background-color: #ffffff;"><![endif]-->
        
    <!--[if (mso)|(IE)]><td align="center" width="550" style="width: 550px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
    <div class="u-col u-col-100" style="max-width: 320px;min-width: 550px;display: table-cell;vertical-align: top;">
    <div style="width: 100% !important;">
    <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
    
    <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
        <tr>
        <td style="overflow-wrap:break-word;word-break:break-word;padding:30px 10px 10px;font-family:arial,helvetica,sans-serif;" align="left">
            
    <h1 style="margin: 0px; line-height: 140%; text-align: center; word-wrap: break-word; font-weight: normal; font-family: arial,helvetica,sans-serif; font-size: 26px;">
        Welcome to BharatOff
    </h1>

        </td>
        </tr>
    </tbody>
    </table>

    <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
        <tr>
        <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
            
    <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #f1f1f1;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
        <tbody>
        <tr style="vertical-align: top">
            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
            <span>&#160;</span>
            </td>
        </tr>
        </tbody>
    </table>

        </td>
        </tr>
    </tbody>
    </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
    </div>
    <!--[if (mso)|(IE)]></td><![endif]-->
        <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
        </div>
    </div>
    </div>



    <div class="u-row-container" style="padding: 0px;background-color: transparent">
    <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 550px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:550px;"><tr style="background-color: #ffffff;"><![endif]-->
        
    <!--[if (mso)|(IE)]><td align="center" width="550" style="width: 550px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
    <div class="u-col u-col-100" style="max-width: 320px;min-width: 550px;display: table-cell;vertical-align: top;">
    <div style="width: 100% !important;">
    <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
    
    <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
        <tr>
        <td style="overflow-wrap:break-word;word-break:break-word;padding:10px 15px;font-family:arial,helvetica,sans-serif;" align="left">
            
    <div style="line-height: 140%; text-align: left; word-wrap: break-word;">
        <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 16px; line-height: 22.4px;"><strong>Hi """+name+""",</strong></span></p>
    <p style="font-size: 14px; line-height: 140%;"><br /><span style="font-size: 16px; line-height: 22.4px;">Welcome to BharatOff Family!</span></p>
    <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 140%;">Thanks for choosing our services for expanding your business outreach and customer base. We are so excited to be with you in your success.</p>
    <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 140%;">Please find these credentials to login into our dashboard and make a few changes there to customize your customer reach.</p>
    <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 140%;">Username - """+username_client+"""</p>
    <p style="font-size: 14px; line-height: 140%;">Password - """+password_client+"""</p>
    <p style="font-size: 14px; line-height: 140%;">Dashboard - """+"""<a href="https://bharatoff.com/dashboard">Click here</a>"""+"""</p>
    <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 16px; line-height: 22.4px;">Support Team,</span><br /><strong>BharatOff</strong><br />&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </p>
    </div>

        </td>
        </tr>
    </tbody>
    </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
    </div>
    <!--[if (mso)|(IE)]></td><![endif]-->
        <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
        </div>
    </div>
    </div>



    <div class="u-row-container" style="padding: 0px;background-color: transparent">
    <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 550px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:550px;"><tr style="background-color: #ffffff;"><![endif]-->
        
    <!--[if (mso)|(IE)]><td align="center" width="550" style="width: 550px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
    <div class="u-col u-col-100" style="max-width: 320px;min-width: 550px;display: table-cell;vertical-align: top;">
    <div style="width: 100% !important;">
    <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
    
    <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
        <tr>
        <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
            
    <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #f1f1f1;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
        <tbody>
        <tr style="vertical-align: top">
            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
            <span>&#160;</span>
            </td>
        </tr>
        </tbody>
    </table>

        </td>
        </tr>
    </tbody>
    </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
    </div>
    <!--[if (mso)|(IE)]></td><![endif]-->
        <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
        </div>
    </div>
    </div>



    <div class="u-row-container" style="padding: 0px;background-color: transparent">
    <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 550px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:550px;"><tr style="background-color: #ffffff;"><![endif]-->
        
    <!--[if (mso)|(IE)]><td align="center" width="550" style="width: 550px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
    <div class="u-col u-col-100" style="max-width: 320px;min-width: 550px;display: table-cell;vertical-align: top;">
    <div style="width: 100% !important;">
    <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
    
    <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
        <tr>
        <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
            
    <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #f1f1f1;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
        <tbody>
        <tr style="vertical-align: top">
            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
            <span>&#160;</span>
            </td>
        </tr>
        </tbody>
    </table>

        </td>
        </tr>
    </tbody>
    </table>

    <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
        <tr>
        <td style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 30px;font-family:arial,helvetica,sans-serif;" align="left">
            
    <div style="line-height: 140%; text-align: left; word-wrap: break-word;">
        <p style="font-size: 14px; line-height: 140%;"><strong>Questions? </strong>Contact us anytime at info@bharatoff.com</p>
    </div>

        </td>
        </tr>
    </tbody>
    </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
    </div>
    <!--[if (mso)|(IE)]></td><![endif]-->
        <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
        </div>
    </div>
    </div>



    <div class="u-row-container" style="padding: 0px;background-color: transparent">
    <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 550px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:550px;"><tr style="background-color: transparent;"><![endif]-->
        
    <!--[if (mso)|(IE)]><td align="center" width="550" style="width: 550px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
    <div class="u-col u-col-100" style="max-width: 320px;min-width: 550px;display: table-cell;vertical-align: top;">
    <div style="width: 100% !important;">
    <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
    
    <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
        <tr>
        <td style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 15px;font-family:arial,helvetica,sans-serif;" align="left">
            
    <div style="color: #888888; line-height: 180%; text-align: center; word-wrap: break-word;">
        <p style="font-size: 14px; line-height: 180%;">Want to change how you receive these emails? You can update your preferences or <span style="text-decoration: underline; font-size: 14px; line-height: 25.2px;"><span style="color: #ff0000; font-size: 14px; line-height: 25.2px; text-decoration: underline;">unsubscribe</span></span> from this list.</p>
    </div>

        </td>
        </tr>
    </tbody>
    </table>

    <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
        <tr>
        <td style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 15px;font-family:arial,helvetica,sans-serif;" align="left">
            
    <div style="color: #888888; line-height: 180%; text-align: center; word-wrap: break-word;">
        <p style="font-size: 14px; line-height: 180%;">&copy; 2020 BharatOff. All Rights Reserved.</p>
    </div>

        </td>
        </tr>
    </tbody>
    </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
    </div>
    <!--[if (mso)|(IE)]></td><![endif]-->
        <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
        </div>
    </div>
    </div>


        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
        </td>
    </tr>
    </tbody>
    </table>
    <!--[if mso]></div><![endif]-->
    <!--[if IE]></div><![endif]-->
    </body>

    </html>

    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

def send_invoice(name, package_amount, gst, total_amount, invoice_number, email):
    sender_email = "Info@bharatoff.com" #"contact@bharatoff.com"
    receiver_email = email
    password = "jtyrjtclwsizuxom" #"@Bharat8602950609"

    message = MIMEMultipart("alternative")
    message["Subject"] = "BharatOff - Invoice Mailer"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = """\
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta name="x-apple-disable-message-reformatting" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <meta name="color-scheme" content="light dark" />
        <meta name="supported-color-schemes" content="light dark" />
        <title></title>
        <style type="text/css" rel="stylesheet" media="all">
        /* Base ------------------------------ */
        
        @import url("https://fonts.googleapis.com/css?family=Nunito+Sans:400,700&display=swap");
        body {
        width: 100% !important;
        height: 100%;
        margin: 0;
        -webkit-text-size-adjust: none;
        }
        
        a {
        color: #3869D4;
        }
        
        a img {
        border: none;
        }
        
        td {
        word-break: break-word;
        }
        
        .preheader {
        display: none !important;
        visibility: hidden;
        mso-hide: all;
        font-size: 1px;
        line-height: 1px;
        max-height: 0;
        max-width: 0;
        opacity: 0;
        overflow: hidden;
        }
        /* Type ------------------------------ */
        
        body,
        td,
        th {
        font-family: "Nunito Sans", Helvetica, Arial, sans-serif;
        }
        
        h1 {
        margin-top: 0;
        color: #333333;
        font-size: 22px;
        font-weight: bold;
        text-align: left;
        }
        
        h2 {
        margin-top: 0;
        color: #333333;
        font-size: 16px;
        font-weight: bold;
        text-align: left;
        }
        
        h3 {
        margin-top: 0;
        color: #333333;
        font-size: 14px;
        font-weight: bold;
        text-align: left;
        }
        
        td,
        th {
        font-size: 16px;
        }
        
        p,
        ul,
        ol,
        blockquote {
        margin: .4em 0 1.1875em;
        font-size: 16px;
        line-height: 1.625;
        }
        
        p.sub {
        font-size: 13px;
        }
        /* Utilities ------------------------------ */
        
        .align-right {
        text-align: right;
        }
        
        .align-left {
        text-align: left;
        }
        
        .align-center {
        text-align: center;
        }
        /* Buttons ------------------------------ */
        
        .button {
        background-color: #3869D4;
        border-top: 10px solid #3869D4;
        border-right: 18px solid #3869D4;
        border-bottom: 10px solid #3869D4;
        border-left: 18px solid #3869D4;
        display: inline-block;
        color: #FFF;
        text-decoration: none;
        border-radius: 3px;
        box-shadow: 0 2px 3px rgba(0, 0, 0, 0.16);
        -webkit-text-size-adjust: none;
        box-sizing: border-box;
        }
        
        .button--green {
        background-color: #ff5a00;
        border-top: 10px solid #ff5a00;
        border-right: 18px solid #ff5a00;
        border-bottom: 10px solid #ff5a00;
        border-left: 18px solid #ff5a00;
        }
        
        .button--red {
        background-color: #FF6136;
        border-top: 10px solid #FF6136;
        border-right: 18px solid #FF6136;
        border-bottom: 10px solid #FF6136;
        border-left: 18px solid #FF6136;
        }
        
        @media only screen and (max-width: 500px) {
        .button {
            width: 100% !important;
            text-align: center !important;
        }
        }
        /* Attribute list ------------------------------ */
        
        .attributes {
        margin: 0 0 21px;
        }
        
        .attributes_content {
        background-color: #F4F4F7;
        padding: 16px;
        }
        
        .attributes_item {
        padding: 0;
        }
        /* Related Items ------------------------------ */
        
        .related {
        width: 100%;
        margin: 0;
        padding: 25px 0 0 0;
        -premailer-width: 100%;
        -premailer-cellpadding: 0;
        -premailer-cellspacing: 0;
        }
        
        .related_item {
        padding: 10px 0;
        color: #CBCCCF;
        font-size: 15px;
        line-height: 18px;
        }
        
        .related_item-title {
        display: block;
        margin: .5em 0 0;
        }
        
        .related_item-thumb {
        display: block;
        padding-bottom: 10px;
        }
        
        .related_heading {
        border-top: 1px solid #CBCCCF;
        text-align: center;
        padding: 25px 0 10px;
        }
        /* Discount Code ------------------------------ */
        
        .discount {
        width: 100%;
        margin: 0;
        padding: 24px;
        -premailer-width: 100%;
        -premailer-cellpadding: 0;
        -premailer-cellspacing: 0;
        background-color: #F4F4F7;
        border: 2px dashed #CBCCCF;
        }
        
        .discount_heading {
        text-align: center;
        }
        
        .discount_body {
        text-align: center;
        font-size: 15px;
        }
        /* Social Icons ------------------------------ */
        
        .social {
        width: auto;
        }
        
        .social td {
        padding: 0;
        width: auto;
        }
        
        .social_icon {
        height: 20px;
        margin: 0 8px 10px 8px;
        padding: 0;
        }
        /* Data table ------------------------------ */
        
        .purchase {
        width: 100%;
        margin: 0;
        padding: 35px 0;
        -premailer-width: 100%;
        -premailer-cellpadding: 0;
        -premailer-cellspacing: 0;
        }
        
        .purchase_content {
        width: 100%;
        margin: 0;
        padding: 25px 0 0 0;
        -premailer-width: 100%;
        -premailer-cellpadding: 0;
        -premailer-cellspacing: 0;
        }
        
        .purchase_item {
        padding: 10px 0;
        color: #51545E;
        font-size: 15px;
        line-height: 18px;
        }
        
        .purchase_heading {
        padding-bottom: 8px;
        border-bottom: 1px solid #EAEAEC;
        }
        
        .purchase_heading p {
        margin: 0;
        color: #85878E;
        font-size: 12px;
        }
        
        .purchase_footer {
        padding-top: 15px;
        border-top: 1px solid #EAEAEC;
        }
        
        .purchase_total {
        margin: 0;
        text-align: right;
        font-weight: bold;
        color: #333333;
        }
        
        .purchase_total--label {
        padding: 0 15px 0 0;
        }
        
        body {
        background-color: #F4F4F7;
        color: #51545E;
        }
        
        p {
        color: #51545E;
        }
        
        p.sub {
        color: #6B6E76;
        }
        
        .email-wrapper {
        width: 100%;
        margin: 0;
        padding: 0;
        -premailer-width: 100%;
        -premailer-cellpadding: 0;
        -premailer-cellspacing: 0;
        background-color: #F4F4F7;
        }
        
        .email-content {
        width: 100%;
        margin: 0;
        padding: 0;
        -premailer-width: 100%;
        -premailer-cellpadding: 0;
        -premailer-cellspacing: 0;
        }
        /* Masthead ----------------------- */
        
        .email-masthead {
        padding: 25px 0;
        text-align: center;
        }
        
        .email-masthead_logo {
        width: 94px;
        }
        
        .email-masthead_name {
        font-size: 16px;
        font-weight: bold;
        color: #A8AAAF;
        text-decoration: none;
        text-shadow: 0 1px 0 white;
        }
        /* Body ------------------------------ */
        
        .email-body {
        width: 100%;
        margin: 0;
        padding: 0;
        -premailer-width: 100%;
        -premailer-cellpadding: 0;
        -premailer-cellspacing: 0;
        background-color: #FFFFFF;
        }
        
        .email-body_inner {
        width: 570px;
        margin: 0 auto;
        padding: 0;
        -premailer-width: 570px;
        -premailer-cellpadding: 0;
        -premailer-cellspacing: 0;
        background-color: #FFFFFF;
        }
        
        .email-footer {
        width: 570px;
        margin: 0 auto;
        padding: 0;
        -premailer-width: 570px;
        -premailer-cellpadding: 0;
        -premailer-cellspacing: 0;
        text-align: center;
        }
        
        .email-footer p {
        color: #6B6E76;
        }
        
        .body-action {
        width: 100%;
        margin: 30px auto;
        padding: 0;
        -premailer-width: 100%;
        -premailer-cellpadding: 0;
        -premailer-cellspacing: 0;
        text-align: center;
        }
        
        .body-sub {
        margin-top: 25px;
        padding-top: 25px;
        border-top: 1px solid #EAEAEC;
        }
        
        .content-cell {
        padding: 35px;
        }
        /*Media Queries ------------------------------ */
        
        @media only screen and (max-width: 600px) {
        .email-body_inner,
        .email-footer {
            width: 100% !important;
        }
        }
        
        @media (prefers-color-scheme: dark) {
        body,
        .email-body,
        .email-body_inner,
        .email-content,
        .email-wrapper,
        .email-masthead,
        .email-footer {
            background-color: #333333 !important;
            color: #FFF !important;
        }
        p,
        ul,
        ol,
        blockquote,
        h1,
        h2,
        h3,
        span,
        .purchase_item {
            color: #FFF !important;
        }
        .attributes_content,
        .discount {
            background-color: #222 !important;
        }
        .email-masthead_name {
            text-shadow: none !important;
        }
        }
        
        :root {
        color-scheme: light dark;
        supported-color-schemes: light dark;
        }
        </style>
    </head>
    <body>
        <table class="email-wrapper" width="100%" cellpadding="0" cellspacing="0" role="presentation">
        <tr>
            <td align="center">
            <table class="email-content" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                <!-- Email Body -->
                <tr>
                <td class="email-body" width="100%" cellpadding="0" cellspacing="0">
                    <table class="email-body_inner" align="center" width="570" cellpadding="0" cellspacing="0" role="presentation">
                    <!-- Body content -->
                    <tr>
                        <td class="content-cell">
                        <div class="f-fallback">
                            <h1>Hi """+name+""",</h1>
                            <p>Thanks for using BharatOff. This is an invoice for your recent purchase.</p>
                            <table class="attributes" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                            <tr>
                                <td class="attributes_content">
                                <table width="100%" cellpadding="0" cellspacing="0" role="presentation">
                                    <tr>
                                    <td class="attributes_item">
                                        <span class="f-fallback">
                <strong>Amount:</strong> """+str(total_amount)+""" INR
                </span>
                                    </td>
                                    </tr>
                                    <tr>
                                    <td class="attributes_item">
                                        <span class="f-fallback">
                <strong>Date:</strong> """+str(date.today())+"""
                </span>
                                    </td>
                                    </tr>
                                    <tr>
                                    <td class="attributes_item">
                                        <span class="f-fallback">
                <strong>Validity:</strong> """+str(date.today()+timedelta(days=372))+""" (1 year + 7 extra days)
                </span>
                                    </td>
                                    </tr>
                                </table>
                                </td>
                            </tr>
                            </table>
                            <!-- Action -->
                            <table class="body-action" align="center" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                            <tr>
                                <td align="center">
                                <!-- Border based button
            https://litmus.com/blog/a-guide-to-bulletproof-buttons-in-email-design -->
                                <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
                                    <tr>
                                    <td align="center">
                                        <a href="http://bharatoff.com/invoice/?invoice-number="""+invoice_number+"""" class="f-fallback button button--green" target="_blank">Download Invoice</a>
                                    </td>
                                    </tr>
                                </table>
                                </td>
                            </tr>
                            </table>
                            <table class="purchase" width="100%" cellpadding="0" cellspacing="0">
                            <tr>
                                <td>
                                <h3>"""+ invoice_number +"""</h3>
                                </td>
                                <td>
                                <h3 class="align-right">"""+ str(date.today()) +"""</h3>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="2">
                                <table class="purchase_content" width="100%" cellpadding="0" cellspacing="0">
                                    <tr>
                                    <th class="purchase_heading" align="left">
                                        <p class="f-fallback">Description</p>
                                    </th>
                                    <th class="purchase_heading" align="right">
                                        <p class="f-fallback">Amount</p>
                                    </th>
                                    </tr>
                                    <tr>
                                    <td width="80%" class="purchase_item"><span class="f-fallback">"""+ str(total_amount) +""" Package</span></td>
                                    <td class="align-right" width="20%" class="purchase_item"><span class="f-fallback">"""+str(package_amount)+"""</span><td>
                                    </tr>
                                    <tr>
                                    <td width="80%" class="purchase_item"><span class="f-fallback">GST (18%)</span></td>
                                    <td class="align-right" width="20%" class="purchase_item"><span class="f-fallback">"""+ str(gst) +"""</span><td>
                                    </tr>
                                    <tr>
                                    <td width="80%" class="purchase_footer" valign="middle">
                                        <p class="f-fallback purchase_total purchase_total--label">Total</p>
                                    </td>
                                    <td width="20%" class="purchase_footer" valign="middle">
                                        <p class="f-fallback purchase_total">"""+ str(total_amount) +"""</p>
                                    </td>
                                    </tr>
                                </table>
                                </td>
                            </tr>
                            </table>
                            <p>If you have any questions about this invoice, simply reply to this email or reach out to our <a href="{{support_url}}">support team</a> for help.</p>
                            <p>Cheers,
                            <br>The BharatOff Team</p>
                            <!-- Sub copy -->
                        </div>
                        </td>
                    </tr>
                    </table>
                </td>
                </tr>
                <tr>
                <td>
                    <table class="email-footer" align="center" width="570" cellpadding="0" cellspacing="0" role="presentation">
                    <tr>
                        <td class="content-cell" align="center">
                        <p class="f-fallback sub align-center">&copy; 2020 BharatOff. All rights reserved.</p>
                        <p class="f-fallback sub align-center">
                        </p>
                        </td>
                    </tr>
                    </table>
                </td>
                </tr>
            </table>
            </td>
        </tr>
        </table>
    </body>
    </html>

    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )



def send_username_password_via_email(username, username_password, email):
    sender_email = "Info@bharatoff.com" #"contact@bharatoff.com"
    receiver_email = email
    password = "jtyrjtclwsizuxom" #"@Bharat8602950609"

    message = MIMEMultipart("alternative")
    message["Subject"] = "BharatOff - Forgot Password Mail"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = """\
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
    <head>
    <!--[if gte mso 9]>
    <xml>
    <o:OfficeDocumentSettings>
        <o:AllowPNG/>
        <o:PixelsPerInch>96</o:PixelsPerInch>
    </o:OfficeDocumentSettings>
    </xml>
    <![endif]-->
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="x-apple-disable-message-reformatting">
    <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->
    <title></title>
    
        <style type="text/css">
        table, td { color: #000000; } a { color: #0000ee; text-decoration: underline; }
    @media only screen and (min-width: 620px) {
    .u-row {
        width: 600px !important;
    }
    .u-row .u-col {
        vertical-align: top;
    }

    .u-row .u-col-100 {
        width: 600px !important;
    }

    }

    @media (max-width: 620px) {
    .u-row-container {
        max-width: 100% !important;
        padding-left: 0px !important;
        padding-right: 0px !important;
    }
    .u-row .u-col {
        min-width: 320px !important;
        max-width: 100% !important;
        display: block !important;
    }
    .u-row {
        width: calc(100% - 40px) !important;
    }
    .u-col {
        width: 100% !important;
    }
    .u-col > div {
        margin: 0 auto;
    }
    }
    body {
    margin: 0;
    padding: 0;
    }

    table,
    tr,
    td {
    vertical-align: top;
    border-collapse: collapse;
    }

    p {
    margin: 0;
    }

    .ie-container table,
    .mso-container table {
    table-layout: fixed;
    }

    * {
    line-height: inherit;
    }

    a[x-apple-data-detectors='true'] {
    color: inherit !important;
    text-decoration: none !important;
    }

    </style>
    
    

    <!--[if !mso]><!--><link href="https://fonts.googleapis.com/css?family=Montserrat:400,700&display=swap" rel="stylesheet" type="text/css"><!--<![endif]-->

    </head>

    <body class="clean-body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #f0f0f0;color: #000000">
    <!--[if IE]><div class="ie-container"><![endif]-->
    <!--[if mso]><div class="mso-container"><![endif]-->
    <table style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #f0f0f0;width:100%" cellpadding="0" cellspacing="0">
    <tbody>
    <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #f0f0f0;"><![endif]-->
        

    <div class="u-row-container" style="padding: 0px;background-color: rgba(255,255,255,0)">
    <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: rgba(255,255,255,0);" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #ffffff;"><![endif]-->
        
    <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
    <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
    <div style="width: 100% !important;">
    <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
    
    <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
        <tr>
        <td style="overflow-wrap:break-word;word-break:break-word;padding:30px 30px 15px;font-family:'Montserrat',sans-serif;" align="left">
            
    <div style="line-height: 150%; text-align: left; word-wrap: break-word;">
        <p style="line-height: 150%; font-size: 14px;"><span style="font-size: 16px; line-height: 24px; color: #282828;">Hi """+username+""", seems like you have requested us for a forgot password problem. Please find your details below to login.</span></p>
    </div>

        </td>
        </tr>
    </tbody>
    </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
    </div>
    <!--[if (mso)|(IE)]></td><![endif]-->
        <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
        </div>
    </div>
    </div>



    <div class="u-row-container" style="padding: 0px 10px;background-color: rgba(255,255,255,0)">
    <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px 10px;background-color: rgba(255,255,255,0);" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #ffffff;"><![endif]-->
        
    <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
    <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
    <div style="width: 100% !important;">
    <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
    
    <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
        <tr>
        <td style="overflow-wrap:break-word;word-break:break-word;padding:5px 30px;font-family:'Montserrat',sans-serif;" align="left">
            
    <div style="line-height: 140%; text-align: left; word-wrap: break-word;">
        <ul style="list-style-type: circle;">
    <li style="font-size: 14px; line-height: 19.6px;"><span style="color: #292929; font-size: 16px; line-height: 22.4px;">Username: """+username+"""</span></li>
    </ul>
    </div>

        </td>
        </tr>
    </tbody>
    </table>

    <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
        <tr>
        <td style="overflow-wrap:break-word;word-break:break-word;padding:5px 30px;font-family:'Montserrat',sans-serif;" align="left">
            
    <div style="line-height: 140%; text-align: left; word-wrap: break-word;">
        <ul style="list-style-type: circle;">
    <li style="font-size: 14px; line-height: 19.6px;"><span style="font-size: 16px; line-height: 22.4px;">Password: """+username_password+"""</span></li>
    </ul>
    </div>

        </td>
        </tr>
    </tbody>
    </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
    </div>
    <!--[if (mso)|(IE)]></td><![endif]-->
        <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
        </div>
    </div>
    </div>



    <div class="u-row-container" style="padding: 0px;background-color: rgba(255,255,255,0)">
    <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: rgba(255,255,255,0);" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #ffffff;"><![endif]-->
        
    <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
    <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
    <div style="width: 100% !important;">
    <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
    
    <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
        <tr>
        <td style="overflow-wrap:break-word;word-break:break-word;padding:10px 30px 20px;font-family:'Montserrat',sans-serif;" align="left">
            
    <div style="color: #292929; line-height: 160%; text-align: left; word-wrap: break-word;">
        <p style="font-size: 14px; line-height: 160%;">Please keep these credentials with you, do not share it with anyone, Also do not write it down somewhere.</p>
    <p style="font-size: 14px; line-height: 160%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 160%;">NOTE - It's always safe to delete such mails from your inbox for better security.</p>
    </div>

        </td>
        </tr>
    </tbody>
    </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
    </div>
    <!--[if (mso)|(IE)]></td><![endif]-->
        <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
        </div>
    </div>
    </div>



    <div class="u-row-container" style="padding: 0px;background-color: rgba(255,255,255,0)">
    <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: rgba(255,255,255,0);" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #ffffff;"><![endif]-->
        
    <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
    <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
    <div style="width: 100% !important;">
    <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
    
    <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
        <tr>
        <td style="overflow-wrap:break-word;word-break:break-word;padding:20px 20px 50px;font-family:'Montserrat',sans-serif;" align="left">
            
    <div align="center">
    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;font-family:'Montserrat',sans-serif;"><tr><td style="font-family:'Montserrat',sans-serif;" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="" style="height:65px; v-text-anchor:middle; width:226px;" arcsize="49%" stroke="f" fillcolor="#ff5500"><w:anchorlock/><center style="color:#FFF;font-family:'Montserrat',sans-serif;"><![endif]-->
        <a href="https://www.bharatoff.com/login/" target="_blank" style="box-sizing: border-box;display: inline-block;font-family:'Montserrat',sans-serif;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFF; background-color: #ff5500; border-radius: 32px; -webkit-border-radius: 32px; -moz-border-radius: 32px; width:auto; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;">
        <span style="display:block;padding:10px 30px;line-height:150%;"><span style="font-size: 30px; line-height: 45px;">Login Here</span></span>
        </a>
    <!--[if mso]></center></v:roundrect></td></tr></table><![endif]-->
    </div>

        </td>
        </tr>
    </tbody>
    </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
    </div>
    <!--[if (mso)|(IE)]></td><![endif]-->
        <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
        </div>
    </div>
    </div>



    <div class="u-row-container" style="padding: 30px;background-color: rgba(240,240,240,0)">
    <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 30px;background-color: rgba(240,240,240,0);" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: transparent;"><![endif]-->
        
    <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
    <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
    <div style="width: 100% !important;">
    <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
    
    <table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
        <tr>
        <td style="overflow-wrap:break-word;word-break:break-word;padding:20px;font-family:'Montserrat',sans-serif;" align="left">

        </td>
        </tr>
    </tbody>
    </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
    </div>
    <!--[if (mso)|(IE)]></td><![endif]-->
        <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
        </div>
    </div>
    </div>


        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
        </td>
    </tr>
    </tbody>
    </table>
    <!--[if mso]></div><![endif]-->
    <!--[if IE]></div><![endif]-->
    </body>

    </html>


    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

if __name__ == '__main__':
    # send_invoice_and_credentials("roshan", "Linuz@123", "ABC Shop", "jd7june1999@gmail.com")
    # send_credentials("Roshan Pandey","roshan", "Linux@123", "pandeyroshan556@gmail.com")
    # send_invoice("Roshan Pandey", 199, 1, 200, "IN20210713003", "pandeyroshan556@gmail.com")
    send_username_password("pandeyroshan","1ED;2?^f+4","pandeyroshan556@gmail.com")