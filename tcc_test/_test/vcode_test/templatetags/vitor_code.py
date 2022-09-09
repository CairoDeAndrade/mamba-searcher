from django.shortcuts import render
import os


def index(request):
    global i
    dirPath = r"C:\Users\entra21\Desktop\tcc_test"
    result = next(os.walk(dirPath))[2]

    num = 0
    for j in range(len(result)):
        num += 1

        return render(request, 'vcode_test/index.html', {'num': num,
                                                             })
