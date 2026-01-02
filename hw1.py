class reverse:
    def __init__(self, s):
        self.s = s

    def get_reversed_string(self):
        return self.s[::-1]
user_input = input("Enter a word to reverse: ")
reverser_instance = reverse(user_input)

reversed_word = reverser_instance.get_reversed_string()
print("The original word is: ",user_input)
print("The reversed word is: ",reversed_word)
