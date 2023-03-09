from review import *

def read_file_test(file):
    r = read_file(file)
    print ("--- TOTAL REVIEWS: ---\n")
    print(len(r))
    print("\n--- FIRST 3 REVIEWS: ---\n")
    print(*r[:3], sep = "\n\n")
    print("\n--- LAST 3 REVIEWS: ---\n")
    print(*r[-3:], sep = "\n\n")

def filter_by_grade_test(file, n = 5):
    f = filter_by_grade(file, n)
    print("\n---- TOTAL REVIEWS FILTERED BY GRADE = {}: ---\n".format(n))
    print(len(f))
    print("\n---- FIRST 2 REVIEWS FILTERED BY GRADE = {}: ---\n".format(n))
    print(*f[:2], sep = "\n\n")
    print("\n---- LAST 2 REVIEWS FILTERED BY GRADE = {}: ---\n".format(n))
    print(*f[-2:], sep = "\n\n")

def filter_by_date_test(file, date, recent = True):
    d = filter_by_date(file, date, recent)
    print("\n---- TOTAL REVIEWS WRITTEN FROM {date} TO {order}: ---\n".format(date=date, order="NOW" if recent == True else "THE FIRST"))
    print(len(d))
    print("\n---- FIRST 2 REVIEWS FROM {date} TO {order}: ---\n".format(date=date, order="NOW" if recent == True else "THE FIRST"))
    print(*d[:2], sep = "\n\n")
    print("\n---- LAST 2 REVIEWS ({order}): ---\n".format(order="MOST RECENT" if recent == True else "OLDEST"))
    print(*d[-2:], sep = "\n\n")

def count_by_grade_test(file, n):
    c = count_by_grade(file, n)
    print("\n---- TOTAL REVIEWS WITH A GRADE = {}: ---\n".format(n))
    print(c)

def count_by_year_test(file, y):
    c = count_by_year(file, y)
    print("\n---- TOTAL REVIEWS WRITTEN IN {}: ---\n". format(str(y)))
    print(c)

def total_pass_test(file):
    p = total_pass(file)
    print("\n---- TOTAL REVIEWS WITH A GRADE >= 5: ---\n")
    print(p)

def pass_percentage_test(file):
    p = pass_percentage(file)
    print("\n---- PERCENTAGE OF REVIEWS WITH A GRADE >= 5: ---\n")
    print(p, "%")

def extreme_grade_test(file, max = True):
    e = extreme_grade(file, max)
    print("\n---- TOTAL REVIEWS WITH THE {ext} GRADE ({grade}): ---\n".format(ext="MINIMUM" if max == False else "MAXIMUM", grade="0" if max == False else "10"))
    print(len(e))
    print("\n---- 2 REVIEWS WITH THE {} GRADE: ---\n".format("MINIMUM" if max == False else "MAXIMUM"))
    print(*e[:2], sep = "\n\n")

def extreme_date_test(file, max = True):
    e = extreme_date(file, max)
    print("\n---- TOTAL REVIEWS WRITTEN THE {} DAY: ---\n".format("FIRST" if max == False else "LAST"))
    print(len(e))
    print("\n---- 2 REVIEWS WRITTEN THE {} DAY: ---\n".format("FIRST" if max == False else "LAST"))
    print(*e[:2], sep = "\n\n")

def sorted_length_containing_test(file, content, max = True):
    l = sorted_length_containing(file, content, max)
    print('\n---- TOTAL REVIEWS CONTAINING "{}": ---\n'.format(content))
    print(len(l))
    print('\n---- {order} REVIEW CONTAINING "{content}": ---\n'.format(order="SHORTEST" if max == False else "LARGEST", content=content))
    print(*l[:1], sep = "\n\n")
    print('\n---- {order} REVIEW CONTAINING "{content}": ---\n'.format(order="LARGEST" if max == False else "SHORTEST", content=content))
    print(*l[-1:], sep = "\n\n")

def group_by_grade_test(file):
    d = group_by_grade(file)
    print('\n---- TOTAL GRADES: ---\n')
    print(d.keys())
    print('\n---- FIRST REVIEW WITH EVERY GRADE: ---\n')
    for e in d:
        print("\n---- " + str(e) + ": ----\n", d[e][0], sep = "\n\n")
    
def group_by_date_test(file):
    d = group_by_date(file)
    print('\n---- TOTAL DATES: ---\n')
    print(d.keys())
    print('\n---- A REVIEW OF EVERY DAY: ---\n')
    for e in d:
        print("\n---- " + str(e) + ": ----\n", d[e][0], sep = "\n\n")

def count_reviews_per_grade_test(file):
    d = count_reviews_per_grade(file)
    print('\n---- NUMBER OF REVIEWS PER GRADE: ---\n')
    for e in d:
        print("{} reviews have a grade of {}".format(d[e], e))
    
