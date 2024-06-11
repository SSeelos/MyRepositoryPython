import sys
import PyQt.App

if __name__ == '__main__':
    try:
        PyQt.App.run(sys.argv)
    except Exception as e:
        print("you've done fucked up")
        print(e)
    else:
        print("at least you tried")
    finally:
        print("I am done")
