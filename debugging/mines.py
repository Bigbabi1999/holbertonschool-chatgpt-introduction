def check_win(self):
    revealed_count = sum(row.count(True) for row in self.revealed)
    total_safe_cells = self.width * self.height - len(self.mines)
    return revealed_count == total_safe_cells

def play(self):
    while True:
        self.print_board()
        try:
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))
            if not self.reveal(x, y):
                self.print_board(reveal=True)
                print("Game Over! You hit a mine.")
                break

            # 🌟 Check for win here
            if self.check_win():
                self.print_board(reveal=True)
                print("Congratulations! You cleared all safe cells!")
                break

        except ValueError:
            print("Invalid input. Please enter numbers only.")