import tensorflow as tf
from tensorflow.keras import layers, models
import os


BATCH_SIZE = 32
IMG_HEIGHT = 180
IMG_WIDTH = 180
DATA_DIR = 'dataset'


train_ds = tf.keras.utils.image_dataset_from_directory(
  DATA_DIR,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(IMG_HEIGHT, IMG_WIDTH),
  batch_size=BATCH_SIZE)


val_ds = tf.keras.utils.image_dataset_from_directory(
  DATA_DIR,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(IMG_HEIGHT, IMG_WIDTH),
  batch_size=BATCH_SIZE)

#  (Train vs Not Train)
class_names = train_ds.class_names
print("Classes found:", class_names)

#  (CNN Architecture)
model = models.Sequential([
  layers.Rescaling(1./255, input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(1, activation='sigmoid') 
])


model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])


print("Training started...")
history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=10 
)


model.save('train_detection_model.keras')
print("Model saved successfully as 'train_detection_model.keras'")


json_config = model.to_json()
with open('model_config.json', 'w') as json_file:
    json_file.write(json_config)
print("Model architecture saved as 'model_config.json'")