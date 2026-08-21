"""
Training
We need to coordinate the learning loop over multiple rounds. It pulls data from dataset.py, pushes it
through model.py -> get predictions, and checks how wrong the guesses are (calculating loss). It saves the 
best performing version of the model.

File returns:
A saved model file and logs.txt of training/validation loss per epoch
"""
