import subprocess

filename = "prueba.mp3"
newfilename = "prueba.wav"
command = ['sox', filename, '-c', '1', newfilename] 
subprocess.Popen(command)