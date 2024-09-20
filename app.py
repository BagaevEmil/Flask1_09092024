from flask import Flask, jsonify,request 
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False; 

about_me = {
"name": "Эмиль",
"surname": "Багаев",
"email": "e.bagaev@mail.ru"
}

quotes = [
   {
       "id": 3,
       "author": "Rick Cook",
       "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает."
   },
   {
       "id": 5,
       "author": "Waldi Ravens",
       "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей с острыми бритвами в руках."
   },
   {
       "id": 6,
       "author": "Mosher’s Law of Software Engineering",
       "text": "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили."
   },
   {
       "id": 8,
       "author": "Yoggi Berra",
       "text": "В теории, теория и практика неразделимы. На практике это не так."
   },

]


@app.route("/") # "это первый  URL который мы будем обрабатывать    "
def hello_world(): # эта функция обработчик будет вызвана при запросе этого URL
    return jsonify(data="Hello, World!"),200

@app.route("/about")
def about():
    return jsonify(about_me),200 # можно для явности дописывать jsonify и статус ответа 200 


# URL/quotes
@app.route("/quotes")
def get_quotes():
    """Функция неявно преобразовывает список словарей в JSON"""
    return quotes


# URL/quotes
"""
@app.route("/quotes", methods=['POST'])
def create_quote():
    data = request.json
    print("data = ", data)
    return {}, 201
"""


    

if __name__ == "__main__": # если этот файл запущена как главный модуль тогда мы запускаем приложение вызываем у нее метод run и запускаем его в тч в режиме отладки
    app.run(debug=True)

    from flask import request

