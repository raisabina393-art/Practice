def check(x):
    print("funtion called for value:",x)
    return True if x>0 else False

a= check
b= check
c= check

if a(-10) or b(-50) or c(-20):
    print("Atleast one true")
else:
    print("all false")
