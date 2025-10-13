import json
import re #Used for cleaning filenames
from datetime import datetime
import os 

def create_post():
    """Gathers input from the user and saves a new blog post."""
    print("\n---Create New Post---")
    title = input("Enter the title here : ").strip()
    author = input("Enter Authors Name : "). strip()
    
    # Simple content input—in a real app, this would be more advanced
    content_lines = []
    print("Enter Post Content (Type : 'END' on a new line to finish)")
    
    while True:
      linee = input()
      
      #Loops Breaks when 'End" is typed
      if linee.strip().upper() == 'END':
        break
      #appends the input in the temporary list
      content_lines.append(linee)
    content = "\n".join(content_lines)  
    
    # 1.Creating the Data Structure:(Dictionary)
    
    post_data = {
        "title": title,
        "author": author,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "content": content
    }
    
    # 2. Prepare the Filename
    # Slugify the title for a clean filename (e.g., "My Post" -> "my-post")
    filename_base = re.sub(r'[^\w]+', '-', title.lower()).strip('-')
    filename = f"posts/{filename_base}.json"
    
    # 3. File I/O: Writing the JSON data to a file
    try:
        # 'w' mode opens the file for writing. If it exists, it's overwritten.
        # `indent=4` makes the JSON file human-readable (pretty-printed).
        with open(filename, 'w') as f:
            json.dump(post_data, f, indent=4)
        print(f"\n✅ Post '{title}' saved successfully to {filename}")
    except IOError as e:
        print(f"❌ Error saving post: {e}")  
        

def view_posts():
  """Reads and displays a summary of all existing blog posts."""
  print("\n--- All Blog Post ---")
  
  # Check if the 'posts' directory exists
  if not os.path.exists('posts'):
        print("No posts found. Create one first!")
        return
  
  post_files = [f for f in os.listdir('posts') if f.endswith('.json')]
  
  if not post_files:
        print("No posts found in the 'posts' directory.")
        return    
   
  # Data Structure (List of Dictionaries) to hold summaries
  all_post_summaries =[]  
  
  for filename in post_files:
    filepath = os.path.join('posts', filename)   
   
  #reading the titles from the files
  try:
    
    with open(filepath , 'r') as f:
      
      post = json.load(f)
      
      all_post_summaries.append({
        "title" : post.get("title" , "No Title"),
        "author": post.get("author" , "Unknown Author"),
        "date": post.get("date" ,"N/A"),
        "filename" : filename
      }
      )      
  except (IOError, json.JSONDecodeError) as e:
    print(f"❌ Error reading or parsing file {filename}: {e}")
            
  if all_post_summaries:
    print(f" Total Posts : {len(all_post_summaries)} ")
    print(f"{'TITLE':<30} | {'AUTHOR':<30} | DATE")
    print("-" * 60)
    for summary in all_post_summaries:
      print(f"{summary['title']:<30} | {summary['author']:<30} | {summary['date']} ") 



def generate_index():
    """Generates a simple index.html file with links to all posts."""
    print("\n--- Generating Index ---")

    post_files = [f for f in os.listdir('posts') if f.endswith('.json')]
    if not post_files:
        print("No posts to generate an index for.")
        return

    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Simple CLI Blog Index</title>
</head>
<body>
    <h1>Blog Posts Index</h1>
    <ul>
"""
    # Loop to read summaries and build the HTML list
    for filename in post_files:
        filepath = os.path.join('posts', filename)
        try:
            with open(filepath, 'r') as f:
                post = json.load(f)
                title = post.get("title", "Untitled Post")
                author = post.get("author", "Unknown")
                date = post.get("date", "N/A")
                
                # Append an <li> tag for each post
                html_content += f'        <li><a href="{filepath}">{title}</a> by {author} on {date}</li>\n'
        except Exception as e:
            print(f"Warning: Could not include {filename} due to error: {e}")

    html_content += """
    </ul>
    <p>Index generated on: %s</p>
</body>
</html>
""" % datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # File I/O: Writing the HTML content
    try:
        # 'w' mode for writing the final index.html file
        with open('index.html', 'w') as f:
            f.write(html_content)
        print("✅ Index generated successfully! Open 'index.html' in your browser.")
    except IOError as e:
        print(f"❌ Error writing index.html: {e}")
 
def remove_post():
    """Lists posts and removes the selected post file from the posts directory."""
    print("\n--- Remove Blog Post ---")
    
    # 1. Check Directory and Get Files (Same as before)
    if not os.path.exists('posts'):
        print("No 'posts' directory found.")
        return

    post_files = [f for f in os.listdir('posts') if f.endswith('.json')]

    if not post_files:
        print("No posts found to remove.")
        return

    # 2. Display Indexed List of Posts (Same as before)
    post_map = {} 
    print("Available Posts:")
    print("-" * 30)
    for i, filename in enumerate(post_files):
        filepath = os.path.join('posts', filename)
        try:
            with open(filepath, 'r') as f:
                post = json.load(f)
                title = post.get("title", "Untitled Post")
                index = i + 1
                post_map[index] = filename 
                print(f"{index}. {title} ({filename})")
        except Exception as e:
            print(f"Warning: Cannot read file {filename}. Skipping. Error: {e}")
            continue

    print("-" * 30)
    
    # 3. Get User Selection (Same as before)
    while True:
        choice = input("Enter the number of the post to remove (or 0 to cancel): ").strip()
        try:
            choice_num = int(choice)
            if choice_num == 0:
                print("Removal cancelled.")
                return
            
            filename_to_delete = post_map.get(choice_num)
            
            if filename_to_delete:
                break
            else:
                print("Invalid number. Please choose from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # 4. Confirmation, File Deletion, and **Index Update**
    filepath_to_delete = os.path.join('posts', filename_to_delete)
    
    confirm = input(f"Are you sure you want to delete '{filename_to_delete}'? (yes/no): ").strip().lower()

    if confirm == 'yes':
        try:
            # Delete the JSON file
            os.remove(filepath_to_delete) 
            print(f"✅ Post '{filename_to_delete}' successfully removed from disk.")
            
            # 💡 AUTOMATICALLY REGENERATE THE INDEX
            generate_index() # Calls the function to rewrite index.html
            
        except OSError as e:
            print(f"❌ Error deleting file {filepath_to_delete}: {e}")
    else:
        print("Removal cancelled by user.") 
               
def print_menu():
    """Displays the main menu options."""
    print("\n==================================")
    print("  Simple CLI Blog Generator")
    print("==================================")
    print("1. Create New Post")
    print("2. View All Posts Summary")
    print("3. Generate Index.html")
    print("4. Remove Blog Post")  # ADDED OPTION
    print("5. Exit")              # OPTION NUMBER SHIFTED
    print("----------------------------------")

def main():
    """The main application loop."""
    os.makedirs('posts', exist_ok=True) 

    while True:
        print_menu()
        # Update the prompt and check range
        choice = input("Enter choice (1-5): ").strip() 

        if choice == '1':
            create_post()
        elif choice == '2':
            view_posts()
        elif choice == '3':
            generate_index()
        elif choice == '4': # NEW HANDLER
            remove_post()
        elif choice == '5': # SHIFTED EXIT
            print("Exiting Blog Generator. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
            
  
          