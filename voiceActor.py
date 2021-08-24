import requests
from io import BytesIO
from pydub.audio_segment import AudioSegment
from pydub.playback import play

def inpIdOutVoiceActor(id): #return voiceAtor string 0 - 7
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

def playSoundUrl(url): #play sound
    response = requests.get(url).content
    soundArr = BytesIO(response)
    sound = AudioSegment.from_file(soundArr, format='mp3')
    play(sound)

#main programs
msg = input('Enter message: ')
voiceId = int(input('Enter id voice actor: '))
json_data = responseUrlVoice(msg, inpIdOutVoiceActor(voiceId))
if json_data['URL'] != '':
    playSoundUrl(json_data['URL'])
else:
    print('No url')
