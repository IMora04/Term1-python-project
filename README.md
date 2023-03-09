# First Term Project. Fundamentals of programming (Course  22/23)
Autor/a: Ignacio Mora Pérez.  uvus: ignmorper1

My dataset consists on analysing reviews of the game "[Animal Crossing: New Horizons](https://www.animal-crossing.com/new-horizons/es/)", a Nintendo Switch videogame released in 2020. These dataset contains the information of the mark (integer), the username (string), the text (string) and the date of the review (date). As there is not any logic variable, I have introduced a new one based on the grade of the review, named "pass".

## Project folder structure

* **/src**: Contains the python modules that make up the project.
  * **[review.py](#review-module)**: Contains functions to read the CSV file and the important functions.
  * **[review_test.py](#review-test-module)**: Module to test functions from `review.py`. Main function is in this module.
* **/data**: Contains the project dataset.
    * **user_reviews.csv**: CSV file with the data of the reviews.
    
## *Dataset* structure

The dataset is made up of 4 columns, with the following description:

* **Grade**: type integer, represents the grade given by the user that has written the review, rated from 0 to 10
* **Username**: type string, is the name of the user that has written the review.
* **Text**: type string, contains the information of the review.
* **Date**: type date, indicates the moment when the review was made.

## Implemented types:

In the file `review.py`, I define the named tuple "review".

`review = namedtuple("review", "grade, user_name,text,date,passed,variation")`

The type of each element of the tuple is:

`review(int, str, str, datetime.date, bool, float)`

The last two elements, "passed" and "variation", are new elements that we get from the grades of the reviews. The first one is a logic value that is true when the grade is equal or greater than 5, and the second one is a float value that indicates how much does the grade vary with respect to the average grade of all the reviews in our dataset.

## Implemented functions

In this project, the following functions have been implemented. They are structured in blocks according to the deliveries in which they had to be uploaded. The main module is `review.py`.

### Review module

#### First delivery - Basic structure of the project. Creating modules and Readme.

* **read_file(file)**: It reads the data from the CSV file, calculates the two variables mentioned before (passed, variation) and creates the list of tuples incluiding the information about the reviews.

#### Second delivery - Blocks I and II. Creating first functions.

* **Block I:**
  
  * **filter_by_grade(file, n = 5)**: It returns a list of reviews, filtered by the grade specified in theparameter "n". It will return only the reviews that have that grade.
  
  * **filter_by_date(file, date, recent = True)**: It returns a list of reviews, filtered by the date specified in the parameter "date". In this case, it will return reviews from the date specified to the present, if "recent" == True, or to the first review done, if "recent" == False. By default, it returns the most recent ones. It is also important to mention that the parameter "date" accepts strings of type": "YYYY-MM-DD" or "YYYY/MM/D".
    
  * **count_by_grade(file, n)**: Function that counts the total amount of reviews that have the grade specified in the parameter "n".
    
  * **count_by_year(file, y)**: Similarly as the previous one, this function counts the number of reviews written on the year specified in the parameter "y".
    
  * **total_pass(file)**: This function returns a list of reviews that have a grade greater or equal than five. It does so by checking if the "passed" element of the review is equal to True.
    
  * **pass_percentage(file)**: Function that returns the percentage of reviews that graded the game with a five or more. It uses the previous function `total_pass(file)` to calculate the number of passes, and then compute the percentage with respect to the total reviews. It will show the percentage with only 2 decimal digits.

* **Block II:**
  
  * **extreme_grade(file, max = True)**: This function returns the maximum or minimum value of all the grades of the reviews. If "max" is True, it will return all the reviews with the maximum grade (10), and if "max" is False, it returns the reviews with the minimum grade (0).
    
  * **extreme_date(file, max = True)**: This function works similarly as the previous one, but with dates. It returns the most recent or the oldest review, depending on the value of "max".
    
  * **sorted_length_containing(file, content, max = True)**: This function filters the reviews that contain the word or characters specified in "content", and returns the filtered list sorted by the length of the review, from greatest to lowest if "max" == True, or in the opposite way if "max" == False.
    
  * **group_by_grade(file)**: This function returns a dictionary whose keys are equal to all the possible grades of the reviews, and whose values are lists of reviews that graded the game with the value of the key.
    
  * **group_by_date(file)**: Similarly as the previous function, this function returns a dictionary where the keys are all the dates when there were reviews made, and the values are lists of the reviews made in that date. To make keys more accessible, we transform the date of the review, that is of type "datetime", to type "string", transforming it into the form "YYYY-MM-DD", and then assigning that strings to the keys.

#### Third delivery - Blocks III and IV. Last functions and graphic representations.

* **Block III:**
  
  * **count_reviews_per_grade(file)**: In this function, the number of reviews per grade is counted. It returns a dictionary whose keys are all the grades used, and whose values are the amount of reviews that used that grade.
  
  * **count_reviews_per_date(file)**: This function works in a similar way as the previous one. Now, the dictionary that is returned has the dates in which there were reviews written as keys, in the format "YYYY-MM-DD", and the number of reviews written those dates as values.

  * **characters_written_per_date(file)**: This function returns a dictionary in which keys are all the dates when there were reviews written, and values are the amount of characters written every day, in all the reviews.

  * **extreme_reviews_by_grade(file, max = True)**: This function uses the function `count_reviews_by_grade(file)` to create a list including either the most or the least repeated grade among all the reviews, depending on the parameter "max". If this parameter is True, then it will return the most repeated, and if not, it will return the least repeated.
  
  * **extreme_characters_by_date(file, max = True)**: This function also uses another function, in this case `characters_written_per_date(file)`, to create a list with the dates in which more characters where written.

  * **max_variation_per_date(file, max = True)**: It returns a dictionary that stores all the dates when reviews were written as keys, and the maximum or minimum variation from the average grade among all the reviews written that day as values. It will return the maximum variation when the parameter "max" is True, and the minimum when it is False. (Maximum or minimum is taken as the absolute value).
  
  * **max_user_length_by_letter(file, max = True)**: This function returns a dictionary whose keys are all the letters from a to z, and whose values are lists containing the longest or shortest usernames that contain such letters. These lists are in alphabetical order. It will return the longest usernames when the parameter "max" is set to True, and the shortest otherwise.
  
* **Block IV:**

  * **plot(x, y, title = " ", xl = "x", yl = "y", grid = True)**: This function is just a quick way to make graphic representations. In this case, it is an ordinary plot function, that needs at least two parameters: x and y. These two parameters should be two lists, that would be represented in the x and y axes respectively. We can also add a title, that would be empty if not specified, an x-label ("xl") and a y-label ("y"), to denote what is being represented in each axis (x and y if not specified), and the grid, that is True by default in order to get a more precise representation.

### Review test module

In the test module, the following functions have been defined, each one used to test the equally named functions in the `review.py` module:

* **read_file_test(file)**: This function tests the function `read_file(file)`  by reading the file introduced, and printing the length of the list read, the first three elements, and the last three elements.
  
* **filter_by_grade_test(file, n = 5)**: It tests the function `filter_by_grade(file, n = 5)` by showing the total reviews, the first two and the last two reviews with grade n.

* **filter_by_date_test(file, date, recent = True)**: This function is a test of `filter_by_date(file, date, recent = True)`. Depending on the parameter "recent", it shows the total, first 2 and last 2 reviews from the date specified in "date" to the first review or to the last review. Tested with 2 examples, with the 2 possible values of "max" and 2 random dates.

* **count_by_grade_test(file, n)**: It is a test of the function `count_by_grade(file, n)` with two example values.

* **count_by_year_test(file, y)**: As the previous test, it tests the function `count_by_year(file,y)` with two example values.

* **total_pass_test(file)**: Tests the function `total_pass(file)` by executing it.

* **pass_percentage_test(file)**: Tests the function `pass_percentage(file)` by executing it.

* **extreme_grade_test(file, max = True)**: This function tests `extreme_grade(file, max = True)` by printing the total reviews with the maximum or minimum grade, and 2 reviews with this grade. Tested with the 2 possible values of "max".

* **extreme_date_test(file, max = True)**: It works similarly as the previous test: Tests the function `extreme_date(file, max = True)` by printing the total and 2 reviews written the first or the last day.

* **sorted_length_containing_test(file, content, max = True)**: This function tests `sorted_length_containing(file, content, max = True)`. It shows the total reviews, and the ones with the largest and the shortest text, containing what we specify in "content". It was tested with the 2 different values of "max" and with 2 random words

* **group_by_grade_test(file)**: It tests the function `group_by_grade(file)` by printing all the keys (grades), and every grade with the first review with that grade.

* **group_by_date_test(file)**: As the previous function, it tests `group_by_date(file)` by printing all the keys (dates), and every date with the first review written that date.

* **count_reviews_per_grade_test(file)**: This function tests the function `count_reviews_per_grade(file)` by printing the number of reviews that used each grade.

* **count_reviews_per_date_test(file)**: It works as the previous function. This functino tests `count_reviews_per_date(file)` by printing the number of reviews written each date.

* **characters_written_per_date_test(file)**: In this function, `characters_written_per_date(file)` is tested. It prints the number of characters written each day.

* **extreme_reviews_by_grade_test(file, max = True)**: It is a tests of the function `extreme_reviews_by_grade(file, max = True)` by printing the most and the least common grade, with the number of reviews that used those grades.

* **extreme_characters_by_date_test(file, max = True)**: This function is a test of `extreme_characters_by_date(file, max = True)`. It prints the dates when the maximum and minimum number of characters were written, and both quantities.

* **max_variation_per_date_test(file, max = True)**: It tests the function `max_variation_per_date(file, max = True)` by printing the maximum and minimum variations of each date. 

* **max_user_length_by_letter_test(file, max = True)**: This function tests the function `max_user_length_by_letter(file, max = True)` by printing 3 examples of usernames: 2 of them are examples of longests usernames containing "a" or "z", and the other one is an example of the shortests usernames containing "f".

* **`plot(x, y, title = " ", xl = "x", yl = "y", grid = True)`**: This function does not have a defined "test" function, but is executed twice as tests. The two graphics shown are the number of characters written per day, and the number of reviews written per day. It can be seen comparing both representations that they are very similar, but with slight differences. This makes sense, because if more reviews are written, more characters will be written as well.

![Reviews per day](https://github.com/FP-22-23/term-project-IMora04/blob/main/data/Screenshot%202022-12-11%20at%2016.34.57.png)
![Character per day](https://github.com/FP-22-23/term-project-IMora04/blob/main/data/Screenshot%202022-12-11%20at%2016.35.07.png)