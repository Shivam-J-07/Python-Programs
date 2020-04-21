loop_counter = int(input())
all_elements = []
final_output = []
for i in range(loop_counter):
        user_input = input()
        user_input = user_input.lower()
        input_elements = []
        input_elements = user_input.split()
        if input_elements [0] == "insert":
            index_val = int(input_elements[1])
            all_elements.insert(index_val, input_elements[2])
        elif input_elements [0] == "remove":
            all_elements.remove(input_elements[1])
        elif input_elements[0] == "append":
            all_elements.append(input_elements[1])
        elif input_elements[0] == "sort":
            all_elements = [int(x) for x in all_elements]
            all_elements.sort()
        elif input_elements[0] == "pop":
            all_elements.pop()
        elif input_elements[0] == "reverse":
            all_elements.reverse()
        elif input_elements[0] == "print":
            print(all_elements)
        else:
            print("invalid input mate")







