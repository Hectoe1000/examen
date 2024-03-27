from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  return '''
    <html>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
            .card {
                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
                max-width: 300px;
                margin: auto;
                text-align: center;
                font-family: arial;
            }
            /* Resto del estilo aquí */

        </style>
    </head>
    <body>
        <h2 style="text-align:center">User Profile Card</h2>
        <div class="card">
            <img src="https://i.pinimg.com/736x/7f/5e/e2/7f5ee2d0620e9698d7b8c696b1e35ed7.jpg" alt="John" style="width:100%">
            <h1>John Doe</h1>
            <p class="title">CEO & Founder, Example</p>
            <p>Harvard University</p>
            <div style="margin: 24px 0;">
                <a href="#"><i class="fa fa-dribbble"></i></a>
                <a href="#"><i class="fa fa-twitter"></i></a>
                <a href="#"><i class="fa fa-linkedin"></i></a>
                <a href="#"><i class="fa fa-facebook"></i></a>
            </div>
            <p><button>Contact</button></p>
        </div>
    </body>
    </html>
    '''
if __name__== "__main__":
  app.run(debug=True)