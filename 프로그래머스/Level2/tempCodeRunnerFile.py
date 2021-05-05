    if len(heap) == 0:
            break
        for srt, dest, cost in road:
            print(heap)
            current_node, current_cost = heapq.heappop(heap)
            next_cost = current_cost+cost
            if current_node == srt and next_cost < dist[dest]:
                dist[dest] = next_cost
                heapq.heappush(heap, [dest, next_cost])

            if current_node == dest and next_cost < dist[srt]:
                dist[srt] = next_cost
                heapq.heappush(heap, [srt, next_cost])