# Создание голосового ассистента
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
        # voice_recognizer.adjust_for_ambient_noise(source, duration=5)  # Убираем шум
        audio = voice_recognizer.listen(source)  # слушаем микрофон

    try:
        print("Google..." + voice_recognizer.recognize_google(audio))
        voice_text = voice_recognizer.recognize_google(audio, language="ru")
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
    # unique_file = "audio_" + str(1) + ".mp3"
    # voice.save('song.mp3')
    voice.save(unique_file)
    playsound.playsound(unique_file)
    # playsound('song.mp3')
    print(voice)
    os.remove(unique_file)
    # os.remove('song.mp3')

    print(f"Ассистент: {text}")


# Обработка текста введенного с клавиатуры
def handle_command(command):
    command = command.lower()  # Переводим в нижний регистр все слова
    print('Слово выглядит так:', command)

    if command == "привет":
        say("привет привет")
    elif command == "тест":
        say("запуск теста")
    elif command == "повтори":
        say("повтор команды")
    elif command == "пока":
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
        # command = 'привет'
        handle_command(command)


# Пробуем запустить ассистента
try:
    start()

except KeyboardInterrupt:
    stop()
