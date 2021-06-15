# the running time for this algoritm is constan time or 0(1)
class solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            y = str(x)
            z = y[1:len(y)]
            rever = z[::-1]
            solut = int(rever)
            if x >= 2**31 - 1 or x <= -2**31:
                return 0
            else:
                return -solut

        y = str(x)
        rev = y[::-1]
        result = int(rev)
        if x >= 2**31-1 or x <= -2**31:
            return 0
        else:
            return result


s = solution()
a = s.reverse(-123)
z = s.reverse(123)
b = s.reverse(120)
c = s.reverse(0)
d = s.reverse(1534236469)
e = s.reverse(-15633847412)
print(a)
print(b)
print(z)
print(c)
print(d)
print(e)
