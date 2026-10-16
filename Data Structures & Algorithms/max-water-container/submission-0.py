class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        We are given a arr with heights, we want to find the max water the contaiter can hold 

        To calculate width index (right - left)
        to calculate height min(heights[right], heights[left])

        start at diff ends of the create two pointers:
        p1 = 0 
        p2 = len(arr) - 1
        whole p1 < p2:
        calculate p1 p2 width get min 
        height
        area = width times heights
        max_area = max(area,max_area)
        compare p1 p2 move smaller one if p1 is smaller += 1 if p2 is smaller -=1
        '''
        p1 = 0
        p2 = len(heights) - 1
        max_area = 0

        while p1 < p2:
            width = p2 - p1
            height = min(heights[p2], heights[p1])
            area = width * height
            max_area = max(max_area, area)

            if heights[p1] < heights[p2]:
                p1 += 1
            elif  heights[p2] < heights[p1]:
                p2 -=1
            else:
                p1 += 1
            
        return max_area

