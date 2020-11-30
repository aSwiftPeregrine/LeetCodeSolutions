def defangIPaddr(address: str) -> str:
        result = ""
        for c in address:
            if c == ".":
                result = result + "[.]"
            else:
                result = result + c
        return result

print(defangIPaddr("192.168.55.3"))