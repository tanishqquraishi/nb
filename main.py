#main.py implementation 
#user friendly interface to detect spam/ ham email 
#should provide the user with instructions
#baseline func- user can train spam classifier
#Batch classify the test dataset and output the filename, the predicted spam score and classification result to a file


    # The implementation of the SpamFilter class is the same as in the previous answer.
import corpus
from nb import SpamFilter
from corpus import read_dataset
def main():
    print("Welcome to the Spam Filter!")
    print("1. Train the classifier")
    print("2. Batch classify emails")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        spam_filter = SpamFilter()
        print("Enter the text of the email and the label (spam/ham).")
        print("Enter an empty line to finish training.")
        while True:
            text = input("Text: ")
            if text == "":
                break
            category = input("Category: ")
            spam_filter.train(text, category)
    elif choice == "2":
        test_dataset_path = input("Enter the path to the test dataset: ")
        output_file_path = input("Enter the path to the output file: ")
        with open(output_file_path, 'w') as output_file:
            output_file.write("Filename\tSpam Score\tClassification\n")
            for filename, text in read_dataset(test_dataset_path):
                score = spam_filter.predict_proba(text)[0][1]
                result = spam_filter.classify(text)
                output_file.write(f"{filename}\t{score}\t{result}\n")
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    main()
