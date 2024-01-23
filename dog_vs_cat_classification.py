# -*- coding: utf-8 -*-
"""Dog vs Cat Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZWDTQ_k97dPZjTfXuknDh6XHGDnaCEvX
"""

# installing kaggle library
!pip install kaggle

#Configuring the path of Kaggle.json file
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

"""Importing Dataset From Kaggle"""

#Kaggle API
!kaggle competitions download -c dogs-vs-cats

# Extracting the compressed dataset
from zipfile import ZipFile

dataset = '/content/dogs-vs-cats.zip'

with ZipFile(dataset, 'r') as zip:
  zip.extractall()
  print('The dataset is extracted')

# Extracting the compressed dataset
from zipfile import ZipFile

dataset = '/content/train.zip'

with ZipFile(dataset, 'r') as zip:
  zip.extractall()
  print('The dataset is extracted')

import os
#Counting the no. of File in train folder
path, dirs, files = next(os.walk('/content/train'))
file_count = len(files)
print("Number of images: ",file_count)

"""Printing the Name of Images"""

file_names = os.listdir('/content/train/')
print(file_names)

"""Importing Dependencies"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.model_selection import train_test_split
from google.colab.patches import cv2_imshow

"""Displaying the Images"""

# display dog image
img = mpimg.imread('/content/train/dog.5940.jpg')
imgplt = plt.imshow(img)
plt.show()

# display cat image
img = mpimg.imread('/content/train/cat.7502.jpg')
imgplt = plt.imshow(img)
plt.show()

"""Counting the number of dog and cat images"""

file_names = os.listdir('/content/train/')
dog = 0
cat = 0
for img_file in file_names:
  if img_file.startswith('dog'):
    dog+=1
  else:
    cat+=1
print("Number of dog images: ",dog)
print("Number of cat images: ",cat)

"""Resizing All the images"""

#Creating a directory for resized images
os.mkdir('/content/image_resized')

org = "/content/train/"
rez = "/content/image_resized/"

for i in range(2500):

  filename = os.listdir(org)[i]
  img_path = org + filename

  img = Image.open(img_path)
  img = img.resize((224, 224))
  img = img.convert('RGB')

  newImgPath = rez + filename
  img.save(newImgPath)

# display Resized dog image
img = mpimg.imread('/content/image_resized/dog.5940.jpg')
imgplt = plt.imshow(img)
plt.show()

# display Resized cat image
img = mpimg.imread('/content/image_resized/cat.7502.jpg')
imgplt = plt.imshow(img)
plt.show()

"""**Creating labels for resized images of dogs and cats**

Cats -> 0

Dogs -> 1
"""

# Creating a for loop to assign labels
file_names = os.listdir('/content/image_resized')


labels = []

for i in range(2500):

  file_name = file_names[i]
  label = file_name[0:3]

  if label == 'dog':
    labels.append(1)

  else:
    labels.append(0)

print(labels)
print(len(labels))

# counting the images of dogs and cats out of 2500 images
values, counts = np.unique(labels, return_counts=True)
print(values)
print(counts)

"""Converting all the resized images to numpy arrays"""

import cv2
import glob

img_dir = '/content/image_resized/'
img_ext = ['png', 'jpg']

files = []

[files.extend(glob.glob(img_dir + '*.' + e)) for e in img_ext]

dog_cat_images = np.asarray([cv2.imread(file) for file in files])

print(type(dog_cat_images))
print(dog_cat_images.shape)

X = dog_cat_images
Y = np.asarray(labels)

"""**Train Test Split**"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""2000 -> Training images

500 -> Test images
"""

# Scaling the data
X_train_scaled = X_train/255

X_test_scaled = X_test/255

print(X_train_scaled)

"""**Building the Neural Network**"""

import tensorflow as tf
import tensorflow_hub as hub

mobilenet_model = 'https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4'

pretrained_model = hub.KerasLayer(mobilenet_model, input_shape = (224,224,3), trainable = False)

num_of_classes = 2

model = tf.keras.Sequential([
    pretrained_model,
    tf.keras.layers.Dense(num_of_classes)


])

model.summary()

model.compile(
    optimizer = 'adam',
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics = ['acc']
)

model.fit(X_train_scaled, Y_train, epochs=5)

score, acc = model.evaluate(X_test_scaled,Y_test)
print("Test Loss: ", score)
print("Test Accuracy: ", acc)

"""**Predictive System**"""

input_img_path = input("Path of the image to be predicted: ")

input_img = cv2.imread(input_img_path)

input_img_rez = cv2.resize(input_img, (224,224))

cv2_imshow(input_img_rez)

input_img_scaled = input_img_rez/255

img_reshaped = np.reshape(input_img_scaled, [1, 224, 224, 3])

input_pred = model.predict(img_reshaped)

input_pred_label = np.argmax(input_pred)

if input_pred_label == 0:
  print("The image represents a CAT")
else:
  print("The image represents a DOG")
