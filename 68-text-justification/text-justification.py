class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0

        while i < len(words):
            j = i
            length = 0

            # Find words that fit in the current line
            while j < len(words) and length + len(words[j]) + (j - i) <= maxWidth:
                length += len(words[j])
                j += 1

            gaps = j - i - 1
            spaces = maxWidth - length

            # Last line or line with one word
            if j == len(words) or gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:
                extra = spaces // gaps
                remainder = spaces % gaps

                line = ""

                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (extra + (1 if k - i < remainder else 0))

                line += words[j - 1]

            result.append(line)
            i = j

        return result