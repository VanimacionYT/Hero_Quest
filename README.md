
# Hero Quest

## Academy project developed in Python, originaly using Jupyter Notebook, and now developed on Visual Studio Code as IDE, which I will update with everything I learn and can be applied.

This project/game is my first serius in depth game made in python following the instructions and information that I gather from my Python academy [Tokio School](https://www.tokioschool.com).
As of now it includes:
* A *main menu* with various options using *Enum Library* and *Controlong Files*.
* A *virtual dice system* using "random" library and modifyable values to the minimal and maximal values usind *Enum Library* and *Controlong Files*.
* A *character system* using objects, clases, getters, setters and all other OOP concepts.
* A Log system that captures the events and registers characters informarion and game results in 3 diferent text files using *file management* and being able to check those while in the game using the menu.
* A *time event capturer* using the library "datetime". Working on implementing *Time zone management* and features with "pytz".
* A class working with *Enum Library* and *Controlong Files* to control the various phases of the game.

# Python Version 
As of right now using python version **3.12.0** (Newest)

# Dependencies
As of now using the following libraries:
* Random
* Datetime
* Locale
* Time [Link](https://pypi.org/project/TIME-python/)
      - Pip instalation ```pip install TIME-python```
* Enum [Link](https://pypi.org/project/enum/)
      - Pip instalation ```pip install enum```

# How to modificate
Keep in mind i'm new, I don't know 100% how to use, manage or assist on GitHub.

Because this is a project of mine I give full consent if you want to use, copy, modify or help me upgrade the project.
Feel free to modify as you want respecting the lisence terms.

For any issues or sugestions you can contact me via discord: *(heyne_cositas / VanimaYT#8738)*

## What does this project contain?

* This project contains inside the SRC folder the key files for the program to work and a LOG folder to store data and a Control folder to control the global and current events and values.
* HeroQuest.py is the main source for the .exe version. and the manager of all the files in SRC/. If you want to try the game out inside a code editor you must run this file in order for everythn to work.

Also the Log folder is the one where the logs are stores, such as:
* LogGames.txt is the file where the log of every game is saved.
* LogPlayers.txt is the file where the log of every player is saved.
* LogSystem.txt is the file where the logs are stored in a way that can be then opened to be read inside the program.
* LogDices.txt is the file where the log values of the dice maximum and minimum values are stored for the program to read.

Release may include:
* The .exe file, necessary to boot the program as a game. (*May launch errors and is far from perfect. Please read [Known Issues](https://github.com/VanimacionYT/Hero_Quest/blob/main/README.md#known-issues))

## Known Issues

- Windows detects the Hero-Quest.exe at (Hero-Quest.zip) as a **threat**.
    -Fix: This is a common error on the python community as I understand. **File is not a thread**, it is detected as if it was. Currently working to send Microsoft a copy to flag as *false positive*, but that is under consideration. [Documentation about the errors](https://stackoverflow.com/questions/54730851/windows-defender-detecting-python-exe-as-trojan) 

If you find any issue or bug, don't hesitate to try and tell me or even fix it!

## What happended to the Jupyter Notebokk version?

After consideration I decided that for improving my work flow and my results I will only focus on the main idea of creating the proyect/game. As of now the .ipynb version of HeroQuest will be deleted.
If you want to use the code in jupyter is as simple as copying the main codes to the platform.

For any issues or sugestions you can contact me via discord: *(heyne_cositas / VanimaYT#8738)*
