start_sum = int(input())
target_sum  = int(input())
percent = int(input())
middle_sum = start_sum

while middle_sum < target_sum:
    middle_sum += middle_sum*0.01*percent/12

    print(middle_sum)


