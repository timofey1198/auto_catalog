# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import escape
from content import html_all, index_html
import data
import auto_data
import os

app = Flask(__name__)
app.secret_key = 'd&hnkj;84H(Ffn97@)#38rf3c7uhf39^&@Tb8'

def valid_login(login, password):
    return ((data.is_password(login, password)))


@app.route("/login", methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['login'],
                       request.form['password']):
            session['login'] = request.form['login']
            return profile()
        else:
            error = 'error!!!'
    return index()

@app.route("/reg", methods=['POST', 'GET'])
def reg():
    if request.method == 'POST':
        if session['key'] == request.form['captcha']:
            user = request.form['login']
            password = request.form['password']
            if(not data.is_user(user)):
                data.new_user(user, password)
                return index()
    return register()

@app.route("/logout", methods=['POST', 'GET'])
def logout():
    session.pop('login', None)
    return index()

def login_form():
    if 'login' in session:
        login_form = ('<div class="enter_form">Hi, %s' 
                   % escape(session['login']) +
                   """
                    <br><br>
                    <a href="/logout">
                    <div class="button">Выйти</div>
                    </a>
                    </div>
                """)
    else:
        login_form = """
            <div class="enter_form">
                <form action="/login" method="POST">
                    <input type="text" name="login">
                    <input type="password" name="password">
                    <input type="submit" value="Войти">
                </form>
                <br>
                <a href="/register">
                <div class="button">Регистрация</div>
                </a>
            </div>
            """
    return login_form

def page_not_found_error():
    html = """
        <html>
            <body>
                <center>
                    <h1>Страница не найдена...</h1><br>
                    <a href="index">На главную</a>
                </center>
            </body>
        </html>
        """
    return html


@app.route("/news_handler", methods=['POST', 'GET'])
def news_handler():
    if request.method == 'POST':
        title = request.form['news_title']
        body = request.form['news_text']
        author = session['login']
        data.new_article(title, body, author)
        return redirect(url_for("news"))
    return redirect(url_for("edit"))

#------------------------------------PAGES--------------------------------------

@app.route("/")
@app.route("/index")
def index():
    content = '<br>'
    right_sidebar = login_form()
    return index_html()


@app.route("/register")
def register():
    content = """
            <div class="enter_form">
                <form action="/reg" method="POST">
                    <input type="text" name="login" required placeholder="Логин"><br>
                    <input type="password" name="password" required placeholder="Пароль"><br><br>
                    <img src="/captcha"><br><br>
                    <input type="text" name="captcha" required placeholder="Введите текст с картинки"><br>
                    <input type="submit" value="Регистрация">
                </form>
            </div>
            """
    return html_all('Регистрация', content, '')

@app.route("/news")
def news():
    edit = ''
    if 'login' in session:
        user = session['login']
        if data.is_access(user, 0):
            edit = """
                <div class="header_block">
                <center><a href="edit">
                    <div class="add_new">Добавить новость</div>
                </a><center>
                </div>
            """
    news = ''
    files = os.listdir(path = 'pages/news')
    files.sort(key=lambda x: -int(x.split('.')[0]))
    for name in files:
        f = open('pages/news/' + name, 'r', encoding='utf-8')
        text = f.read()
        text = text.replace('\n', '<br>')
        f.close()
        number = int(name.split('.')[0])
        info = data.get_articles_info(number)
        title = info[1]
        author = info[3]
        flag = False
        if 'login' in session:
            user = session['login']
            if data.is_access(user, 0):
                flag = True
            if data.is_access(user, 1) and user == author:
                flag = True
        delete = ''
        if flag:
            delete = """
                <form action="news/delete" method="POST">
                <input type="hidden" name="article_id" value="%s">
                <input type="submit" value="Удалить запись" style="
                        background: inherit;
                        border: 0px;
                        color: red;
                        cursor: pointer;
                        ">
                </form>
            """%str(number)
        article = """
            <div class="news">
                <h3>%s</h3>
                <p>%s</p>
                <form action="news/article" method="POST">
                <input type="hidden" name="article_id" value="%s">
                <input type="submit" value="Подробнее" style="
                        background: inherit;
                        border: 0px;
                        color: blue;
                        cursor: pointer;
                        ">
                </form>
                %s
                <br>
                <i>Автор: %s</i>
                <br><br>
                <hr>
            </div>
        """%(title, text, str(number), delete, author)
        news += article
    content = edit + news
    right_sidebar = login_form() 
    return html_all('Новости', content, right_sidebar)


