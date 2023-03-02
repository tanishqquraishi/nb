#corpus.py implementation
#discover file, read using read_file and return dataset of training instances consisting of emails with their label
import nltk
#nltk.download('stopwords')
import string
#from nltk.corpus import stopwords
#from nltk import word_tokenize 
import os 



stopwords = stopwords.words('english')
punctuation = string.punctuation

#accepts text as input and returns a list of tokens
def tokenize(text):
    remove_punct = "".join([word.lower() for word in text if word not in punctuation])
    toks = word_tokenize(remove_punct)
    remove_stopwords = [word for word in toks if word not in stopwords]
    return remove_stopwords


#accepts path to text file (email) as input, reads and returns contained text, note:remove "subject"
def read_file(directory1):
    f = open(directory1, 'r', encoding="latin")
    return f.read()

spam_tokens = []
ham_tokens = []

#accepts path to a dataset, should return tuple
def read_dataset(dataset):
    

    train_ham = os.path.join(dataset, "data" , "train", "ham")
    files_in_ham = os.listdir(train_ham)
    train_spam = os.path.join(dataset, "data" , "train", "spam")
    files_in_spam = os.listdir(train_spam)
    
    
    for file_name in files_in_spam: 
        spam = ""
        p = os.path.join(train_spam, file_name)
        content = read_file(p)
        spam += content
        tokenize_content = tokenize(content)
        spam_tokens.extend(tokenize_content)

         

    for file_name in files_in_ham:
        ham = ""
        p = os.path.join(train_ham, file_name)
        content = read_file(p)
        ham += content
        tokenize_content = tokenize(content)
        ham_tokens.extend(tokenize_content)

read_dataset("")


spam_dict = dict( [ (i,spam_tokens.count(i)) for i in set(spam_tokens) ] )
ham_dict = dict( [ (i,ham_tokens.count(i)) for i in set(ham_tokens) ] )

print(spam_dict)
