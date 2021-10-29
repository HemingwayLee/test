from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import os

regions = ["函館", "宇都宮", "堺", "尾張小牧"]

def main():
    tarWidth = 503
    tarHeight = 263

    settings = {
        "GenShinGothic-P-Medium.ttf": {
            "id": 1,
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
            "id": 2,
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
        for region in regions:
            print(f"{filename} {region}")

            w = settings[filename]["position"][str(len(region))]["w"]
            x = settings[filename]["position"][str(len(region))]["x"]

            # imgTemp = Image.new('RGBA', (w, tarHeight), color=(0, 0, 0, 0))
            imgTemp = Image.new('RGB', (w, tarHeight), color=(255, 0, 0))
            fnt = ImageFont.truetype(f'./font/{filename}', settings[filename]["fontsize"])
            d = ImageDraw.Draw(imgTemp)
            d.text((x, settings[filename]["y"]), region, font=fnt, fill=(255, 255, 0))
            imgTarget = imgTemp.resize((tarWidth, tarHeight), Image.ANTIALIAS)
            
            imgTarget.save(f'./imgs/{region}_{settings[filename]["id"]}.png')
    

if __name__ == '__main__':
    main()
