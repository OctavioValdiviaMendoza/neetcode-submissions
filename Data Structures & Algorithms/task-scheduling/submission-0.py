class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        input: List of Task ["X","X","Y","Y"] and n = cooldown time
        output: int -> minimum number of CPU cycles

        ["X","X","Y","Y"] n = 2 -> 5
        X,Y,_,X,Y
        ["A","A","A","B","C"] n = 3 -> 9
        A,B,C,_,A,_,_,_,A
        B,C,A,_,_,_,A,_,_,_,A

        *The order we select the processes affects the outcome -> Becasue they all have the same wait time we want to pop the largest first
        We need a maxHeap to know which to pop next. Queue will be used to check when we can push it back to heap
        '''

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() #insert list[-cnt, time after cooldown]

        while maxHeap or q:
            time += 1

            if maxHeap:
                process = 1 + heapq.heappop(maxHeap)
                if process:
                    q.append([process, time + n])
            if q and q[0][1] == time:
                process = q.popleft()[0]
                heapq.heappush(maxHeap, process)
        return time
