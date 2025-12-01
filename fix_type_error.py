# 方案1：适用于 Python 3.9+
# def lower_bound(nums: list[int], target: int) -> int:

# 方案2：适用于 Python 3.8 及更早版本
from typing import List

def lower_bound(nums: List[int], target: int) -> int:
    left = -1
    right = len(nums)
    
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid
            
    return right

# 测试代码
if __name__ == "__main__":
    # 示例测试
    arr = [1, 3, 5, 6]
    target = 5
    result = lower_bound(arr, target)
    print(f"下界索引: {result}")