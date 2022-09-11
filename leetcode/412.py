class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = [str(i) for i in range(0, n + 1)]

        round = 1
        while round * 3 <= n:
            if (round * 15) <= n:
                output[round * 15] = 'FizzBuzz'
            if (round * 5) <= n and output[round * 5].isdigit():
                output[round * 5] = 'Buzz'
            if (round * 3) <= n and output[round * 3].isdigit():
                output[(round * 3)] = 'Fizz'

            round += 1

        return output[1:]

# for문으로 n까지 다 돌면서 값 확인해도 통과됨 