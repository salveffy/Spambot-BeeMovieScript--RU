#чтобы все адекватно работало, необходимо запускать бота с английской раскладкой,
# так pyatogui не поддерживает русский язык, пришлось переводить на английскую раскладку
import pyautogui, time

layout = dict(zip(map(ord, "йцукенгшщзхъфывапролджэячсмитьбю.ё" 
                           'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'),

                            "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                           'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'))

fileRead = open('script.txt','r',encoding='utf8')
fileWrite = open('scriptTranslate.txt','w',encoding='utf8')
for line in fileRead:
    fileWrite.write(line.translate(layout))

fileRead.close()
fileWrite.close()

time.sleep(5)  # есть 5 секунд, чтобы навести курсор на поле для ввода сообщения
pyautogui.hotkey('shift','altleft') # переключает раскладку с английского на русскую
for word in open('scriptTranslate.txt','r'):
     pyautogui.write(word)
     pyautogui.press('enter')

