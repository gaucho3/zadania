try:
    f = open('testfile.txt')
except IOError as e :
    print(e)
except Exception as e:
    print('Error')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")