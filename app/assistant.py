#
# Создание голосового ассистента
#
# Подключаем необходимые библиотеки,
# предварительно установленные с pypi.org
#

import speech_recognition as sr  # преобразование голоса (отправляется на сервера для распознавания)
# в текст для последующей обработки
import random
import playsound  # воспроизведение аудио через колонки
import os
from gtts import gTTS  # преобразование текста в аудио(голос), отправка запросов на Google service


# Ассистент слушает
def listen():
    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите что-нибудь >>> ")
        audio = voice_recognizer.listen(source)

    try:
        voice_text = voice_recognizer.recognize_google(audio, language="ru")
        # text = input("Скажите что-нибудь >>> ")
        print(f"Вы сказали: {voice_text}")
        return voice_text
    except sr.UnknownValueError:
        return "Ошибка распознавания"
    except sr.RequestError:
        return "Ошибка запроса"


# Ассистент говорит
def say(text):
    voice = gTTS(text, lang="ru")
    unique_file = "audio_" + str(random.randint(0, 10000)) + ".mp3"  # audio_10.mp3
    voice.save(unique_file)

    playsound.playsound(unique_file)
    os.remove(unique_file)

    print(f"Ассистент: {text}")


# Обработка текста введенного с клавиатуры
def handle_command(command):
    command = command.lower()  # Переводим в нижний регистр все слова

    if command == "Привет":
        say("Привет-привет!")
    elif command == "Пока":
        stop()
    else:
        say("Не понятно, повторите")


# Остановка ассистента
def stop():
    say("До скорого!")
    exit()


# Запуск асситента
def start():
    print("Запуск ассистента...")

    while True:  # бесконечный цикл
        command = listen()
        handle_command(command)


# Пробуем запустить ассистента
try:
    start()
    # handle_command('привет')
except KeyboardInterrupt:
    stop()
