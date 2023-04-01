import requests


def get_sparc_result(query):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'http://wave.ttu.edu/ajax.php'
    payload = {"action": 'getQuery', "query": query,
               "editor":
                   """ sorts
                   #people={tommy,alex,john,daniel,sarah,peter,lino}.
                   #book={book1,book2}.
                   #book_categories={drama, crime, fantasy, scientific}.
                   #day={monday, tuesday, sunday, weekday}.
                   #hours={morning_8_to_6pm, morning_8_to_12pm}.
                   predicates
                   categories(#book_categories,#book).
                   book_author(#people,#book).
                   opening_hours(#day,#hours).
                   rules
                   opening_hours(weekday, morning_8_to_6pm).
                   opening_hours(sunday, morning_8_to_12pm).
                   """}

    x = requests.post(url, headers=headers, data=payload)
    print(x.text)
    return x.text


# get_sparc_result('opening_hours(monday,X)')
