def findPairs(numbers_array: list, sum: int) -> None:
  checked = set();
  for number in numbers_array:
    if sum - number in checked:
        print(f'({number},{sum - number})')

    checked.add(number)

def read_input() -> None:
  try:
    numbers_array = list(map(int, input("Enter the array of numbers: ").split()))
    sum = int(input("Enter the sum: "))
    findPairs(numbers_array, sum)
  except:
    print("Invalid input")

if __name__ == '__main__':
  read_input()
