# -*- coding: utf-8 -*-


def head():
    head = """
    <head>
        <meta charset="utf-8">
        <link href="/style" type="text/css" rel="stylesheet">
        <script type="text/javascript" 
        src="http://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js">
        </script>
    </head>"""
    return head


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


def html_all(title, content, right_sidebar):
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
                </div><!-- .wrapper -->
                <script type="text/javascript">
                    $(document).ready(function(){
                        function captcha_new(){
                            $("#captcha_img").attr("src", "/captcha?q=" + 
                                                   Math.random());
                        } 
                        
                        $("#captcha_new").click(captcha_new);
                    });
                </script>
            </body>
        </html>""")
    return html


if __name__ == '__main__':
    print('Это модуль, содержащий html-шаблон сайта')
    input('Для продолэения введите любой символ...')