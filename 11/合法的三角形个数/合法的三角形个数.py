while 1:
    try:
        nums = list(map(int, input().split()))
        nums = sorted(nums)
        lens = len(nums)

        # [left, right] 窗口内的数和 [i] 始终满足三角形
        count = 0
        for i in range(lens):
            left = i + 1
            right = i + 2
            while left < lens:
                while right < lens and nums[right] < nums[i] + nums[left]:
                    count += max(right - left, 0)
                    right += 1
                left += 1
        print(count)
    except Exception:
        break
