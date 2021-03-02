if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for key in student_marks.keys():
        if key == query_name:
            numlist = student_marks[query_name]
            sumoff = sum(numlist)
            avg = sumoff/len(numlist)
            
    print("%.2f" % avg)
