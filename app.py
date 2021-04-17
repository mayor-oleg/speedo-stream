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
conn = boto3.connect_s3()
print ('================conn================')
print (conn)


@app.route('/audio')
def audio():
    # start Recording
    def sound():

        sampleRate = fs = 44100  # Частота дискретизации
        seconds = 3  # Продолжительность записи

        bitsPerSample = 16
        channels = 2
        wav_header = genHeader(sampleRate, bitsPerSample, channels)

        stream = myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Дождитесь окончания записи
        #write('output.wav', fs, myrecording)  # Сохранить как WAV файл
        print("recording...")
        #frames = []
        first_run = True
        while True:
           if first_run:
               data = wav_header + stream
               first_run = False
           else:
               data = stream
           yield(data)

    return Response(sound())





@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run()

