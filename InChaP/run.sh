#!/bin/sh
#   Author        : Levent Aydinbakar
#   Date          : 17-36-20---27-03-2024
#   Last Modified : 22-08-51---28-09-2024


pyside6-uic main.ui -o guidata/ui_main.py
pyside6-rcc icons.qrc -o icons_rc.py
