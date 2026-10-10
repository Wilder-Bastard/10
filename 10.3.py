from PIL import Image, ImageDraw, ImageFont
slovar = {
    "День рождения": "DR.jpg",
    "Любой": "universal.jpg",
    "День доброты": "kind_day.jpg"
}
word = input("Введите ваш праздник\n").title()
name = input("Кому?\n").title()
if word in slovar:
    img = Image.open(slovar[word])
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arialbold.ttf", size=45)
    except:
        try:
            font = ImageFont.truetype("Arial Bold.ttf", size=45)
        except:
            font = ImageFont.load_default()
    text = f"{name}, поздравляю."
    bbox = draw.textbbox((0,0), text, font=font)
    text_wight = bbox[2] - bbox[0]
    x = (img.width - text_wight) // 2
    draw.text((x, 50), text, fill=(255, 0, 0, 255), font=font)

    img.save('greeting_card.png')
    img.show()
    print("Открытка сохранена как 'greeting_card.png'")
else:
    print("Такого праздника нет в списке!")
