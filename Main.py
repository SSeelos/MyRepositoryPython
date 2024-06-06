import sys
import PyQt.App

try:
    PyQt.App.Run(sys.argv)
except:
    print("you've done fucked up")
else:
    print("at least you tried")
finally:
    print("I am done")