def count_reviews_per_date_test(file):
    d = count_reviews_per_date(file)
    print('\n---- NUMBER OF REVIEWS PER DAY: ---\n')
    for e in d:
        print("{} reviews written on {}".format(d[e], e))

def characters_written_per_date_test(file):
    d = characters_written_per_date(file)
    print('\n---- CHARACTERS WRITTEN PER DAY: ---\n')
    for e in d:
        print("{} characters written on {}".format(d[e], e))

def extreme_reviews_by_grade_test(file, max = True):
    print('\n---- {} COMMON GRADE: ---\n'.format("MOST" if max == True else "LESS"))
    a = extreme_reviews_by_grade(file, max)
    print("{} reviews graded with a {}".format(a[0][1], a[0][0]))

def extreme_characters_by_date_test(file, max = True):
    print('\n---- {} Nº OF CHARACTERS WRITTEN ON A DAY: ---\n'.format("MAXIMUM" if max == True else "MINIMUM"))
    a = extreme_characters_by_date(file, max)
    print("{} characters written on {}".format(a[0][1], a[0][0]))

def max_variation_per_date_test(file, max = True):
    print('\n---- {} VARIATION PER DATE (ABS VALUE): ---\n'.format("MAXIMUM" if max == True else "MINIMUM"))
    d = max_variation_per_date(file, max)
    for e in d:
        print(e, d[e])

def max_user_length_by_letter_test(file, l, max = True):
    print('\n---- EXAMPLE OF THE {ord} USERNAMES, CONTAINING "{content}": ---\n'.format(ord = "LONGEST" if max == True else "SHORTEST", content = l))
    print(max_user_length_by_letter(file)[l][0])

def main():

    route = "data/user_reviews.csv"

    print("\n--------- START --------\n")

    print("\n****** read_file_test(file): ******\n")
    read_file_test(route)

    print("\n****** filter_by_grade_test(file, n = 5): ******\n")
    filter_by_grade_test(route, 2)
    filter_by_grade_test(route)

    print("\n****** filter_by_date_test(file, date, recent = True): ******\n")
    filter_by_date_test(route, "2020-4-2", False)
    filter_by_date_test(route, "2020-4-30")

    print("\n****** count_by_grade_test(file, n): ******\n")
    count_by_grade_test(route, 3)
    count_by_grade_test(route, 7)

    print("\n****** count_by_year_test(file, y): ******\n")
    count_by_year_test(route, 2020)
    count_by_year_test(route, 2019)

    print("\n****** total_pass_test(file): ******\n")
    total_pass_test(route)

    print("\n****** pass_percentage_test(file): ******\n")
    pass_percentage_test(route)

    print("\n****** extreme_grade_test(file, max = True): ******\n")
    extreme_grade_test(route, False)
    extreme_grade_test(route)

    print("\n****** extreme_date_test(file, max = True): ******\n")
    extreme_date_test(route, False)
    extreme_date_test(route)

    print("\n****** sorted_length_containing_test(file, content, max = True): ******\n")
    sorted_length_containing_test(route, "island", False)
    sorted_length_containing_test(route, "game")

    print("\n****** group_by_grade_test(file): ******\n")
    group_by_grade_test(route)

    print("\n****** group_by_date_test(file): ******\n")
    group_by_date_test(route)

    print("\n****** count_reviews_per_grade_test(file): ******\n")
    count_reviews_per_grade_test(route)

    print("\n****** count_reviews_per_date_test(file): ******\n")
    count_reviews_per_date_test(route)

    print("\n****** characters_written_per_date_test(file): ******\n")
    characters_written_per_date_test(route)

    print("\n****** extreme_reviews_by_grade_test(file, max = True): ******\n")
    extreme_reviews_by_grade_test(route)
    extreme_reviews_by_grade_test(route, False)

    print("\n****** extreme_characters_by_date_test(file, max = True): ******\n")
    extreme_characters_by_date_test(route)
    extreme_characters_by_date_test(route, False)

    print("\n****** max_variation_per_date_test(file, max = max): ******\n")
    max_variation_per_date_test(route)
    max_variation_per_date_test(route, False)

    print("\n****** max_user_length_by_letter_test(file, l, max = True): ******\n")
    max_user_length_by_letter_test(route, "a")
    max_user_length_by_letter_test(route, "f", False)
    max_user_length_by_letter_test(route, "z")

    print("\n****** PLOTTING THE NUMBER OF CHARACTERS PER DAY: ******\n")
    l = characters_written_per_date(route)
    plot(list(l.keys()), list(l.values()), "CHARACTERS WRITTEN PER DAY", "DAYS", "CHARACTERS")

    print("\n****** PLOTTING THE NUMBER OF REVIEWS PER DAY: ******\n")
    a = count_reviews_per_date(route)
    plot(list(a.keys()), list(a.values()), "REVIEWS WRITTEN PER DAY", "DAYS", "REVIEWS")

    print("\n--------- END --------\n")
    
if __name__ == "__main__":
    main()