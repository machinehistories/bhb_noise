import array
import math
import audiocore
import winterbloom_bhb
import random
import time
bhb = winterbloom_bhb.BigHonkingButton()

pressing = 0
button_sample = bhb.load_sample("samples/kick.wav")
long_press = False
short_press = False

# This generates a raw set of samples that represents one full
# cycle of a sine wave. If you wanted different waveforms, you
# could change the formula here to generate that instead.
def generate_sine_wave(volume=1.0):
    volume = volume * (2 ** 15 - 1)  # Increase this to increase the volume of the tone.
    length = 100
    sine_samples = array.array("H", [0] * length)

    for i in range(length):
        sine_samples[i] = int((1 + math.sin(math.pi * 2 * i / length)) * volume)

    return sine_samples

sine_wave = generate_sine_wave(0.8)
sine_sample = audiocore.RawSample(sine_wave)

# Change this to play different notes. You can also
# check the CV input using `bhb.pitch_in` and re-adjust
# the sample rate.
frequency = 440
sine_sample.sample_rate = frequency * len(sine_wave)

def generate_noise(volume=1.0):
    volume = volume * (2 ** 15 - 1)  # Increase this to increase the volume of the tone.
    length = 800
    noise_samples = array.array("H", [0] * length)

    for i in range(length):
        noise_samples[i] = int(random.random() * volume)

    return noise_samples

noise = generate_noise(0.8)
noise_sample = audiocore.RawSample(noise)
# Change this to set the noise sample's frequency.
# This generate works well as pretty low numbers,
# but you can get some interesting effects at higher
# values.
frequency = 2
noise_sample.sample_rate = frequency * len(noise)
sample = bhb.load_sample("samples/reverse.wav")
burst_intervals = [0.05, 0.2, 0.03, 0.05, 0.1]


while True:
    
    if bhb.gate_in is True:
        random_val = random.random()
        bhb.gate_out = True
        bhb.play(noise_sample, pitch_cv=bhb.pitch_in * math.sin(random_val), loop=True)

    if bhb.gate_in is False:
        bhb.gate_out = False
        random_val = random.random()
        noise = generate_noise(random_val)
        noise_sample.sample_rate = frequency * len(noise)
        random_sine = random.uniform(0,10.0)
        bhb.play(sine_sample , pitch_cv=bhb.pitch_in* int(math.sin(random_val) * random_sine), loop=True)
        if bhb.pitch_in > 3:
            bhb.gate_out = True
            
    if bhb.button is True:
        pressing +=1
        bhb.play(sine_sample, pitch_cv=bhb.pitch_in)
        bhb.gate_out = True
        print(pressing)
    if bhb.button is False:
        bhb.gate_out = False
        if pressing > 10:
            long_press = True
            short_press = False
        elif pressing < 9 and pressing > 0:
            short_press = True
            long_press = False
        if long_press is True:
            for intervals in burst_intervals:
                bhb.gate_out = True
                bhb.play(sample, pitch_cv=bhb.pitch_in)
                time.sleep(intervals)
                bhb.gate_out = False
                bhb.stop()
                time.sleep(intervals)
                long_press = False
                if pressing > 15:
                    pressing = 0
        if short_press is True:
            bhb.play(button_sample, pitch_cv=bhb.pitch_in)
            pressing = 0
        
    long_press = False
    short_press = False

        
