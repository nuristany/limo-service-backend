from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from. serializers import ContactSerializer
from django.template.loader import render_to_string
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.conf import settings
from. models import Contact

# Create your views here.



class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    #permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        contact_data = serializer.validated_data
        #print("ConatctData:", contact_data)

        #sending data to mail owner

        subject = "Thank you for Using Our Services"
        html_message = render_to_string('contact_email.html', {'contact_data': contact_data})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to_email = serializer.data['email']
        send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

        # Send notification email to the owner
        subject = 'Customer Message'
        html_message = render_to_string('contact_notification_email.html', {'contact_data': contact_data})
        plain_message = strip_tags(html_message)
        to_email = 'zhakyanuristany@gmail.com'  # Update with your email
        send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)



      
    

    


