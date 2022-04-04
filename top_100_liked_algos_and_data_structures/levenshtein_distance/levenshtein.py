def levenshtein(X, Y) -> int:
    m, n = len(X), len(Y)
    if m == 0: return n
    if n == 0: return m

    cost = 0
    try: 
        for i in range(n if n > m else m):
            if Y[i] != X[i]: cost += 1
    
    except IndexError:
        cost += n - m if n > m else m - n

    return cost

 
if __name__ == "__main__":
    from time import time
    X = "kafkjahdfkjhakjdshfksdfkjhasdkjfskahfkjsadkfjhaskdhfhajkfvakhdghasdfauhuiawrhbduabudfajfdnaiuwedhbfnwadiuhbfnkaergfuhbjnadsfhvbhjwadkfjvj"
    Y = "faljkdkjdafhhiusahdjfkadhfkjhadjhfiuahsduifjakljhakdhfkjhajwioendkajsdnjlfiwheadfhakjdfhakjhhajdhfjkahdkfhakdfhakjhdfhakjdfahdf"
    m, n = len(X), len(Y)
    start = time()
    print(levenshtein(X, Y))
    print(time() - start)
