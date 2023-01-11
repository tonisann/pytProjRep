"""dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
words = [word for word in dictionary]
print(words)    # ['red', 'blue', 'green']"""


dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
words = [f"{key}: {dictionary[key]}" for key in dictionary]
print(words)    # ['red: красный', 'blue: синий', 'green: зеленый']
