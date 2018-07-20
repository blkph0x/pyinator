from __future__ import print_function

import numpy as np
import tflearn

# Download the Titanic dataset
#from tflearn.datasets import titanic
#titanic.download_dataset('CRYPTO.csv')

# Load CSV file, indicate that the first column represents labels
from tflearn.data_utils import load_csv
data, labels = load_csv('crypto.csv',
                        categorical_labels=False)
labels = np.reshape(labels, (-1, 1))

# Preprocessing function
def preprocess(data, columns_to_ignore):
    # Sort by descending id and delete columns
    for id in sorted(columns_to_ignore, reverse=True):
        [r.pop(id) for r in data]
    for i in range(len(data)):
      # Converting 'sex' field to float (id is 1 after removing labels column)
      data[i][6] = 1 
    return np.array(data, dtype=np.float32)

# Ignore 'name' and 'ticket' columns (id 1 & 6 of data array)

to_ignore=[6]

# Preprocess data
data = preprocess(data, to_ignore)

# Build neural network
net = tflearn.input_data(shape=[None , 7])
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 1, activation='softmax')
net = tflearn.regression(net)

# Define model
model = tflearn.DNN(net)
#labels = np.reshape(labels, (1, -1))
# Start training (apply gradient descent algorithm)
model.fit(data, labels, n_epoch=10, batch_size=6, show_metric=True)
labels = np.reshape(labels, (1, 1, -1))
# Let's create some data for DiCaprio and Winslet
dicaprio = [17,7,2018,23,2,11,1,5,1.0028036335090211657]
# Preprocess data
dicaprio = preprocess([dicaprio], to_ignore)
# Predict surviving chances (class 1 results)
pred = model.predict([dicaprio])
print("chance of Rate incress:", pred[0][1])

