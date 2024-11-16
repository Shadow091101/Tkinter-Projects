# Description:

This Python program uses the tkinter library to create a simple graphical user interface (GUI) that allows users to input text and have it read aloud using the pyttsx3 text-to-speech (TTS) engine.

## Features:

- **Text-to-Speech Functionality**: The user can type text into the input field, and upon pressing the "Speak" button, the text is spoken aloud using the pyttsx3 engine.
- **Voice Customization**: The program allows customization of the voice. By default, it uses a female voice, but this can be changed to a male voice by adjusting the voice property of pyttsx3.
- **Volume and Rate Adjustment**: The program also sets a fixed volume level (50%) and adjusts the speech rate to 125 words per minute. These can be customized further to meet user preferences.
- **Tkinter GUI**: The application features a basic interface with a text entry box and a button, making it user-friendly and easy to use.

## Requirements:

1. Python 3.x
2. pyttsx3 library (for text-to-speech)
3. tkinter library (for GUI)

## Usage:

1. Enter any text in the input field.
2. Press the "Speak" button to hear the text aloud.
3. The voice will read the text, and the input field will be cleared after each use.

## Customization:

You can modify the engine.

```sh
setProperty('volume', 0.5) 
```
and

```sh
 engine.setProperty('rate', 125) 
```

to adjust the volume and speech rate.

The voice can be switched between male and female by changing the index in 
```sh
engine.setProperty('voice', voices[0].id)
```

## Example Output:

The program will read aloud the entered text with the specified voice, volume, and rate settings.
