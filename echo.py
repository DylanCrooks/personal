def egho(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    result = ""
    for i in range(min(repetitions, len(text))+1):
        if i == repetitions:
            result += "."
        else:
            result += text[i:] + "\n"
    return result

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(egho(text))
