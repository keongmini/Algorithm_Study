class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = ''
        current_string = ''

        for char in s:
            if char.isdigit():
                current_num += char

            elif char == '[':
                stack.append(current_string)
                stack.append(current_num)
                current_string = ''
                current_num = ''

            elif char == ']':
                num = stack.pop()
                if num:
                    num = int(num)

                prev_string = stack.pop()
                current_string = prev_string + num * current_string

            else:
                current_string += char

        return current_string



