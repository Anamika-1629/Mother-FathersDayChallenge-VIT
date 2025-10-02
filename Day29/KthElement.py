import heapq

def findKthLargest(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

if __name__ == "__main__":
    nums = list(map(int, input("Enter array: ").split()))
    k = int(input("Enter k: "))
    print(findKthLargest(nums, k))
