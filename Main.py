import sys
import PyQt.App

try:
    PyQt.App.Run(sys.argv)
except Exception as e:
    print("you've done fucked up")
    print(e)
else:
    print("at least you tried")
finally:
    print("I am done")