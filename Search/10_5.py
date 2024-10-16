def pack(weight, max_box, cap):
    box_used = 1
    load = 0
    for w in weight:
        if w > cap:
            return False
        if load + w > cap:
            box_used += 1
            load = w
        else:
            load += w
    return box_used <= max_box

def find_min(weights, max_box):
    low = max(weights)
    high = sum(weights)
    answer = high
    while low <= high:
        mid = (low + high) // 2
        if pack(weights, max_box, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    return answer

inp = input("Enter Input : ")
things, box = inp.strip().split('/')
weight = list(map(int,things.strip().split()))
max_box = int(box.strip())

print(f"Minimum weigth for {max_box} box(es) = {find_min(weight, max_box)}")