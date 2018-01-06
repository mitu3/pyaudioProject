import wave
from pyaudio import PyAudio,paInt16


framerate = 8000
NUM_SAMPLES = 2000
channels = 2
sampwidth = 2
TIME = 1

def save_wave_file(filename,data):
    '''save the data to the wan file'''
    wf = wave.open(filename,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b''.join(data))
    wf.close()

def my_record(filename):
    pa = PyAudio()
    stream = pa.open(format = paInt16, channels = 2,
                     rate = framerate, input = True,
                     frames_per_buffer = NUM_SAMPLES)
    my_buf = []
    count = 0
    while count < TIME * 10:
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count += 1
        print('..')
    save_wave_file(filename,my_buf)
    stream.stop_stream()
    stream.close()




