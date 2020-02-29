dataset = "datasets/f_libraries_of_the_world.txt"



def get_max_books(remaining_days, signup_days, perday, books, n_books, collected_books):

    max_books = (remaining_days - signup_days) * perday
    if max_books > n_books:
        max_books = n_books
    if max_books < 0:
        return [], 0
    books_to_add = books[:max_books]
    new_books_to_add = set(books_to_add) - collected_books

    return books_to_add, len(new_books_to_add)


with open(dataset) as f:
    line = f.readline()
    B, L, D = line.split(" ")
    B, L, D = int(B), int(L), int(D)


    book_scores = f.readline().rstrip().split(" ")
    #print("all books", book_scores)
    #print("B L D", B, L, D)

    libraries = {}

    for i in range(int(L)):
        n_books, signup_days, per_day = f.readline().rstrip().split(" ")
        books = f.readline().rstrip().split()
        #print("n, s , pd", n_books, signup_days, per_day)
        #print(books)
        libraries[i] = [int(n_books), int(signup_days), int(per_day), books]
    #print(libraries)

    result = []
    collected_books = set()

    remaining_days = D
    while remaining_days > 0:
        cur_max = (-1, set(), -1)

        for lid, library in libraries.items():
            res = get_max_books(remaining_days, library[1], library[2], library[3], library[0], collected_books)
            if cur_max[2] < res[1]:
                cur_max = (lid, res[0], res[1])
        if not cur_max[1]:
            print("no books to add")
            break
        else:
            remaining_days = remaining_days - library[1]
            if remaining_days <= 0:
                print("remainig is negative")
                break
            collected_books = collected_books.union(cur_max[1])
            result.append(cur_max)
    print(result)
    print(collected_books)
    with open(dataset+'_result', 'w+') as r:
        r.write(str(len(result))+"\n")
        for lib in result:
            r.write("%s %s\n"%(lib[0], len(lib[1])))
            r.write(" ".join(lib[1])+"\n")





