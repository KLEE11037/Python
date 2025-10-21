start_sum = int(input())
percent = int(input())
target_sum  = int(input())
middle_sum = start_sum
month = 0

while middle_sum < target_sum:
    middle_sum += middle_sum*0.01*percent/12
    month += 1

    print(f"{month}-{middle_sum:.2f}")


