# -*- coding: utf-8 -*-


def head(page = 'other'):
    links = ''
    if page == 'index':
        links = """
        <link href="/style?file=style.css" type="text/css" rel="stylesheet">
        <link href="/style?file=bootstrap.css" type="text/css" rel="stylesheet">
        <link href="/style?file=bootstrap-grid.css"
            type="text/css" rel="stylesheet">
	"""
    head = ("""
    <head>
        <meta charset="utf-8">
        <link href="/style?file=style_v0.css" type="text/css" rel="stylesheet">
        """ + links +
        """
        <script type="text/javascript" 
            src="http://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js">
        </script>
    </head>""")
    return head


def index_html():
    html = ("""
        <html>""" +
            head(page = 'index') + """
            <body>
		<div class="conteiner" id="wrapper">
                    <header>
                        <div class="row" id="nav-panel">
                            <div class="col-1"></div>
                            <div class="col-2"></div>
                            <div class="col-1"></div>
                            <div class="col-5">
                                <a href="/">
                                    <div class="nav-elem">Новости</div>
                                </a>
                                <a href="/cars">
                                    <div class="nav-elem">Машины</div>
                                </a>
                            </div>
                            <div class="col-3"></div>
                        </div>
                        <div class="conteiner" id="main-info">
                            <div class="conteiner title-box">
                                <span id="title">Название</span><br>
                                Слоган...
                            </div>
                        </div>
                    </header>
                    <div class="conteiner" id="middle">
                        <div class="conteiner col-12" id="content">
                            Content
                        </div>
                    </div>
                    <footer>
				S. T. M.
                    </footer>
		</div>
		<!--Scripts-->
		<script type="text/javascript" 
                    src="/scripts?script=nav-panel_changer.js"></script>
	    </body>
        </html>""")
    return html


def menu(title):
    menu = """
            <div class="menu_box">
                <a href="/index"><div class="Menu">Главная</div></a>
                <a href="/news"><div class="Menu">Новости</div></a>
                <a href="/cars"><div class="Menu">Машины</div></a>
                <a href="/profile"><div class="Menu">Профиль</div></a>
            </div>"""    
    if title == 'Главная':
        menu = """
                <div class="menu_box">
                    <a href="/index"><div class="Menu-opened">Главная</div></a>
                    <a href="/news"><div class="Menu">Новости</div></a>
                    <a href="/cars"><div class="Menu">Машины</div></a>
                    <a href="/profile"><div class="Menu">Профиль</div></a>
                </div>"""
    elif title == 'Новости':
        menu = """
                <div class="menu_box">
                    <a href="/index"><div class="Menu">Главная</div></a>
                    <a href="/news"><div class="Menu-opened">Новости</div></a>
                    <a href="/cars"><div class="Menu">Машины</div></a>
                    <a href="/profile"><div class="Menu">Профиль</div></a>
                </div>"""
    elif title == 'Профиль':
        menu = """
                <div class="menu_box">
                    <a href="/index"><div class="Menu">Главная</div></a>
                    <a href="/news"><div class="Menu">Новости</div></a>
                    <a href="/cars"><div class="Menu">Машины</div></a>
                    <a href="/profile"><div class="Menu-opened">Профиль</div></a>
                </div>"""
    elif title == 'Машины':
        menu = """
            <div class="menu_box">
                <a href="/index"><div class="Menu">Главная</div></a>
                <a href="/news"><div class="Menu">Новости</div></a>
                <a href="/cars"><div class="Menu-opened">Машины</div></a>
                <a href="/profile"><div class="Menu">Профиль</div></a>
            </div>"""         
    return menu


def footer():
    footer = """
    <footer class="footer">
            Starodubtsev Timofei<br>
            Copyright &copy; 2017
    </footer> <!-- .footer -->"""
    return footer


def html_all(title, content, right_sidebar, scripts = ''):
    html = ("""
        <html>"""
            + head() + """
            <body>
                <a href="#top"><div class="up"></div></a>
                <div class="wrapper">
                    <header class="header" name="top">
                        <div class="head_block">
                            <div class="logo">
                            </div>"""
                            + menu(title) + """
                        </div>
                    </header> <!-- .header-->
                    <div class="middle">
                        <div class="container">
                            <div class="content">"""
                                + content + """
                        </div>
                        </div><!-- .container-->
                        <div class="right-sidebar">"""
                        + right_sidebar +
                        """</div>
                    </div><!-- .middle-->"""
                    + footer() + """
                </div><!-- .wrapper -->"""
                    + scripts + """
                <script type="text/javascript" 
                    src="scripts?script=captcha_reloader.js">
                </script>
            </body>
        </html>""")
    return html


if __name__ == '__main__':
    print('Это модуль, содержащий html-шаблон сайта')
    input('Для продолэения введите любой символ...')