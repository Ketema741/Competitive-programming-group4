def decode(s, mult=1) -> str:
    curnt_str = ''

    while self.idx < len(s):
        if s[self.idx].isdigit():
            curnt_mult = ''

            while s[self.idx].isdigit():
                curnt_mult += s[self.idx]
                self.idx += 1

            self.idx += 1
            curnt_str += decode(s, mult = int(curnt_mult))

        elif s[idx].isalpha():
            curnt_str += s[self.idx]
            self.idx += 1

        else:
            self.idx += 1
            return mult*curnt_str

    return mult*curnt_str
