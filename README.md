# sars-cov-dice
Statistical Analysis and Randomized Simulation for Consecutive Outcome Variation - Dice edition

Just a shitty project for simulating dice rolls


# How to build the windows executable

1. Follow the steps here to install wine [https://wiki.winehq.org/Debian](https://wiki.winehq.org/Debian)
2. Follow those steps [https://www.makeworld.space/2021/10/linux-wine-pyinstaller.html](https://www.makeworld.space/2021/10/linux-wine-pyinstaller.html)
3. Also read this: [https://customtkinter.tomschimansky.com/documentation/packaging/](https://customtkinter.tomschimansky.com/documentation/packaging/)


My command line looked like this:

```bash
wine C:/Python312/Scripts/pyinstaller.exe --noconfirm --onedir --windowed --add-data "C:/Python312/Lib/site-packages/customtkinter:customtkinter/" main.py
```
I did it with python 3.12.3 and it worked.
