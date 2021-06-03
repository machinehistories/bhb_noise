# bhb_noise
for https://github.com/wntrblm/Big_Honking_Button module using circuit python https://github.com/adafruit/circuitpython.
this seperates the button and gate inputs to provide 6 ways to generate noise and gates
It offers 6 noise makers and gate generators for big honkin button module
Just feed in some melodic cv's and away you go
1. with no gate plugged in it makes a random sinewave that responds to cv and outputs a gate based on a threshold
2. with a gate signal plugged in it generate random noise voltages responding to cv input and outputs the incoming gate
3. with no cv plugged in but with a gate it makes a hybrid sine and noise but it works best at bpm's under 60
4. with no cv and no gate plugged in it outputs some nice sine tones
5. with button short pressed it plays a sample modified by cv input and outputs a gate (it sounds different with and without a gate plugged in since that toggles the sine and noise)
6. with button long pressed it acts a burst generator and plays a sample according to an array of intervals and outputs those gates

