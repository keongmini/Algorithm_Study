class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()

        for email in emails:
            idx = email.index('@')
            after = ''
            domain = email[idx:]
            for char in email[:idx]:
                if char == '.':
                    continue

                if char == '+':
                    break

                after += char

            result.add(after + domain)

        return len(result)