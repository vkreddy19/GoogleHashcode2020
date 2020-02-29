from itertools import accumulate

dataset = "datasets/d_tough_choices.txt"

def find_sum(books):
    score_sum = 0
    for i in books:
        score_sum += book_scores[i]
    return score_sum


def get_max_books(remaining_days, signup_days, perday, books, n_books):
    max_books = min((remaining_days - signup_days) * perday, n_books)
    books_to_add = books[:max_books]
    new_books_to_add = set(books_to_add) - collected_books

    return books_to_add, find_sum(new_books_to_add)


with open(dataset) as f:
    line = f.readline()
    B, L, D = line.split(" ")
    B, L, D = int(B), int(L), int(D)

    book_scores = [int(i) for i in f.readline().rstrip().split(" ")]
    # print("all books", book_scores)
    # print("B L D", B, L, D)

    libraries = {}

    for i in range(int(L)):
        n_books, signup_days, per_day = f.readline().rstrip().split(" ")
        books = [int(k) for k in f.readline().rstrip().split()]
        # print("n, s , pd", n_books, signup_days, per_day)
        # print(books)
        libraries[i] = [int(n_books), int(signup_days), int(per_day), books]
    # print(libraries)

    result = []
    collected_books = set()

    remaining_days = D
    while remaining_days > 0:
        cur_max = (-1, set(), -1)

        for lid, library in libraries.items():
            if remaining_days - library[1] <= 0:
                continue
            res = get_max_books(remaining_days, library[1], library[2], library[3], library[0])
            if cur_max[2] < res[1]:
                cur_max = (lid, res[0], res[1])
        if not cur_max[1]:
            print("no books to add")
            break
        collected_books.update(cur_max[1])
        result.append(cur_max)
        remaining_days -= libraries[cur_max[0]][1]
        del libraries[cur_max[0]]
        if remaining_days <= 0:
            print("remainig is negative")
            break

    print(result)
    print(find_sum(collected_books))

    with open(dataset + '_result2', 'w+') as r:
        r.write(str(len(result)) + "\n")
        for lib in result:
            r.write("%s %s\n" % (lib[0], len(lib[1])))
            r.write(" ".join(map(str, lib[1])) + "\n")





