def countDroppedRequests(server):
    capacity = 0  # Total available threads
    dropped_requests = 0
    
    for event in server:
        if event == -1:  # Request comes in
            if capacity > 0:
                capacity -= 1  # Serve the request using a thread
            else:
                dropped_requests += 1  # No available threads, drop the request
        else:
            capacity += event  # Add threads to the capacity
    
    return dropped_requests

# Test cases
test_cases = [
    [-1, -1, -1, -1],
    [4, -1, -1, -1],
    [1, -1, 1, -1],
    [1, -1, -1, 4],
]

for idx, test_case in enumerate(test_cases):
    dropped = countDroppedRequests(test_case)
    print(f"Test case {idx + 1}: Dropped requests = {dropped}")
