from mongoengine import connect, Q
from models import Author, Quote
from mongo_connect import connect

def search_quotes_by_author(author_name):

    author = Author.objects(fullname=author_name).first()
    if not author:
        return f"No quotes found for author '{author_name}'."
    
    quotes = Quote.objects(author=author)
    return [quote.quote for quote in quotes]

def search_quotes_by_tag(tag):

    quotes = Quote.objects(tags=tag)
    if not quotes:
        return f"No quotes found for tag '{tag}'."
    
    return [quote.quote for quote in quotes]

def search_quotes_by_tags(tags):

    tags_list = tags.split(',')
    quotes = Quote.objects(Q(tags__in=tags_list))
    
    if not quotes:
        return f"No quotes found for tags '{tags}'."
    
    return [quote.quote for quote in quotes]

def main():

    while True:
        user_input = input("Enter command (format: command:value): ").strip()
        
        if user_input.lower() == 'exit':
            print("Exiting the script. Goodbye!")
            break
        
        try:
            command, value = user_input.split(":", 1)
            command = command.strip().lower()
            value = value.strip()
            
            if command == 'name':
                results = search_quotes_by_author(value)
            elif command == 'tag':
                results = search_quotes_by_tag(value)
            elif command == 'tags':
                results = search_quotes_by_tags(value)
            else:
                print("Unknown command. Please use 'name', 'tag', 'tags', or 'exit'.")
                continue


            if isinstance(results, list):
                for result in results:
                    print(result.encode('utf-8'))
            else:
                print(results.encode('utf-8'))

        except ValueError:
            print("Invalid input format. Please use the format command:value.")

if __name__ == "__main__":
    main()
