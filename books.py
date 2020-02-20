#!/usr/bin/env python3

""" Hash Code 2020 solver.

Using python 3.8.1
"""

import sys

class Library:
    def __init__(self, id, number_of_books, signup_days, books_per_day):
        self.id = id
        self.number_of_books = number_of_books
        self.signup_days = signup_days
        self.books_per_day = books_per_day
        self.books = []


class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score


class World:
    def __init__(self, file):
        line = self._readline(file)

        # first line of input
        self.number_of_books = line[0]
        self.number_of_libraries = line[1]
        self.days_for_scanning = line[2]

        # book scores, second line of input
        self.book_scores = self._readline(file)

        self.libraries = []
        # read each library
        for i, x in enumerate(range(self.number_of_libraries)):
            # read library header
            line = self._readline(file)
            lx = Library(i, line[0], line[1], line[2])

            # read books from this library
            book_ids = self._readline(file)
            for bid in book_ids:
                lx.books.append(Book(bid, self.book_scores[bid]))

            # add this library
            self.libraries.append(lx)

    def _readline(self, file):
        """Return a list of integers."""
        return [int(x) for x in file.readline().strip().split()]

    def __str__(self):
        return (f'{self.number_of_books} books, '
                f'{self.number_of_libraries} libraries, '
                f'{self.days_for_scanning} days')



if __name__ == "__main__":
    filename = sys.argv[1]

    with open(filename) as f:
        w = World(f)

        print(w.number_of_libraries)
        for l in w.libraries:
            print(f'{l.id} {l.number_of_books}')
            print(' '.join(str(b.id) for b in l.books))