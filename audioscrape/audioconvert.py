# coding=utf-8
'''Convert audio clips to user defined format via ffmpeg'''
import subprocess


def ffmpeg_convert(file, audio_title, fileformat):
    command = ['ffmpeg', '-hide_banner',  # quiet ffmpeg banner
               '-loglevel', 'panic',   # quiet ffmpeg stdout
               '-i', "./{}".format(file),  # input file to convert
               '-f', '{}'.format(fileformat),  # output fileformat type
               '-ac', '1',  # mono channel
               '-ar', '16000',  # sampling rate 16000Hz
               '-vn',  # only want audio, no video
               "./{0}/{1}.{0}".format(fileformat,
                                      audio_title.replace(" ", "_"))]
    subprocess.call(command)
    return None
