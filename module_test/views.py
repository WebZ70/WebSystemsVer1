from django.shortcuts import render


def main(request):
    test_name = "module_test №1"
    return render(request, 'module_test/index.html', locals())