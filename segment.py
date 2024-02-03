from tensorflow.keras.models import load_model
MODEL_NAME =   'model_fmr_all.h5'
import numpy as np
from PIL import Image
model = load_model(MODEL_NAME)                                              # Загрузка весов модели
#model.summary()
INPUT_SHAPE = (28, 28, 1)


def process(image_file):
    image = Image.open(image_file)  # Открытие обрабатываемого файла
    resized_image = image.resize((INPUT_SHAPE[1], INPUT_SHAPE[0]))          # Изменение размера изображения в соответствии со входом сети
    array = np.array(resized_image)[...][np.newaxis, ..., np.newaxis]   # Регулировка формы тензора для подачи в сеть
    prediction_array = (255 * model.predict(array)).astype(int)             # Запуск предсказания сети
    prediction_result = np.argmax(prediction_array)
    return prediction_result                           # Возврат исходного уменьшенного изображения, найденной маски и исходного изображения с наложенной маской