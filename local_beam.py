import random



def knapsack_local_beam_search(values, weights, capacity, k, max_iter, item_types):
    # Khởi tạo k trạng thái bắt đầu ngẫu nhiên
    states = []
    for i in range(k):
        state = []
        for j in range(len(values)):
            state.append(random.choice([0, 1]))
        # Thêm yêu cầu ít nhất 1 vật phẩm của mỗi loại được chọn cho trạng thái ban đầu. Khi này ta có thể đảm bảo rằng ở trạng thái ban đầu, ít nhất 1 vật phẩm mỗi loại được chọn
        for item_type in item_types:
            item_indices = [i for i in range(len(values)) if item_types[i] == item_type]
            if all(state[i] == 0 for i in item_indices):# trường hợp này là không có vật phầm nào thuộc item type nằm trong state( == 0)
                state[random.choice(item_indices)] = 1
        states.append(state)

    # Lặp lại cho đến khi đạt đến số lần lặp tối đa
    for _ in range(max_iter):
        # giá trị của mỗi trạng thái và lựa chọn k trạng thái tốt nhất(cho các trạng thái ban đầu)
        evals = []
        for state in states:
            value = sum([v * s for v, s in zip(values, state)])
            weight = sum([w * s for w, s in zip(weights, state)])
            if weight > capacity:
                evals.append(float('-inf'))#thêm giá trị không hợp lệ (-inf) vào nếu w > C
            else:
                evals.append(value)
        sorted_indices = sorted(range(len(evals)), key=lambda k: evals[k], reverse=True)#sắp xếp các chỉ số của list evals theo giá trị tương ứng của các phần tử trong list đó (từ lớn đến bé) và trả về một list mới chứa các chỉ số đã sắp xếp.
        states = [states[i] for i in sorted_indices[:k]]

        # Thực hiện các thay đổi ngẫu nhiên trên mỗi trạng thái được chọn
        new_states = []
        for state in states:
            for _ in range(5):
                new_state = state.copy()
                index = random.randint(0, len(state) - 1)
                new_state[index] = 1 - new_state[index]
                new_states.append(new_state)
        #Thêm yêu cầu ít nhất 1 vật phẩm của mỗi loại được chọn sau khi qua các giai đoạn ngẫu nhiên, để đảm bảo không bị thiếu xót vật phẩm nào của từng loại
        for new_state in new_states:
            for item_type in item_types:#tìm kiếm trong mảng class item
                item_indices = [i for i in range(len(values)) if item_types[i] == item_type]#tìm kiếm trong value ta đã tạo
                if all(new_state[i] == 0 for i in item_indices):
                    new_state[random.choice(item_indices)] = 1

        # Lựa chọn k trạng thái tốt nhất từ các trạng thái mới được tạo
        evals = []
        for state in new_states:
            value = sum([v * s for v, s in zip(values, state)])
            weight = sum([w * s for w, s in zip(weights, state)])
            if weight > capacity:
                evals.append(float('-inf'))
            else:
                evals.append(value)
        sorted_indices = sorted(range(len(evals)), key=lambda k: evals[k], reverse=True)
        states = [new_states[i] for i in sorted_indices[:k]]

    
    best_state = states[0]#danh sách các vật phẩm được chọn
    best_value = sum([v * s for v, s in zip(values, best_state)])#giá trị tốt nhất
    
    # Trả về mảng đồ vật đã được chọn và giá trị tốt nhất
    return best_state, best_value







def solve(x):
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
    
    k = 15
    max_iterations = 1000

    solution, value = knapsack_local_beam_search(values, weights, capacity, k, max_iterations, item_class)
    print("Solution: ", solution)
    print("value: ", value)
    with open(f"OUTPUT_{x}.txt","w") as file:
        file.write(str(value) + '\n' + str(solution))