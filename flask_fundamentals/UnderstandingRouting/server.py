from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return 'Dojo'

# Create a route that responds with "Hi" and whatever name is in the URL after /say/
@app.route('/say/<string:Name>')
def say(Name):
    return f'Hello {Name}'

# Create a route that responds with the given word repeated as many times as specified in the URL
@app.route('/repeat/<int:num>/<string:word>')
def repeatWord(num,word):
    return word*num


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.