import librosa
import matplotlib.pyplot as plt 
import librosa.display 
import sklearn
import os
import numpy as np
import random
import sys

#set the time parrmeter
time_len = 4000
compress_unit = 50

def get_sound_feature(filename):
    
    #過零率:zero_crossing
    x, sr = librosa.load(filename) 
    n0 = 9000
    n1 = 9100
    zero_crossings = librosa.zero_crossings(x[0:len(x)-1], pad=False) 

    #光譜質心:spectral_centroids
    spectral_centroids = librosa.feature.spectral_centroid(x, sr=sr)[0]
    spectral_centroids.shape
    def normalize(x, axis=0): 
        return sklearn.preprocessing.minmax_scale(x, axis=axis) 
    normalize_spectral_centroids = normalize(spectral_centroids)

    #光譜衰減:spectral_rolloff
    spectral_rolloff = librosa.feature.spectral_rolloff(x+0.01, sr=sr)[0] 

    #梅爾頻率倒譜系數:mfccs.mean/ mfccs.var
    x, fs = librosa.load(filename) 
    mfccs = librosa.feature.mfcc(x, sr=fs) 
    mfccs.shape
    mfccs = sklearn.preprocessing.scale(mfccs, axis=1) 
    #print(mfccs.mean(axis=1)) 
    #print(mfccs.var(axis=1)) 

    #色度頻率:chromagram
    x, sr = librosa.load(filename) 
    chromagram = librosa.feature.chroma_stft(x, sr=sr) 
    
    return sum(zero_crossings), spectral_centroids, spectral_rolloff, mfccs, chromagram, x

def compress(item, time_len, compress_unit):
    
    item = item.tolist()
    
    cut_time = time_len / compress_unit #12
    item_line = int( len(item) / compress_unit ) #14
    remaining = len(item) - item_line * compress_unit
    
    #first time random delete
    for i in range(remaining):
        item.pop(random.randint(0,len(item)))
        
    #second time random delete
    for i in range(cut_time):
        for j in range(item_len - item_line):
            item.pop(random.randint(i*item_line,(i+1)*time_line-j-1))
    
    return item


def excute(time_len, compress_unit)
    

    files= os.listdir() 

    fp_zero_crossing = open("zero_crossing.txt", "w")
    fp_spectral_centroids = open("spectral_centroids.txt", "w")
    fp_spectral_rolloff = open("spectral_rolloff.txt", "w")
    fp_mfccs = open("mfccs.txt", "w")
    fp_chromagram = open("chromagram.txt", "w")
    fp_label = open("label.txt", "w")

    np.set_printoptions(threshold=np.inf)

    for file in files:

        if '.wav' in file:

            zero_crossings, spectral_centroids, spectral_rolloff, mfccs, chromagram , x = get_sound_feature(file)

            if len(spectral_centroids) > time_len:

                #write in zero_crossings_rate
                zero_crossings_rate = round(zero_crossings/len(x)*100)
                fp_zero_crossing.write(str(zero_crossings_rate)+ ' ')

                #write in mfccs
                fp_mfccs.write('[')
                for item in mfccs:
                    if len(item) > time_len:
                        fp_mfccs.write(str(compress(item, time_len, compress_unit)))
                fp_mfccs.write(']')

                #write in chromagram
                fp_chromagram.write('[')
                for item in chromagram:
                    if len(item) > time_len:
                        fp_chromagram.write(str(compress(item, time_len, compress_unit)))
                fp_chromagram.write(']')

                #write in spectral_centroids
                for item in spectral_centroids:
                    if len(item) > time_len:
                        fp_spectral_centroids.write(str(compress(item, time_len, compress_unit)))

                #write in spectral_rolloff
                for item in spectral_rolloff:
                    if len(item) > time_len:
                        fp_spectral_rolloff.write(str(compress(item, time_len, compress_unit)))

                if 'sad' in file:
                    fp_label.write('1 ')

                else if 'happy' in file:
                    fp_label.write('2 ')

                else if 'angry' in file:
                    fp_label.write('3 ')

                else:
                    print('filename error!')
                    sys.exit()


    fp_zero_crossing.close()
    fp_spectral_centroids.close()
    fp_spectral_rolloff.close()
    fp_mfccs.close()
    fp_chromagram.close()
    fp_label.close()
    
    

excute(time_len, compress_unit)
