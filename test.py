# from operator import itemgetter
# from collections import namedtuple
#
# Film = namedtuple("Film", ["name", "runtime_min", "director"])
#
# best_picture_2026 = [
#     Film("Bugonia",                 118, "Yorgos Lanthimos"),
#     Film("F1",                      155, "Joseph Kosinski"),
#     Film("Frankenstein",            150, "Guillermo del Toro"),
#     Film("Hamnet",                  125, "Chloé Zhao"),
#     Film("Marty Supreme",           150, "Josh Safdie"),
#     Film("One Battle After Another", 162, "Paul Thomas Anderson"),
#     Film("The Secret Agent",        161, "Kleber Mendonça Filho"),
#     Film("Sentimental Value",       133, "Joachim Trier"),
#     Film("Sinners",                 137, "Ryan Coogler"),
#     Film("Train Dreams",            102, "Clint Bentley"),
# ]
#
# print(best_picture_2026)
#
# def format_sort_films(lst: list, srtcrit) -> list:
#     output = []
#     for item in sorted(lst, key=lambda x : getattr(x, srtcrit)):
#         output.append(f'{item.name:24} {item.runtime_min:10} {item.director:15}')
#     return output
# # print('***Sorted by film***')
# # print('\n'.join(format_sort_films(best_picture_2026, 'name')))
# # print('***Sorted by duration***')
# # print('\n'.join(format_sort_films(best_picture_2026, 'runtime_min')))
# # print('***Sorted by director***')
# # print('\n'.join(format_sort_films(best_picture_2026, 'director')))
#
# while True:
#     userinput = input("""
# Choose a criteria to sort the films:
# 1. Film name
# 2. Runtime
# 3. Director name
# q to quit
# """
#                       )
#     if userinput == 'q':
#         break
#     elif userinput not in "123":
#         print('Invalid choice. Choose 1, 2, or 3')
#         continue
#     elif userinput == '1':
#         print('\n'.join(format_sort_films(best_picture_2026, 'name')))
#     elif userinput == '2':
#         print('\n'.join(format_sort_films(best_picture_2026, 'runtime_min')))
#     elif userinput == '3':
#         print('\n'.join(format_sort_films(best_picture_2026, 'director')))

def foo(x):
    def bar(y):
        return x * y
    return bar
f = foo(10)
print(f(20))

def foo():
    call_counter = 0
    def bar(y):
        nonlocal call_counter
        call_counter += 1
        return f'y = {y}, call_counter = {call_counter}'
    return bar

b = foo()
for i in range(10, 100, 10):
    print(b(i))