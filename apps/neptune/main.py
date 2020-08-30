import neptune

# The init() function called this way assumes that
# NEPTUNE_API_TOKEN environment variable is defined.

neptune.init('ferdzso05/sandbox')
#neptune.create_experiment(name='minimal_example')

# Define parameters

PARAMS = {'decay_factor' : 0.5,
          'n_iterations' : 117}

# Create experiment with defined parameters + upload source files

neptune.create_experiment (name='example_with_parameters',
                          params=PARAMS, upload_source_files=['main.py'])

neptune.append_tags('first-steps', 'neptune-tutorial')

# log some metrics

for i in range(100):
    neptune.log_metric('loss', 0.95**i)

neptune.log_metric('AUC', 0.96)

# Log image data

import numpy as np

array = np.random.rand(10, 10, 3)*255
array = np.repeat(array, 30, 0)
array = np.repeat(array, 30, 1)
neptune.log_image('mosaics', array)

# Log text data

neptune.log_text('top questions', 'what is machine learning?')
