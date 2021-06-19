from website import create_app



app = create_app()

def home():
    return "HOME"

if __name__ == '__main__':
    app.run(debug=True)





    