import re
from pattern import arabic_patterns, english_patterns

class Eliza:
    def __init__(self):
        self.name = "Eliza"
        self.patterns = None
        self.language = None

    def choose_lang(self):
        print("Choose a Language | اختر اللغة")
        print("1. العربية")
        print("2. English")
        
        choice = input("> ")
        if choice == "1":
            self.language = "arabic"
            self.patterns = arabic_patterns
            print("تم اختيار اللغة العربية")
        elif choice == "2":
            self.language = "english"
            self.patterns = english_patterns
            print("English Language Selected")
        else:
            print("Try again | حاول مره اخرى")
            self.choose_lang()

    def user_input(self):
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "bye", "get lost", 
                    "مع السلامة", "مع السلامه", "سلام",]:
                print("Eliza: الله معك, وبتمنّالك يوم سعيد")
                break
            print("Eliza:", self.response(user_input))

    def response(self, user_input):
        for pattern, response in self.patterns:
            match = re.search(pattern, user_input, flags=re.IGNORECASE)
            if match:
                return re.sub(pattern, response, user_input, flags=re.IGNORECASE)
        return "أخبرني بالمزيد عن مشاعرك" if self.language == "arabic" else \
                                            "Tell me more about your feelings."

def main():
    eliza = Eliza()
    eliza.choose_lang()
    eliza.user_input()

if __name__ == "__main__":
    main()
