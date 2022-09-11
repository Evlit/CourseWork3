# Курсовая работа 3
# Основной модуль запуска представлений
# import logging
from flask import Flask, render_template, request, json, redirect

from api.view_api import api_blueprint
from myutils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user

posts = get_posts_all("data/posts.json")
bookmarks = get_posts_all("data/bookmarks.json")

app = Flask(__name__)
app.register_blueprint(api_blueprint)
# logging.basicConfig(filename='logs/api.log', format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO,
#                     encoding='utf-8')


@app.route("/")
def page_index():
    """
    Деоратор без параметров -вывод всего списка постов
    """
    return render_template('index.html', posts=posts, bookmarks=bookmarks)


@app.route('/posts/<int:postid>')
def get_post(postid):
    """
    Вывод одного поста по номеру
    """
    one_post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template('post.html', post=one_post, comments=comments, bookmarks=bookmarks)


@app.route('/search/')
def search_posts():
    """
    Вывод постов по ключевой фразе
    """
    key_search = request.args.get('s', '')
    posts_search = search_for_posts(key_search)
    return render_template('search.html', posts=posts_search, bookmarks=bookmarks)


@app.route('/tag/<tagname>')
def search_posts_tag(tagname):
    """
    Вывод постов по тэгам
    """
    posts_tag = search_for_posts(tagname)
    return render_template('tag.html', posts=posts_tag, tagname=tagname)


@app.route('/users/<username>')
def get_user_post(username):
    """
    Вывод постов пользователя
    """
    posts_name = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts_name, bookmarks=bookmarks)


@app.errorhandler(404)
def page_not_found(error):
    """
    Обработка ошибки 404 - страница не найдена
    """
    return "<h1>Страница не найдена, ошибка 404</h1>"


@app.errorhandler(500)
def server_err(error):
    """
    Обработка ошибки 500 - внутренняя ошибка сервера
    """
    return "<h1>Внутренняя ошибка сервера 500 </h1>"


@app.route('/bookmarks/add/<int:postid>')
def bookmarks_add(postid):
    """
    Добавление закладки
    """
    one_post = get_post_by_pk(postid)
    bookmarks.append(one_post)
    with open('data/bookmarks.json', 'w', encoding='utf-8') as f:
        json.dump(bookmarks, f)
    return redirect("/", code=302)


@app.route('/bookmarks/remove/<int:postid>')
def bookmarks_remove(postid):
    """
    Удаление закладки
    """
    one_post = get_post_by_pk(postid)
    bookmarks.remove(one_post)
    with open('data/bookmarks.json', 'w', encoding='utf-8') as f:
        json.dump(bookmarks, f)
    return redirect("/", code=302)


@app.route("/bookmarks/")
def page_bookmarks():
    """
    Вывод постов из закладок
    """
    return render_template('bookmarks.html', posts=posts, bookmarks=bookmarks)


if __name__ == '__main__':
    app.run()
