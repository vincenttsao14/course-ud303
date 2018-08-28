from urllib import request, parse

def read_text():
    quotes = open(r"C:\Users\vince\Downloads\newtext.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    encodedurl = "http://www.wdylike.appspot.com/?q="
    encodedurl = encodedurl + parse.quote(text_to_check)
    with request.urlopen(encodedurl) as url:
        output = url.read()
        print(output)

    if b"true" in output:
        print('Profanity alert!')
    elif b"false" in output: 
        print('No profanity!')
    else:
        print('Could not scan!')
read_text()
