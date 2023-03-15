from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    word_Dict = {}

    for word in wordlist:
        if word in word_Dict:
            # increase here
            word_Dict[word] += 1
        else:
            # add to the dictionary
            word_Dict[word] = 1

    sortedwords = sorted(
        word_Dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})


def about(request):
    return render(request, 'about.html')
