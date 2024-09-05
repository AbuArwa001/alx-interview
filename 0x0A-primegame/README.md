# Prime Game

# Prime Game

🎮 **Description**

Maria and Ben are playing a game with a set of consecutive integers starting from 1 up to and including `n`. They take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game. Maria always goes first, and both players play optimally. This program determines the winner of each game and returns the name of the player who won the most rounds.

📝 **Prototype**

```python
def isWinner(x, nums):
    """
    Determines the winner of each game and returns the name of the player
    who won the most rounds.

    Parameters:
    x (int): The number of rounds.
    numbers (list): An array of integers representing the value of n for each round.

    Returns:
    str: The name of the player that won the most rounds ("Maria" or "Ben").
         If the winner cannot be determined, None.
    """
```

🔍 **Explanation**

First round (n = 4):

- Maria picks 2 and removes 2, 4, leaving 1, 3.
- Ben picks 3 and removes 3, leaving 1.
- Ben wins because there are no prime numbers left for Maria to choose.

Second round (n = 5):

- Maria picks 2 and removes 2, 4, leaving 1, 3, 5.
- Ben picks 3 and removes 3, leaving 1, 5.
- Maria picks 5 and removes 5, leaving 1.
- Maria wins because there are no prime numbers left for Ben to choose.

Third round (n = 1):

- Ben wins because there are no prime numbers for Maria to choose.

Maria wins 2 rounds, and Ben wins 1 round. Therefore, the function returns "Maria".

📥 **Installation**

No installation is required as this is a standalone Python function. Ensure you have Python installed on your system.

💻 **Usage**

1. Copy the `isWinner` function into your Python script.
2. Call the function with the appropriate parameters.

📄 **License**

This project is licensed under the MIT License. See the LICENSE file for details.
