from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import os

REGIONS = ["函館", "宇都宮", "堺", "尾張小牧"]
TARGET_WIDTH = 503
TARGET_HEIGHT = 263

def main():
    colors = {
        "white": [(242, 238, 233)],
        "green": [(12, 38, 21), (27, 69, 50)],
        "black": [(19, 12, 3)],
        "yellow": [(188, 145, 35)]
    }

    settings = {
        "GenShinGothic-P-Medium.ttf": {
            "id": "001",
            "y": -20,
            "fontsize": 210,
            "position": {
                "1": { "w": 300, "x": 45 },
                "2": { "w": 503, "x": 45 },
                "3": { "w": 650, "x": 10 },
                "4": { "w": 850, "x": 0 },
            }
        },
        "HanaMinA.ttf": {
            "id": "002",
            "y": 0,
            "fontsize": 210,
            "position": {
                "1": { "w": 300, "x": 45 },
                "2": { "w": 503, "x": 45 },
                "3": { "w": 650, "x": 10 },
                "4": { "w": 850, "x": 0 },
            }
        }
    }
    
    folder = Path("./font/")
    patterns = ("*.ttf", "*.otf")
    files = [os.path.basename(f) for f in folder.iterdir() if any(f.match(p) for p in patterns)]
    for filename in files:
        for region in REGIONS:
            print(f"{filename} {region}")

            w = settings[filename]["position"][str(len(region))]["w"]
            x = settings[filename]["position"][str(len(region))]["x"]

            imgTemp = Image.new('RGBA', (w, TARGET_HEIGHT), color=(0, 0, 0, 0))
            # imgTemp = Image.new('RGB', (w, TARGET_HEIGHT), color=(255, 0, 0))
            fnt = ImageFont.truetype(f'./font/{filename}', settings[filename]["fontsize"])
            d = ImageDraw.Draw(imgTemp)
            d.text((x, settings[filename]["y"]), region, font=fnt, fill=colors["yellow"][0])
            imgTarget = imgTemp.resize((TARGET_WIDTH, TARGET_HEIGHT), Image.ANTIALIAS)
            
            imgTarget.save(f'./imgs/{region}{settings[filename]["id"]}_w.png')
    

if __name__ == '__main__':
    main()
