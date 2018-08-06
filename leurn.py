from __future__ import print_function

import numpy as np
import tflearn

# Download the Titanic dataset
#from tflearn.datasets import titanic
#titanic.download_dataset('CRYPTO.csv')

# Load CSV file, indicate that the first column represents labels
from tflearn.data_utils import load_csv
data, labels = load_csv('crypto.csv', target_column=10,
                        categorical_labels=True, n_classes=3)
#labels = np.reshape(labels, (-1, 1))

# Preprocessing function
def preprocess(data, columns_to_ignore):
    # Sort by descending id and delete columns
    for id in sorted(columns_to_ignore, reverse=True):
        [r.pop(id) for r in data]
    #for i in range(len(data)):
      # Converting 'sex' field to float (id is 1 after removing labels column)
       
    return np.array(data, dtype=np.float32)

# Ignore 'name' and 'ticket' columns (id 1 & 6 of data array)

to_ignore=[6]

# Preprocess data
data = preprocess(data, to_ignore)

# Build neural network
net = tflearn.input_data(shape=[None , 9])
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 3, activation='softmax')
net = tflearn.regression(net)

# Define model
model = tflearn.DNN(net)
#labels = np.reshape(labels, (1, -1))
# Start training (apply gradient descent algorithm)
model.fit(data, labels, n_epoch=20, batch_size=16, show_metric=True)
# Let's create some data for DiCaprio and Winslet
dicaprio = [6,8,2018,16,50,59,'N/A',350,0.016,2]
# Preprocess data
dicaprio = preprocess([dicaprio], to_ignore)
# Predict surviving chances (class 1 results)
pred = model.predict(dicaprio)
print("chance of Rate incress:", pred[0])

