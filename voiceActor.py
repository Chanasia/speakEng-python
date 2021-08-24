import requests
from io import BytesIO
from pydub.audio_segment import AudioSegment
from pydub.playback import play

def inpIdOutVoiceActor(id): #return voiceAtor string 0 - 8
    voiceActor = ['Ivy', 'Joanna', 'Kimberly', 'Salli', 'Matthew', 'Justin', 'Kendra', 'Joey']
    return voiceActor[id]

def responseUrlVoice(msg, voiceActor): #return json
    url = 'https://ttsmp3.com/makemp3_new.php'
    med = {
        'Content-type': 'application/x-www-form-urlencoded',
        'lang': voiceActor,
        'msg': msg.replace('&', 'and'),
        'source': 'ttsmp3'
    }
    return requests.post(url, med).json()

def playSoundUrl(url): #play sound music
    response = requests.get(url).content
    soundArr = BytesIO(response)
    sound = AudioSegment.from_file(soundArr, format='mp3')
    play(sound)