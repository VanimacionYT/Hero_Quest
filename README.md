
# Hero Quest

## Academy project developed in Python, originaly using Jupyter Notebook, and now developed on Visual Studio Code as IDE, which I will update with everything I learn and can be applied.

This project/game is my first serius in depth game made in python following the instructions and information that I gather from my Python academy [Tokio School](https://www.tokioschool.com).
As of now it includes:
* A rough *main menu* with 2 options using *while and if* commands.
* A *virtual dice system* using "random" library.
* A *character system* using objects, clases, getters, setters.
* A Log system that captures the events and registers characters informarion and game results in 2 diferent text files using *file management*
* A *time event capturer* using the library "datetime". Working on implementing *Time zone management* and features with "pytz"

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

* This project contains inside the SRC folder the key files for the program to work
* HeroQuest.py is the main source for the .exe version. and the manager of all the files in SRC/.

Also the Log folder is the one where the logs are stores, such as:
* LogPartidas.txt is the file where the log of every game is saved.
* LogPersonajes.txt is the file where the log of every game is saved.

Release may include:
* The .exe file, necessary to boot the program as a game. (*May launch errors and is far from perfect. Please read [Known Issues](https://github.com/VanimacionYT/Hero_Quest/blob/main/README.md#known-issues))

## Known Issues

- Windows detects the Hero-Quest.exe at (Hero-Quest.zip) as a **threat**.
    -Fix: This is a common error on the python community as I understand. **File is not a thread**, it is detected as if it was. Currently working to send Microsoft a copy to flag as *false positive*, but that is under consideration. [Documentation abut the errors](https://stackoverflow.com/questions/54730851/windows-defender-detecting-python-exe-as-trojan) 

If you find any issue or bug, don't hesitate to try and tell me or even fix it!

## What happended to the Jupyter Notebokk version?

After consideration I decided that for improving my work flow and my results I will only focus on the main idea of creating the proyect/game. As of now the .ipynb version of HeroQuest will be deleted.
If you want to use the code in jupyter is as simple as copying the main codes to the platform.

For any issues or sugestions you can contact me via discord: *(heyne_cositas / VanimaYT#8738)*
