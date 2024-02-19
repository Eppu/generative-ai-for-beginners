from flask import Flask, request

app = Flask(__name__)

# Input validation function
def validate_name(name):
    if not isinstance(name, str):
        return False
    # You can add more validation logic here if needed
    return True

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    
    # Validate the 'name' parameter
    if not validate_name(name):
        return 'Invalid input for name', 400

    return f'Hello, {name}!'

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return 'Not Found', 404

if __name__ == '__main__':
    # Set the application in debug mode for development
    app.config['DEBUG'] = True
    app.run()
