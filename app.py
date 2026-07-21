from flask import Flask
import os
 
app = Flask(__name__)
 
# Simple in-memory counter (resets on restart)
visits = 0
 
@app.route('/')
def index():
    global visits
    visits += 1
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Visitor Counter</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }}
            .counter {{ font-size: 48px; color: #2c3e50; }}
        </style>
    </head>
    <body>
                <h1>🚀 Welcome to the Real-World DevOps App!</h1>
        <h2>Warmest of welcomes from our side</h2>
        <p>This page has been visited:</p>
        <div class="counter">{visits} times</div>
        <p><i>Powered by Python, Docker, and GitHub Actions.</i></p>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
