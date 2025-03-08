import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sort_list


def main():
    if len(sys.argv) < 2:  # Check if a file path was provided
        print("Usage:")
        print(f"python {sys.argv[0]} <path_to_file>")
        exit()
    path_to_file = sys.argv[1]
    WC = get_num_words(path_to_file)
    chars = get_num_characters(path_to_file)
    
    try:
        chars_sort = sort_list(chars)
        print("Successfully sorted characters")
    except Exception as e:
        print(f"Error sorting characters: {e}")
        chars_sort = [] 
    
    print(f"""============ BOOKBOT ============
Analyzing book found at {path_to_file}...
----------- Word Count ----------
{WC}
--------- Character Count -------""")

    for char_dict in chars_sort:
        for char, count in char_dict.items():
            if char.isalpha():  # Only print alphabetical characters
                print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()




