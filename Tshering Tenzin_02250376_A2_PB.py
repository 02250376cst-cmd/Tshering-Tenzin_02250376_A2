def bubble_sort(namesList):

    total = len(namesList)
    
    # Outer loop: number of passes
    for a in range(total-1):
        # Inner loop: compare adjacent elements
        for b in range(0, total - a - 1):
            left = namesList[b].lower()
            right = namesList[b+1].lower()

            # Swap if the previous name comes after the next
            if left > right:
                hold = namesList[b]
                namesList[b] = namesList[b+1]
                namesList[b+1] = hold
                
    return namesList


def insertion_sort(scoreLIST):

    for i in range(1, len(scoreLIST)):
        current = scoreLIST[i]
        k = i - 1

        # Move elements greater than current one step forward
        while k >= 0 and scoreLIST[k] > current:
            scoreLIST[k+1] = scoreLIST[k]
            k -= 1  
        scoreLIST[k+1] = current

    return scoreLIST


def quick_sort(pricelist, count=[0]):

    count[0] += 1  # Increment recursion counter

    if len(pricelist) <= 1:
        return pricelist

    # Choose pivot as middle element
    pivot_index = len(pricelist)//2
    pivot_item = pricelist[pivot_index]

    leftside = []
    middlestuff = []
    rightside = []

    # Divide elements into left, middle, and right based on pivot
    for val in pricelist:
        if val < pivot_item:
            leftside.append(val)
        elif val == pivot_item:
            middlestuff.append(val)
        else:
            rightside.append(val)

    # Recursively sort left and right sublists
    left_sorted = quick_sort(leftside, count)
    right_sorted = quick_sort(rightside, count)

    # Combine left, middle, and right
    combined = left_sorted + middlestuff
    combined2 = combined + right_sorted

    return combined2


def main():
 
    while True:
        print("\n=== Sorting Algorithms Menu ===")
        print("1. Bubble Sort (Names)")
        print("2. Insertion Sort (Scores)")
        print("3. Quick Sort (Book Prices)")
        print("4. Exit")

        choice = input("Enter your choice 1-4: ")

        # Option 1: Bubble Sort for names
        if choice == '1':
            names = ["Kado","Bobchu","Zamu","Nado","Lemo",
                     "Sonam","Choden","Tshering","Kinley","Ugyen",
                     "Karma","Phurba","Nidup","Ngawang","Tenzin"]

            print("Original:", names)
            result = bubble_sort(names.copy())
            print("Sorted:", result)

        # Option 2: Insertion Sort for scores
        elif choice == '2':
            scores = [78,45,92,67,88,54,73,82,91,59,
                      76,85,48,93,71,89,57,80,69,62]

            print("Scores before:", scores)
            sorted_scores = insertion_sort(scores.copy())
            print("After sort:", sorted_scores)

            # Display top 5 scores
            topfive = sorted_scores[-5:]
            topfive.reverse()
            print("Top 5 Scores:")
            for i, num in enumerate(topfive, 1):
                print(str(i) + " -> " + str(num))

        # Option 3: Quick Sort for book prices
        elif choice == '3':
            prices = [450,230,678,125,890,540,760,320,
                      999,870,150,430,600,300,700]

            print("Prices:", prices)
            c = [0]  # Counter for recursion
            sorted_p = quick_sort(prices.copy(), c)
            print("Sorted prices:", sorted_p)
            print("Number of recursive calls:", c[0])

        # Option 4: Exit program
        elif choice == '4':
            print("Exiting... okay bye.")
            break

        # Invalid menu choice
        else:
            print("Wrong choice... please choose again.")

        # Ask user if they want to sort again
        again = input("Sort again? y/n : ").lower()
        if again != "y":
            print("Alright, closing now.")
            break


if __name__ == "__main__":
    main()


