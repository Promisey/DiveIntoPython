# fsock = open(r"\notthere")
try:
    fsock = open(r"\notthere")
except IOError:
    print("The file does not exit")
print("This line will always print")

try:
    import termios, TERMIOS
except ImportError:
    try:
        import msvcrt
    except ImportError:
        try:
            from EasyDialogs import AskPassword
        except ImportError:
            getpass = default_getpass
        else:
            getpass = AskPassword
    else:
        getpass = win_getpass
else:
    getpass = unix_getpass