class Solution:
    def interpret(self, command: str) -> str:
        #return command.replace("()", "o").replace("(al)", "al")
        result = ""
        i = 0

        while i < len(command):
            if command[i] == 'G':
                result += "G"
                i += 1

            elif command[i] == '(' and command[i + 1] == ')':
                result += "o"
                i += 2

            else:
                result += "al"
                i += 4

        return result