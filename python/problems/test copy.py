

def solution(A):
    before = 0
    after = reduce(lambda x, y: x+y, A) - A[0]
    index = 0

    print index, before, after
    if before == after:
        return index

    index += 1

    while index < len(A) :
        before += A[index-1]
        after -= A[index]
        print index, before, after

        if before == after:
            print index

        index += 1


#solution([-1, 3, -4, 5, 1, -6, 2, 1])
solution([1, 2, 3, 4, 0, -10])