@app.route("/news/article", methods=['POST', 'GET'])
def article():
    if request.method == 'POST':
        number = request.form['article_id']
        info = data.get_articles_info(int(number))
        title = info[1]
        author = info[3]
        path = 'pages/news/%s.txt'%info[2]
        f = open(path, 'r', encoding='utf-8')
        text = f.read()
        text.replace('\n', '<br>')
        html = """
            <div class="news">
                <h3>%s</h3>
                <p>%s</p>
                <br>
                <i>Автор: %s</i>
                <br><br>
            </div>
        """%(title, text, author)
        menu = """
                <div class="menu_box">
                    <a href="/index"><div class="Menu">Главная</div></a>
                    <a href="/news"><div class="Menu">Новости</div></a>
                </div>
                    """        
        return html_all(menu, html, '')
    else:
        return redirect(url_for("news"))


@app.route("/contacts")
def contacts():
    return page_not_found_error()


@app.route("/edit")
def edit():
    menu = """
                <div class="menu_box">
                    <a href="index"><div class="Menu">Главная</div></a>
                    <a href="news"><div class="Menu">Новости</div></a>
                    <a href="profile"><div class="Menu">Профиль</div></a>
                </div>"""
    content = """
        <div class="news">
            <form action="/news_handler" method="POST">
                <input type="text" name="news_title" value="Заголовок"><br>
                <textarea name="news_text" value="введите текст новости" 
                  style="
                  width: 500px;
                  height: 400px;
                  text-align: left;
                  "></textarea><br>
                <input type="submit" value="Создать">
            </form>
        </div>
    """
    return html_all(menu, content, '')


@app.route("/news/delete")
def delete():
    number = request.form['article_id']
    data.delete_article(number) # Удалена запись из базы
    # Тут нужно удалить файл или
    # переместить его в "корзину сайта"


@app.route("/cars", methods = ['GET'])
def cars(**kwargs):
    # Вывод страницы с отдельной машиной
    if 'car' in request.values:
        car_id = request.values['car']
        firm, model = auto_data.get_main_info(car_id)
        if firm != None:
            content = firm
            return html_all('Машины', content, '')
    
    new_car_status = ''
    if 'new_car_status' in kwargs:
        new_car_status = kwargs['new_car_status'] + '<br>'
    content = ''
    
    # Вывод списка машин из базы
    for car_dict in auto_data.get_cars():
        car_html = auto_data.car_info_to_html(car_dict)
        content += car_html
    
    if 'login' in session:
        if session['login'] == 'admin':
            content = (new_car_status + '<a href="new_car">' +
                       '<div class="button">Добавить машину</div></a>'
                      + content)
    return html_all('Машины', content, '')


