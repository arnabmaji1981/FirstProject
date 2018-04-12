from urllib.request import urlopen
import urllib.request

def read_file():
    contents = open("C:\\Users\\HP\\Desktop\\arnab\\cursewords\\movie_qoutes.txt")
    qoutes = contents.read()
    print(qoutes)
    check_badwords(qoutes)

def check_badwords(words_tocheck):
    connection = urlopen("http://www.wdylike.appspot.com/?a="+words_tocheck)

    output = connection.read()
    print(output)


read_file()

