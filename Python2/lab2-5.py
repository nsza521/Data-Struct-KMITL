class WordGame:
    def __init__(self):
        self.words = []
        self.active = True
        self.is_invalid = False

    def restart(self):
        self.words = []
        self.active = True
        print("game restarted")

    def add_word(self, word):
        word_lower = word.lower()
        if word_lower in (w.lower() for w in self.words):
            print(f"'{word}' is Invalid Input !!!")
            return

        if self.words:
            last_word = self.words[-1].lower()
            if last_word[-2:] != word_lower[:2]:
                print(f"'{word_lower}' -> game over")
                self.active = False
                return
        
        self.words.append(word)
        print(f"'{word}' -> {self.words}")

    def process_command(self, command):
        if not self.active and command[0] != 'R':
            return
        if(self.is_invalid == False):
            if(command[0].islower()):
                print(f"'{command}' is Invalid Input !!!")
                self.is_invalid = True
            elif command[0] == 'P':
                word = command[2:]
                self.add_word(word)
            elif command[0] == 'R':
                self.restart()
            elif command[0] == 'X':
                self.active = False
        

game = WordGame()
print("*** TorKham HanSaa ***")
user_input = input("Enter Input : ")
commands = user_input.split(',')

for command in commands:
    game.process_command(command.strip())