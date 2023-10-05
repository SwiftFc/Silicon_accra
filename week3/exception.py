class Division:
    def divide(self, num,deno):
        try:
            result = num /deno
        except (ZeroDivisionError, TypeError) as e:
            print(f" Invalid {e}")

        except SyntaxError:
            print("Syntax Error")
        else:
            print(f" result is {result}")
