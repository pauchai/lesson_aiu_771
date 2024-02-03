import streamlit as st
from PIL import Image
from segment import process

st.title('Digits recognizer demo')

image_file = st.file_uploader('Load an image', type=['png', 'jpg'])  # Добавление загрузчика файлов

if not image_file is None:                       # Выполнение блока, если загружено изображение
    col1, col2 = st.columns(2)                   # Создание 2 колонок # st.beta_columns(2)
    image = Image.open(image_file)               # Открытие изображения
    results = process(image_file)                # Обработка изображения с помощью функции, реализованной в другом файле
    st.text("Source image:")
    st.image(image)                       # Вывод в первой колонке уменьшенного исходного изображения
    st.text("Результат:")
    st.text(results)                         # Вывод исходного изображения с наложенной маской (по центру)
    