import pyautogui as pt
import time
import datetime
import keyboard

def main():
    try:
        img = pt.locateOnScreen('images/wpp.png', confidence=0.6)
        now = datetime.datetime.now().hour
        
        while not keyboard.is_pressed('q'):
            if now != 8:
                time.sleep(30)
                continue
            else:
                if img:
                    pt.moveTo(img, duration=0.5, tween=pt.easeOutQuad)
                    pt.click(clicks=2)

                    time.sleep(2)

                    img = pt.locateOnScreen('images/group.png')
                    pt.moveTo(img, duration=0.5, tween=pt.easeOutQuad)
                    pt.click()

                    time.sleep(1)

                    img = pt.locateOnScreen('images/input.png')
                    pt.moveTo(img, duration=0.5, tween=pt.easeOutQuad)
                    pt.click()

                    time.sleep(1)

                    write_on_input('good morning!')
                    break
    except pt.ImageNotFoundException:
        print('Error: image not found')

def write_on_input(frase: str):
    pt.write(f'{frase}', interval=0.1)
    pt.press('enter')


if __name__=='__main__':
    main()