@app.route("/new_car")
def new_car(**kwargs):
    error = ''
    if 'error' in kwargs:
        if kwargs['error'] == 'captcha':
            error = """
                    <div class="error">
                        Неправильно введен код с картинки<br>
                    </div>
                    """
        else:
            error = '<div class="error">%s<br></div>'%kwargs['error']

    form = ("""
        <form action="new_car_handler" method="POST">
            <b>Общие</b><br>
            Фирма<br>
            <input type="text" name="firm"
                   required><br>
            Модель<br>
            <input type="text" name="model"
                   required><br>
            Цена<br>
            <input type="text" name="price" 
                   pattern="[1-9]{1}[0-9]{0,10}"><br>
            <hr><br>
            <b>Двигатель</b><br>
            Тип<br>
            <input type="text" name="engine_type"
                   ><br>
            Объем<br>
            <input type="text" name="engine_volume"  
                   pattern="[1-9]{1}[0-9]{0,4}"><br>
            Мощность<br>
            <input type="text" name="engine_power"  
                   pattern="[1-9]{1}[0-9]{0,3}"><br>
            Момент<br>
            <input type="text" name="engine_moment"  
                   pattern="[1-9]{1}[0-9]{0,4}"><br>
            Расход топлива (официальный)<br>
            <input type="text" name="engine_fuel_consumption_dealer" 
                   pattern="[1-9]{1}[0-9]{0,1}[,]{0,1}[0-9]{0,3}"><br>
            <hr><br>
            <b>Дополнительно</b><br>
            Транспортный налог<br>
            <input type="text" name="transport_tax" 
                   pattern="[1-9]{1}[0-9]{0,3}"><br>
            Дополнительные расходы<br>
            <input type="text" name="user_defined_expense"><br>""" + 
            #<img src="/captcha" id="captcha_img">
            #<input type="button" id="captcha_new" value="Reload">
            """<br><br>
            <input type="text" name="captcha" 
                   placeholder="Введите текст с картинки"><br>
            <input type="submit" value="Добавить">
        </form>
           """)
    content = '<div class="news">' + error + form + '</div>'
    return html_all('Машины', content, '')


@app.route("/new_car_handler", methods = ['POST'])
def new_car_handler():
    if request.method == 'POST':
        if True: #session['key'] == request.form['captcha']:
            
            firm = request.form['firm']
            model = request.form['model']
            price = request.form['price']
            engine_type = request.form['engine_type']
            engine_volume = request.form['engine_volume']
            engine_power = request.form['engine_power']
            engine_moment = request.form['engine_moment']
            engine_fuel_consumption_dealer =\
                request.form['engine_fuel_consumption_dealer']
            transport_tax = request.form['transport_tax']
            user_defined_expense = request.form['user_defined_expense']
            
            try:
                # Тут проходит верификация данных (auto_data.new_car)
                auto_data.new_car(firm, model, price, engine_type,
                        engine_volume, engine_power, engine_moment,
                        engine_fuel_consumption_dealer, transport_tax,
                        user_defined_expense)
            except ValueError as e:
                return new_car(error = e)
            
            return cars(new_car_status = 'ok')
        return new_car(error = 'captcha')
    return redirect(url_for("new_car"))


@app.route("/profile")
def profile():   
    if 'login' in session:
        content = ('<div class="content">Logged in as %s</div>' 
                   % escape(session['login']))
    else:
        content = '<div class="content">You are not logged in</div>'
    return html_all('Профиль', content, '')


#---------------------------------RESOURCES------------------------------------

@app.route("/scripts", methods = ['GET'])
def sctipts():
    if 'script' in request.values:
        asking_script = request.values['script']
        script_files = os.listdir(path = 'resources/scripts')
        if asking_script in script_files:
            f = open('resources/scripts/%s' % asking_script, 'r')
            return f.read()
        return ''
    return ''


@app.route("/style", methods = ['GET'])
def style():
    if 'file' in request.values:
        asking_script = request.values['file']
        script_files = os.listdir(path = 'resources/style')
        if asking_script in script_files:
            f = open('resources/style/%s' % asking_script, 'r')
            return f.read()
        return ''
    return ''


@app.route("/img", methods = ['GET'])
def img():
    if 'file' in request.values:
        asking_file = request.values['file']
        script_files = os.listdir(path = 'resources/img')
        if asking_file in script_files:
            f = open('resources/img/%s' % asking_file, 'rb')
            return f.read()
        return ''
    return ''


@app.route("/img/top")
def top():
    img = open('resources/img/top.png', 'rb')
    return img.read()

@app.route("/captcha")
def captcha():
    key = data.captcha()
    if 'key' in session:
        name = session['key']
        try:
            os.remove('resources/img/captcha/%s.jpg' % name)
        except:
            pass
    session['key'] = key
    img = open('resources/img/captcha/%s.jpg' %key, 'rb')
    return img.read()


if __name__ == "__main__":
    app.run()