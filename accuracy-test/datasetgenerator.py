import nltk
import random
from nltk.corpus import words

# Ensure NLTK words corpus is downloaded
nltk.download('words')

# Load NLTK words corpus
word_list = words.words()

# Function to create a dataset of misspelled words
def create_dataset(num_words):
    dataset = []
    for _ in range(num_words):
        correct_word = random.choice(word_list)
        # Introduce intentional misspelling (e.g., replace one character randomly)
        if len(correct_word) > 1:
            position = random.randint(0, len(correct_word) - 1)
            incorrect_word = (
                correct_word[:position]
                + chr(random.randint(97, 122))  # Random lowercase letter
                + correct_word[position + 1 :]
            )
        else:
            incorrect_word = correct_word + chr(random.randint(97, 122))  # Add a random letter
        dataset.append((correct_word, incorrect_word))
    return dataset

# Function to save dataset to a file
def save_dataset(dataset, file_path):
    with open(file_path, 'w') as file:
        for correct_word, incorrect_word in dataset:
            file.write(f"{correct_word}:{incorrect_word}\n")

# Main function to generate and save the dataset
def main():
    num_words = 10000  # Number of words in the dataset
    dataset = create_dataset(num_words)
    dataset_file = 'dataset.txt'  # File to save the dataset
    save_dataset(dataset, dataset_file)
    print(f"Dataset with {num_words} words generated and saved to {dataset_file}")

if __name__ == "__main__":
    main()
