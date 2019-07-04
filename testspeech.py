from pocketsphinx import LiveSpeech
import os

lp = LiveSpeech(audio_device = '0', sampling_rate = 16000 ,lm=False,
                kws = os.path.join(os.path.dirname(os.path.abspath(__file__)), './data/keyphrase.list' ))

def tryout():
    print("something happens")
    count = 0
    while True:

        for phrase in lp:

            print(phrase)
            p = phrase.segment()[0]
            print(phrase.segment(detailed = True)
            
            if count == 0 :
                print("bye baby")
                break
            
    

tryout()
