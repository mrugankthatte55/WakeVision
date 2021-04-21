
import headers as headers

def validate(image_path):

  image = headers.tf.keras.preprocessing.image.load_img(image_path, grayscale=False, color_mode="rgb", target_size=(224,224), interpolation="nearest")
  
  input_arr = headers.keras.preprocessing.image.img_to_array(image)
  input_arr = headers.np.array([input_arr])
  input_arr = headers.tf.keras.applications.mobilenet.preprocess_input(input_arr)
  #start = time.time()
  predictions = headers.model.predict(input_arr)
  #print(time.time()-start)
  #time.sleep(20)
  return round(predictions[0][0])