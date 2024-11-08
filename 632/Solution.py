import heapq

def smallestRange(nums):
    min_heap = []
    current_max = float('-inf')
    for i in range(len(nums)):
        heapq.heappush(min_heap, (nums[i][0], i, 0))  
        current_max = max(current_max, nums[i][0])

        
    best_range = [-float('inf'), float('inf')]
    
    while min_heap:
        current_min, list_idx, elem_idx = heapq.heappop(min_heap)
        
        if current_max - current_min < best_range[1] - best_range[0]:
            best_range = [current_min, current_max]
        
        if elem_idx + 1 == len(nums[list_idx]):
            break
        
        next_elem = nums[list_idx][elem_idx + 1]
        heapq.heappush(min_heap, (next_elem, list_idx, elem_idx + 1))
        current_max = max(current_max, next_elem)
    
    return best_range

nums = [
    [-1,1], [-2,2], [-3,3], [-4,4], [-5,5], [-6,6], [-7,7], [-8,8], [-9,9], [-10,10], 
    [-11,11], [-12,12], [-13,13], [-14,14], [-15,15], [-16,16], [-17,17], [-18,18], 
    [-19,19], [-20,20], [-21,21], [-22,22], [-23,23], [-24,24], [-25,25], [-26,26], 
    [-27,27], [-28,28], [-29,29], [-30,30], [-31,31], [-32,32], [-33,33], [-34,34], 
    [-35,35], [-36,36], [-37,37], [-38,38], [-39,39], [-40,40], [-41,41], [-42,42], 
    [-43,43], [-44,44], [-45,45], [-46,46], [-47,47], [-48,48], [-49,49], [-50,50], 
    [-51,51], [-52,52], [-53,53], [-54,54], [-55,55]
]
print(smallestRange(nums)) 
