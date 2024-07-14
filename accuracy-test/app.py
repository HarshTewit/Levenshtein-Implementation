import nltk
from nltk.corpus import words

# Ensure NLTK words corpus is downloaded
nltk.download('words')


# Function to load dataset from file
def load_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as file:
        for line in file:
            correct_word, incorrect_word = line.strip().split(':')
            dataset.append((correct_word.strip(), incorrect_word.strip()))
    return dataset


# Function to perform spell checking
def spell_check(correct_word, incorrect_word):
    # Placeholder logic, replace with your actual spell checking algorithm
    if incorrect_word in words.words():
        return incorrect_word
    else:
        return correct_word  # Replace with your actual correction logic


# Function to calculate accuracy
def calculate_accuracy(dataset):
    correct_predictions = 0
    total_words = len(dataset)

    for correct_word, incorrect_word in dataset:
        corrected_word = spell_check(correct_word, incorrect_word)
        if corrected_word == correct_word:
            correct_predictions += 1

    accuracy = (correct_predictions / total_words) * 100
    return accuracy, total_words  # Return both accuracy and total_words


# Main function to run the spell checker on a dataset
def main(dataset_file):
    dataset = load_dataset(dataset_file)
    accuracy, total_words = calculate_accuracy(dataset)  # Get accuracy and total_words

    print(f"Spell Checker Accuracy: {accuracy:.2f}% on dataset of {total_words} words")


if __name__ == "__main__":
    dataset_file = 'dataset.txt'  # Replace with your dataset file path
    main(dataset_file)
