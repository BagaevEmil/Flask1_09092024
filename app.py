from flask import Flask, jsonify,request 
app = Flask(__name__)



about_me = {
"name": "Эмиль",
"surname": "Багаев",
"email": "e.bagaev@mail.ru"
}


@app.route("/") # "это первый  URL который мы будем обрабатывать    "
def hello_world(): # эта функция обработчик будет вызвана при запросе этого URL
    return "Hello, World!"

@app.route("/about")
def about():
    return about_me

@app.route("/quotes", methods=['POST'])
def create_quote():
    data = request.json
    print("data = ", data)
    return {}, 201

    
    

if __name__ == "__main__": # если этот файл запущена как главный модуль тогда мы запускаем приложение вызываем у нее метод run и запускаем его в тч в режиме отладки
    app.run(debug=True)

    from flask import request

