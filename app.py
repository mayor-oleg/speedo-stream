# -*- coding: utf-8 -*-
#"""
#Created on Sat Apr  3 21:04:11 2021

#@author: jr
#"""

from flask import Flask, Response,render_template
import boto3

app = Flask(__name__)
#server = app.server

# Let's use Amazon S3
s3 = boto3.resource('s3')
# Print out bucket names
for bucket in s3.buckets.all():
    print ('========bucket===========')
    print (bucket.name)
    print ('++++++++bucket+++++++++++')
#conn = boto3.connect_s3()
#print ('================conn================')
#print (conn)


def sound():
    sampleRate = fs = 44100  # Частота дискретизации
    seconds = 3 # Продолжительность записи
        
    bitsPerSample = 16
    channels = 2
    
        
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    
    sd.wait()  # Дождитесь окончания записи
    #write('output.wav', fs, myrecording)  # Сохранить как WAV файл
    s3.Bucket('speedo-raw-store').put_object(Key='output.wav', Body=myrecording)

             
@app.route('/audio')
def audio():
    # start Recording
    sound()
    return 'recorded'

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
