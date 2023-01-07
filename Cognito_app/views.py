from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from pycognito import Cognito
import traceback
from  pycognito.exceptions import ForceChangePasswordException
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from .forms import CognitoAuthForm
import boto3
import hmac, hashlib, base64




def user_login(request):
    context = {}
    try:
        if request.method == 'GET':
            context['form'] = CognitoAuthForm()
        else:
            try:
                #initiate session
                if settings.AWS_ACCESS_KEY != '' and settings.AWS_SECRET_KEY != '':
                    session = boto3.Session(region_name='us-east-1',aws_access_key_id=settings.AWS_ACCESS_KEY,aws_secret_access_key=settings.AWS_SECRET_KEY)
                else:
                    session = boto3.Session(region_name='us-east-1')
                
                
                s3 = session.resource('s3')

                s3_bucket = str(settings.S3_BUCKET_NAME)

        
            except Exception as e:
                raise e
                    

                        
        return render(request,'login.html',context)
    except Exception as e:
        print(e)
        return redirect('forbidden/')


def user_registration(request):
    context = {}
    try:
        if request.method == 'GET':
            pass
        else:
            try:
                total_info = request.body

                total_info = total_info.split(b",")
                image_data = total_info[0] + total_info[1]
                user_name = total_info[2].decode()
                
                    


                
                #initiate session
                if settings.AWS_ACCESS_KEY != '' and settings.AWS_SECRET_KEY != '':
                    session = boto3.Session(region_name='us-east-1',aws_access_key_id=settings.AWS_ACCESS_KEY,aws_secret_access_key=settings.AWS_SECRET_KEY)
                else:
                    session = boto3.Session(region_name='us-east-1')
                
                
                s3 = session.resource('s3')

                s3_bucket = str(settings.S3_BUCKET_NAME)

                s3.Object(s3_bucket,f'{user_name}.jpg').put(Body=image_data)

                return redirect('/')
        
            except Exception as e:
                raise e
                    

                        
        return render(request,'registration.html',context)
    except Exception as e:
        print(e)
        return redirect('forbidden/')



