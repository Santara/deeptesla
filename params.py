#!/usr/bin/env python 
from __future__ import division

import os
from collections import OrderedDict

batch_size = 100
save_dir = os.path.abspath('models')
training_steps = 20000
img_height = 66
img_width = 200
img_channels = 3
data_dir = '/home/lex/Dropbox/projects/mit/code/deepcars/steering/epochs'
out_dir = '/home/lex/Dropbox/projects/mit/code/deepcars/steering/output'
shuffle_training = True

epochs = OrderedDict()
# epochs['train'] = range(1, 11)
# epochs['val'] = range(1, 11)
epochs['train'] = [3, 4, 5, 6, 8]
epochs['val'] = [1, 2, 7, 9, 10]

