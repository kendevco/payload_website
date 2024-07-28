import os
import sys

print(f"Script is running from: {os.path.abspath(__file__)}")

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"ROOT_DIR is set to: {ROOT_DIR}")

OUTPUT_DIR = os.path.join(ROOT_DIR, 'movie_integration_files')
print(f"OUTPUT_DIR is set to: {OUTPUT_DIR}")

os.makedirs(OUTPUT_DIR, exist_ok=True)
print(f"Created OUTPUT_DIR: {os.path.exists(OUTPUT_DIR)}")

FILES_TO_PROCESS = [
    'src/app/layout.tsx',  # This might be 'app/layout.tsx' if src is not used
    'src/app/movies/page.tsx',
    'src/app/movies/add/page.tsx',
    'src/app/movies/[slug]/page.tsx',
    'src/app/api/movies/search/route.ts',
    'src/app/components/MovieCards.tsx',
    'src/collections/Movies.ts',  # Adjust if your collections are stored elsewhere
    'payload.config.ts',  # This is often in the project root
    'src/components/Header.tsx',  # Adjust if your components are stored elsewhere
]

def read_file(file_path):
    print(f"Attempting to read file: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"Successfully read file: {file_path}")
            return content
    except Exception as e:
        print(f"Error reading file: {file_path}")
        print(f"Error details: {str(e)}")
        return f"Error reading file: {str(e)}"

def write_file(file_name, content):
    output_path = os.path.join(OUTPUT_DIR, file_name)
    print(f"Writing file to: {output_path}")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Successfully wrote file: {output_path}")
    except Exception as e:
        print(f"Error writing file: {output_path}")
        print(f"Error details: {str(e)}")

def process_files():
    for file_path in FILES_TO_PROCESS:
        full_path = os.path.join(ROOT_DIR, file_path)
        print(f"Processing file: {full_path}")
        if os.path.exists(full_path):
            content = read_file(full_path)
            write_file(file_path, content)
            print(f"Processed: {file_path}")
        else:
            print(f"File not found, skipping: {file_path}")
        print("-" * 50)

if __name__ == '__main__':
    print("Starting file processing...")
    process_files()
    print("Processing complete.")
