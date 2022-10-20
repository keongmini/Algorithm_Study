# recursion
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        reversible_pairs = [
            ['0', '0'], ['1', '1'],
            ['6', '9'], ['8', '8'], ['9', '6']
        ]

        def generate_strobo_numbers(n, final_length):
            if n == 0:
                return [""]

            if n == 1:
                return ["0", "1", "8"]

            prev_strobo_nums = generate_strobo_numbers(n - 2, final_length)     # 길이 0 또는 1까지 들어가고 거기서 시작 (가운데부터 처리하기 위해)
            curr_strobo_nums = []

            for prev_strobo_num in prev_strobo_nums:
                for pair in reversible_pairs:
                    if pair[0] != '0' or n != final_length:
                        curr_strobo_nums.append(pair[0] + prev_strobo_num + pair[1])

            return curr_strobo_nums

        return generate_strobo_numbers(n, n)

# iteration
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        reversible_pairs = [
            ['0', '0'], ['1', '1'],
            ['6', '9'], ['8', '8'], ['9', '6']
        ]

        curr_strings_length = n % 2

        q = ["0", "1", "8"] if curr_strings_length == 1 else [""]

        while curr_strings_length < n:
            curr_strings_length += 2
            next_level = []

            for number in q:
                for pair in reversible_pairs:
                    if curr_strings_length != n or pair[0] != '0':
                        next_level.append(pair[0] + number + pair[1])
            q = next_level

        return q