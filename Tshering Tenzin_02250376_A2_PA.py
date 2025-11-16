def linear_search(students, find_id):

    found = -1
    comparisons = 0
       
    for i in range(len(students)):
        comparisons = comparisons + 1

        if students[i] == find_id:
            found = i + 1  
            break
     
    return found, comparisons


def binary_search(scores, look_for):

    start = 0
    end = len(scores) - 1
    check_count = 0
    result_pos = -1

    while start <= end:
        check_count = check_count + 1
        mid = (start + end) // 2

        if scores[mid] == look_for:
            result_pos = mid + 1
            break
        elif scores[mid] < look_for:
            start = mid + 1
        else:
            end = mid - 1

    return result_pos, check_count



def main():

    student_ids = [1001, 1005, 1002, 1008, 1003, 1010, 1004, 1009, 1007, 1012,
                   1011, 1015, 1016, 1006, 1013, 1014, 1018, 1019, 1020, 1021]

    scores_sorted = [45, 52, 58, 63, 67, 72, 75, 78, 82, 85,
                     88, 90, 92, 95, 98, 99, 100, 102, 104, 106]

    while True:
        print("\n=== Searching Algorithms Menu ===")
        print("1. Linear Search - Find Student ID")
        print("2. Binary Search - Find Score")
        print("3. Exit Program")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            print("\nStudent IDs List:", student_ids)
            try:
                id_to_find = int(input("Enter the Student ID you want to search for: "))
            except:
                print("Oops! You must enter a number.")
                continue

            pos, tries = linear_search(student_ids, id_to_find)
            if pos != -1:
                print(" Student ID", id_to_find, "found at position", pos)
            else:
                print(" Student ID", id_to_find, "was not found in the list.")
            print("Total comparisons made:", tries)

        elif choice == "2":
            print("\nSorted Scores:", scores_sorted)
            try:
                score_find = int(input("Enter the score to search for: "))
            except:
                print("You must type a number, not text!")
                continue

            pos, comps = binary_search(scores_sorted, score_find)
            if pos != -1:
                print(" Score", score_find, "found at position", pos)
            else:
                print(" Score", score_find, "was not found in the list.")
            print("Comparisons done:", comps)

        elif choice == "3":
            print("Thanks for using my program! (finally works lol)")
            break

        else:
            print("Invalid choice, please pick between 1, 2 or 3.")

        again = input("\nDo you want to search again? (y/n): ")
        if again.lower() != 'y':
            print("Okay bye! Program finished.")
            break



if __name__ == "__main__":
    main()
