from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from  rest_framework import status
from rest_framework.response import Response
from .models import Customer
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string, get_template
import os


class SendMassMail(APIView):
    def post(self, request):
        to = request.data.get("to")
        if to == 'all':
            customers = Customer.objects.all()
            for customer in customers:
                emails = (customer.email)
                subject_file = os.path.join(settings.BASE_DIR, "mail/message/subject.txt")
                subject = render_to_string(subject_file, {'name': customer.name})
                from_email = settings.DEFAULT_MAIL_SENDER
                to_email = [emails,]

                password_message_file = os.path.join(settings.BASE_DIR, "mail/message/body.txt")
                password_message = render_to_string(password_message_file, {
                                                            'name': customer.name,
                                                        })

                message = EmailMultiAlternatives(subject=subject, body=password_message, from_email=from_email, to=to_email)

                html_template = os.path.join(settings.BASE_DIR, "mail/message/body.html")
                template = render_to_string(html_template, {
                                                            'name': customer.name,
                                                            })

                message.attach_alternative(template, "text/html")

                send = message.send()
                if send:
                    response = "Sent"
                else:
                    response = "Not Sent"
        elif to == 'single':
            email = request.data.get("email")
            check_mail = Customer.objects.filter(email=email).exists()
            if check_mail == False:
                return Response({"message": "Email does not exists."}, status=status.HTTP_400_BAD_REQUEST)
            customer = Customer.objects.get(email=email)
            subject_file = os.path.join(settings.BASE_DIR, "mail/message/subject.txt")
            subject = render_to_string(subject_file, {'name': customer.name})
            from_email = settings.DEFAULT_MAIL_SENDER
            to_email = [customer.email,]

            password_message_file = os.path.join(settings.BASE_DIR, "mail/message/body.txt")
            password_message = render_to_string(password_message_file, {
                                                        'name': customer.name,
                                                    })

            message = EmailMultiAlternatives(subject=subject, body=password_message, from_email=from_email, to=to_email)

            html_template = os.path.join(settings.BASE_DIR, "mail/message/body.html")
            template = render_to_string(html_template, {
                                                        'name': customer.name,
                                                        })

            message.attach_alternative(template, "text/html")

            send = message.send()
            if send:
                response = "Sent"
            else:
                response = "Not Sent"
        return Response({"message":response})
