dataset = "datasets/e_so_many_books.txt"
import copy
from itertools import permutations


def get_max_books(remaining_days, signup_days, perday, books, n_books):
    max_books = min((remaining_days - signup_days) * perday, n_books)
    books_to_add = books[:max_books]
    new_books_to_add = set(books_to_add) - collected_books

    return max_books, len(new_books_to_add)


def get_count(remaining_days, signup_days, perday, books, n_books):
    max_books = min((remaining_days - signup_days) * perday, n_books)
    books_to_add = books[:max_books]
    return len(set(books_to_add) - collected_books)


with open(dataset) as f:
    line = f.readline()
    B, L, D = line.split(" ")
    B, L, D = int(B), int(L), int(D)

    book_scores = f.readline().rstrip().split(" ")
    # print("all books", book_scores)
    # print("B L D", B, L, D)

    libraries = {}

    for i in range(int(L)):
        n_books, signup_days, per_day = f.readline().rstrip().split(" ")
        books = f.readline().rstrip().split()
        # print("n, s , pd", n_books, signup_days, per_day)
        # print(books)
        libraries[i] = [int(n_books), int(signup_days), int(per_day), books]
    # print(libraries)
    print("done")
    original_libraries = copy.deepcopy(libraries)
    print("done")
    all_possibles = permutations(range(L))
    temp_result = []
    for perm in all_possibles:
        max_iter = []
        collected_books = set()
        rem_days = D
        total = 0
        for i, libid in enumerate(perm):
            t = get_count(rem_days, libraries[libid][1], libraries[libid][2], libraries[libid][3], libraries[libid][0])
            total += t
            collected_books.update(libraries[libid][3][:t])
        temp_result.append((total, perm))

    temp = sorted(temp_result, key=lambda x: x[0])[-1]
    print(temp)


    #
    # result = []
    # collected_books = set()
    #
    #
    # remaining_days = D
    # while remaining_days > 0:
    #     cur_max = (-1, set(), -1)
    #
    #     for lid, library in libraries.items():
    #         if not remaining_days - library[1]:
    #             continue
    #         res = get_max_books(remaining_days, library[1], library[2], library[3], library[0])
    #         if cur_max[2] < res[1]:
    #             cur_max = (lid, res[0], res[1])
    #     if not cur_max[1]:
    #         print("no books to add")
    #         break
    #     else:
    #         remaining_days = remaining_days - library[1]
    #         if remaining_days <= 0:
    #             print("remainig is negative")
    #             break
    #         collected_books = collected_books.union(libraries[lid][:cur_max[1]])
    #         result.append(cur_max)
    #         del libraries[cur_max[0]]
    # print(result)
    # print(collected_books)
    # with open(dataset + '_result2', 'w+') as r:
    #     r.write(str(len(result)) + "\n")
    #     for lib in result:
    #         r.write("%s %s\n" % (lib[0], lib[1]))
    #         r.write(" ".join(original_libraries[lib[0]][:lib[1]]) + "\n")
    #
    #
    #
    #
    #
