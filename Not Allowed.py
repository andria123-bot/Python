import time
import sys

quotes = [
    ("Now, what's on your nasty old mind?"),
    ("All by yourself, sittin' alone"),
    ("I hope we're still friends, yeah, I hope you don't mind"),
    ("All by yourself, sittin' alone"),
    ("I hope we're still friends, yeah, I hope you don't mind"),
    ("All by yourself, sittin' alone"),
    ("I hope we're still friends, yeah, I hope you don't mind"),
]


def typing_effect(text, delay=0.08):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    time.sleep(0.5)
    sys.stdout.write("\r" + " " * len(text) + "\r")
    sys.stdout.flush()


def main():
    for line in quotes:
        typing_effect(line)


main()
