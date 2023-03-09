import csv
from collections import namedtuple, Counter, defaultdict
from datetime import datetime
import matplotlib.pyplot as plt

review = namedtuple("review", "grade,user_name,text,date,passed,variation")

def read_file(file):
    with open (file, mode = "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        count = 0
        count2 = 0
        for grade,_,_,_ in reader:
            count += int(grade)
            count2 += 1
        f.seek(0)
        next(reader)
        reviews = [review(int(grade), user_name, text, datetime.strptime(date, "%Y-%m-%d"), int(grade) >= 5, int(grade)-(count/count2)) for grade,user_name,text,date in reader]
    return reviews

def filter_by_grade(file, n = 5):
    return [e for e in read_file(file) if e.grade == n]

def filter_by_date(file, date, recent = True):
    if "-" in date:
        i = "-"
    elif "/" in date:
        i = "/"
    date = datetime.strptime(date, "%Y{}%m{}%d".format(i, i))
    if recent == True:
        return [e for e in read_file(file) if e.date >= date]
    if recent == False:
        return ([e for e in read_file(file) if e.date <= date])

def count_by_grade(file, n):
    return len([e for e in read_file(file) if e.grade == n])

def count_by_year(file, y): 
    return len([e for e in read_file(file) if e.date.year == y])

def total_pass(file):
    return len([e for e in read_file(file) if e.passed == True])

def pass_percentage(file):
    p = (total_pass(file)*100)/len(read_file(file))
    return float("{:.2f}".format(p))

def extreme_grade(file, max = True):
    l = sorted([e for e in read_file(file)], key=lambda e:e.grade, reverse = max)
    return [e for e in l if e[0] == l[0][0]]

def extreme_date(file, max = True):
    l = sorted([e for e in read_file(file)], key=lambda e:e.date, reverse = max)
    return [e for e in l if e.date == l[0].date]

def sorted_length_containing(file, content, max = True):
    return sorted([e for e in read_file(file) if content.lower() in e.text.lower()], key=lambda e:len(e.text), reverse = max)

def group_by_grade(file):
    d = dict()
    r = read_file(file)
    grades = set(e.grade for e in r)
    for e in grades:
        s = list(i for i in r if e == i.grade)
        d[e] = s
    return d

def group_by_date(file):
    d = dict()
    r = read_file(file)
    dates = set(e.date for e in r)
    for e in dates:
        s = list(i for i in r if i.date == e)
        d["{}-{}-{}".format(e.year, e.month, e.day)] = s
    return d

def count_reviews_per_grade(file):
    grades = [e.grade for e in read_file(file)]
    return Counter(grades)

def count_reviews_per_date(file):
    d = list("{}-{}-{}".format(e.date.year, e.date.month, e.date.day) for e in read_file(file))
    return Counter(d)

def characters_written_per_date(file):
    l = read_file(file)
    d = sorted(set(e.date for e in l))
    dct = defaultdict(int)
    for r in l:
        for e in d:
            if e == r.date:
                dct["{}-{}-{}".format(e.year, e.month, e.day)] += len(r.text)
                break
    return dct

def extreme_reviews_by_grade(file, max = True):
    d = sorted(count_reviews_per_grade(file).items(), key=lambda e:e[1], reverse = max)
    return [e for e in d if e[1] == d[0][1]]

def extreme_characters_by_date(file, max = True):
    d = sorted(characters_written_per_date(file).items(), key=lambda e:e[1], reverse = max)
    return [e for e in d if e[1] == d[0][1]]

def max_variation_per_date(file, max = True):
    f = read_file(file)
    d = set(e.date for e in f)
    dct = dict()
    for e in d:
        l = set()
        for r in f:
            if e == r.date:
                l.add(r.variation)
        l = sorted(l, key = abs, reverse = max)
        dct["{}-{}-{}".format(e.year, e.month, e.day)] = [e for e in l if e == l[0]]
    return dct

def max_user_length_by_letter(file, max = True):
    l = "abcdefghijklmnopqrstuvwxyz"
    d = defaultdict(set)
    for r in read_file(file):
        for e in l:
            if e in r.user_name.lower():
                d[e].add(r.user_name)
    d = {e:sorted(d[e], key=lambda i:len(i), reverse = max) for e in l}
    return {e:sorted([i for i in d[e] if len(i) == len(d[e][0])]) for e in l}

def plot(x, y, title = "", xl = "x", yl = "y", grid = True):
    plt.plot(x, y)
    plt.xticks(x, rotation=45)
    plt.title(title)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.grid(grid)
    plt.show()