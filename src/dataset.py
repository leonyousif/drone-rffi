"""
Dataset and Signal Preprocessing
We need to take in the raw signal data from data/ -> slice the radio recordings into uniform segments
have to adjust the volume of each recorded wave (normalize) to the same level, this is neccesary for
the audio input to the neural network as the model would learn to classify based on the loudness of the
wave rather than the signal itself. Also need use dyynamic noise augmentation and carrier frequency offsets
so that the model is reliable and robust. 

Files returns:
Batched of (spectrograms, labels) pairs for PyTorch dataloader

"""