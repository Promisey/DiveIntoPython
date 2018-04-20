try:
    f = open("f:\\Ishare\\DiveIntoPython\\MP3\\1.mp3", "rb", 0)
    try:
        f.seek(-128, 2)
        tagdata = f.read(128)
        print(tagdata)
    finally:
        f.close()
finally:
    pass
#except IOError:
#    print("error")