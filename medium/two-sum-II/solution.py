class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers) - 1
        i = 0
        j = n

        while(i < j):
          print(numbers[i] , numbers[j])
          if (numbers[i] + numbers[j] == target):
              return [i+1, j+1]
          elif (numbers[i] + numbers[j] > target):
            j -= 1    
          else:
            i += 1     
