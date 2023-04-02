



def bruteforceSearch(values, weights, capacity, types):
    num_items = len(values)
    max_value = 0
    best_set = None
    for i in range(2 ** num_items):
        current_weight = 0
        current_value = 0
        item_set = []
        chosen_types = set() # một set chứa loại sản phẩm đã được chọn
        j = 0
        while i > 0:
            if i % 2 == 1:
                current_weight += weights[j]
                current_value += values[j]
                item_set.append(j)
                chosen_types.add(types[j]) # thêm loại sản phẩm vào tập hợp đã chọn
            i //= 2
            j += 1
        # Kiểm tra xem có sản phẩm nào bị bỏ sót không
        for t in set(types):
            if t not in chosen_types:
                # Tìm sản phẩm có value và weight nhỏ nhất của loại đó
                min_weight = float('inf')
                min_value = float('inf')
                min_index = None
                for j in range(num_items):
                    if types[j] == t and weights[j] < min_weight:
                        min_weight = weights[j]
                        min_value = values[j]
                        min_index = j
                current_weight += min_weight
                current_value += min_value
                item_set.append(min_index)
        # Kiểm tra xem tập hợp lời giải có thỏa mãn yêu cầu không
        type_count = {t: 0 for t in set(types)}
        for j in item_set:
            type_count[types[j]] += 1
        if all(count > 0 for count in type_count.values()) and current_weight <= capacity and current_value > max_value:
            max_value = current_value
            best_set = item_set
    return max_value, best_set



def solve(x): #nay tach file ra nha
    with open(f"INPUT_{x}.txt","r") as file:
        lines = file.readlines()

    capacity = int(lines[0])
    numberOfClass = int(lines[1])

    inp = lines[2].split()
    weights = [int(num) for num in inp]

    inp = lines[3].split()
    values = [int(num) for num in inp]

    inp = lines[4].split()
    item_class = [int(num) for num in inp]
    max_value, best_set = bruteforceSearch(values, weights, capacity, item_class)
    res = []
    j = 0
    for i in range(len(values)):#đổi các indices của vật phẩm đã chọn thành format theo yêu cầu đề bài
        if i == best_set[j]:
            res.append(1)
            j += 1
        else:
            res.append(0)
    print(f"Maximum value: {max_value}")
    print(f"Best set of items: {res}")
    with open(f"OUTPUT_{x}.txt","w") as file:
        file.write(str(max_value) + '\n' + str(res))


