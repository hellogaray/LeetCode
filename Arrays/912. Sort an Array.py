class Solution(object):
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums

        def merge(left, right):
            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        left_sorted = self.sortArray(left_half)
        right_sorted = self.sortArray(right_half)

        return merge(left_sorted, right_sorted)

