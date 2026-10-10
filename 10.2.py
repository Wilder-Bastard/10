from PIL import Image, ImageDraw, ImageFont
import os
slovar = {
    "День рождения": "DR.jpg",
    "Любой": "universal.jpg",
    "День доброты": "kind_day.jpg"
}
word = input("Введите ваш праздник\n").title()
if word == "День рождения":
    print("Вот открытка под ваш праздник\n")
    img = Image.open("Dr.jpg")
    img.show()
elif word == "Любой":
    print("Вот открытка под ваш праздник\n")
    img = Image.open("universal.jpg")
    img.show()
elif word == "День доброты":
    print("Вот открытка под ваш праздник\n")
    img = Image.open("kind_day.jpg")
    img.show()
else:
    print("Введите один из трёх вариантов: день рождения, любой, день доброты")