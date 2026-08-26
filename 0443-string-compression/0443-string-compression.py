class Solution(object):
    def compress(self, chars):
        write = 0
        i = 0

        while i < len(chars):
            current = chars[i]
            count = 0

            while i < len(chars) and chars[i] == current:
                i += 1
                count += 1

            chars[write] = current
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write