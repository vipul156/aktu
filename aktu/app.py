from flask import Flask, render_template

app = Flask(__name__)

def get_links_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            links = file.readlines()
            links = [link.strip() for link in links]
            return links
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

@app.route('/')
def index():
    file_path = 'link.txt'  # Change this to the path of your text file
    links = get_links_from_file(file_path)
    return render_template('index.html', links=links)

if __name__ == '__main__':
    app.run(debug=True)
