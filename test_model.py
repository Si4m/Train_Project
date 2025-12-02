import tensorflow as tf
import numpy as np


model = tf.keras.models.load_model('train_detection_model.keras')


img_path = 'test_image.jpg'
img = tf.keras.utils.load_img(
    img_path, target_size=(180, 180)
)
img_array = tf.keras.utils.img_to_array(img)
# Create a batch
img_array = tf.expand_dims(img_array, 0) 

predictions = model.predict(img_array)
score = predictions[0][0]

# Print result in English
if score > 0.5:
    print(f"This is a TRAIN ({100 * score:.2f}% confidence)")
else:
    print(f"This is NOT a train ({100 * (1 - score):.2f}% confidence)")