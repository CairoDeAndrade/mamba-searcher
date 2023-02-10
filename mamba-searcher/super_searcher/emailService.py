# Django imports
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import os
# email imports
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import shutil


@login_required(redirect_field_name='login')
def email_response(request):
    dirPath = r"media/filtered_files"
    lista_arquivo = next(os.walk(dirPath))[2]

    for i in lista_arquivo:
        shutil.move(f'media/filtered_files/{i}',
                    f'media/filtered_files/{i}'.replace("á", "a").replace("é", "e").replace("ê", "e").replace("í",
                                                                                                              "i")
                    .replace("ó", "o")
                    .replace("ú", "u").replace("ü", "u").replace("ã", "a").replace("ç", "c").replace(" ", "_")
                    .replace(",", "").replace("õ", "o").replace("Á", "A").replace("É", "E").replace("Ê", "E").replace(
                        "Í", "I").replace("Ó", "O")
                    .replace("Ú", "U").replace("Ü", "U").replace("Ã", "A").replace("Ç", "C").replace(" ", "_")
                    .replace(",", "").replace("Õ", "O"))

    # Sending email
    dirPath = r"media/filtered_files"
    list_arq = next(os.walk(dirPath))[2]
    fromaddr = "mamba.entra21@gmail.com"  # Alternative email: mamba.python.entra21@gmail.com
    toaddr = str(request.GET.get('term').replace('%40', '@'))

    try:
        validate_email(toaddr)
    except ValidationError as e:
        messages.error(request, 'Email inválido!')
        return redirect('email_input')
    else:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Emails Filtrados"
        body = "Aqui estão seus emails filtrados"
        msg.attach(MIMEText(body, 'plain'))

        for i in list_arq:
            filename = i
            attachment = open(f"media/filtered_files/{i}", "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload(attachment.read())
            encoders.encode_base64(p)

            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "utjwzdlbrpvwgovh")
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()

        messages.add_message(request, messages.SUCCESS, 'Os arquivos filtrados foram enviados com sucesso!')

    return render(request, 'super_searcher/email_response.html')


@login_required(redirect_field_name='login')
def email_input(request):
    return render(request, 'super_searcher/email_input.html')
