class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        op = []

        i = 1
        fizz = 0
        buzz = 0

        while i <= n:
            fizz += 1
            buzz += 1

            if fizz == 3 and buzz == 5:
                op.append("FizzBuzz")
                fizz, buzz = 0, 0
            elif fizz == 3:
                op.append("Fizz")
                fizz = 0
            elif buzz == 5:
                op.append("Buzz")
                buzz = 0
            else:
                op.append(str(i))
            i += 1
        return op