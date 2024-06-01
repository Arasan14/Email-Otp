from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import userserializer, VerifyAccountSerialzer
from .emails import send_otp_via_email
from .models import user

class RegisterEmail(APIView):
    def post(self, request):
        try:
            query = request.data
            serializer = userserializer(data=query)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status': status.HTTP_200_OK,
                    'message': 'User registered successfully.',
                    'data': serializer.data,
                })
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Validation Error.',
                'errors': serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Internal Server Error.'
            })

class VerifyOtp(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyAccountSerialzer(data=data)
            if serializer.is_valid():
                otp = serializer.data['otp']

                # Assuming you have a User model with an otp field
                user_instance = user.objects.get(email=serializer.data['email'])
                if user_instance.otp != otp:
                    return Response({
                        'status': status.HTTP_400_BAD_REQUEST,
                        'message': 'Invalid OTP.',
                    })
                
                user_instance.is_verified = True  # Corrected line
                user_instance.save()  # Save the changes

                return Response({
                    'status': status.HTTP_200_OK,
                    'message': 'Verification successful.',
                })
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Validation Error.',
                'errors': serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Internal Server Error.'
            })
