def main():
    path = "books/frankenstein.txt"
    text = get_book(path)
    words_count = words_counter(path)
    char_count_letters = char_counter_letters(path)   
    char_count_symbols = char_counter_symbols(path)  
    sorted_letters = letter_sorter_by_popularit(char_count_letters)
    generated_report = report_generator(path,words_count,sorted_letters)
    return print(generated_report)

def get_book(path):
    with open(path) as f:
        return f.read()
    
def words_counter(path):
     file = open(path)
     opened_file = file.read()
     words = opened_file.split()
     words_count1 = len(words)
     return words_count1

def char_counter_letters(path):
    file = open(path)
    opened_file = file.read()
    lower_case = opened_file.lower()
    unique_letters ={} 
    for char in lower_case:
        if char.isalpha():
            if char in unique_letters:
                unique_letters[char]+=1
            else:
                unique_letters[char]=1
    return unique_letters
    
def char_counter_symbols(path):
    file = open(path)
    opened_file = file.read()
    lower_case = opened_file.lower()
    unique_char = {}
    for char in lower_case:
        if char in unique_char:
            unique_char[char]+=1
        else:
            unique_char[char]=1
    return unique_char  

def get_count(item):
    return item[1]

def letter_sorter_by_popularit(char_count_letters):
    list_letters = list(char_count_letters.items())
    list_letters.sort(reverse=True,key=get_count)
    return list_letters

def report_generator(path,words_count,sorted_letters):
    report=[]
    report.append(f"--- Begin report of {path} ---")
    report.append(f"{words_count} words found in the document")
    for letter, count in sorted_letters:
        report.append(f"The {letter} character was found {count} times")
    report.append("--- End Report ---")
    return "\n".join(report)

main()
