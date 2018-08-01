# coding=utf-8
'''Convert audio clips to user defined format via ffmpeg'''
import subprocess


def ffmpeg_convert(file, audio_title, fileformat,
                   channel=1, sampling_rate=16000):
    '''
    Convert audio file to designated file type
    defaults using 16kHz, mono channel wav commonly used in
    training automatic speech recognition models
    '''
    command = ['ffmpeg', '-hide_banner',  # quiet ffmpeg banner
               '-loglevel', 'panic',   # quiet ffmpeg stdout
               '-i', "./{}".format(file),  # input file to convert
               '-f', '{}'.format(fileformat),  # output fileformat type
               '-ac', '{}'.format(channel),  # mono channel default
               '-ar', '{}'.format(sampling_rate),  # sampling rate 16000Hz default
               '-vn',  # only want audio, no video
               "./{0}/{1}.{0}".format(fileformat,
                                      audio_title.replace(" ", "_"))]
    subprocess.call(command)
    return None
