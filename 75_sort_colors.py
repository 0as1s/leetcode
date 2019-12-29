def s(colors):
    left = 0
    left_sorted = 0
    right = len(colors) - 1
    right_sorted = len(colors) - 1
    dire = 0
    while left_sorted <= right_sorted:
        if left >= len(colors) or right < 0:
            break
        if dire == 0:
            if colors[left] == 2:
                colors[left], colors[right_sorted] = colors[right_sorted], colors[left]
                dire = 1
                right_sorted -= 1
            elif colors[left] == 1:
                dire = 1
                right -= 1
            else:
                left += 1
        if dire == 1:
            if colors[right] == 0:
                colors[left_sorted], colors[right] = colors[right], colors[left_sorted]
                dire = 1
                left_sorted += 1
            elif colors[right] == 1:
                left += 1
                dire = 0
            else:
                right -= 1

    print(colors)


s([2,0,2,1,1,0,2,1,0,1,2,0,2,1,0])