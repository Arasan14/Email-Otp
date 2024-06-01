from django.core.mail import send_mail
import random
from django.conf import settings
from . models  import  user
from django.core.exceptions import ObjectDoesNotExist


def send_otp_via_email(email):

    subject = 'Your account verification email'
    otp = random.randint(1000, 9999)
    message = f'Your OTP is: {otp}'
    email_from = settings.EMAIL_HOST_USER 
    try:
        
        user_obj = user.objects.get(email=email)
        user_obj.otp = otp
        user_obj.save()
        send_mail(subject, message, email_from, [email])
        return otp
    except ObjectDoesNotExist:
        return None  
    except Exception as e:
        print("An error occurred while sending OTP:", str(e))
        return None 




    # subject = 'Your account verification email'
    # otp = random.randint(1000, 9999)
    # message = f'Your OTP is: {otp}'
    # email_from = settings.EMAIL_HOST
    # send_mail(subject, message, email_from, [email])
    # user_o = user.objects.get(email = email)
    # user_o.otp = otp
    # user_o.save()
    
