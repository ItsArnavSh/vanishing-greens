import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array, image_dataset_from_directory
import pathlib

# Specify the folder path for your images
folder_path = os.path.join('C:\\Users\\mitta\\OneDrive\\Desktop\\Hackathon\\valid\\wildfire1')  # Replace with your actual path

class_names = ['road', 'wild-fire']
img_width = 350
img_height = 350

model = load_model('C:\\Users\\mitta\\OneDrive\\Desktop\\Hackathon\\Deforest.keras')

# Open the text file for writing in append mode
with open("predictions.txt", "a") as f:

  # Get a list of all image file paths in the folder
  image_paths = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path)
                 if filename.endswith(('.jpg','.jpeg','.png'))]

  # Loop through each image path
  for image_path in image_paths:
    img = tf.keras.utils.load_img(
        image_path, target_size=(img_width, img_height)
    )
    img_array = img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    # Write prediction results to the file
    f.write(f"{image_path}\n")

    confidence = 100 * np.max(score)  # Calculate confidence percentage

    if confidence < 75:
      f.write(f"Image not identified since model not trained on it.\n")
    else:
      f.write(
          "This image appears to belong to a forest {} with {:.2f}% precision.\n"
          .format(class_names[np.argmax(score)], confidence)
      )

# Rest of the code for validation_ds (not modified)

validation_dir = pathlib.Path(folder_path)  # Use the same folder path for validation_ds
validation_ds = image_dataset_from_directory(
    validation_dir,
    image_size=(img_width, img_height)
)
