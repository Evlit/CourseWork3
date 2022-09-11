import json


POST_PATH1 = "data/comments.json"


def get_posts_all(post_path):
    """
    Функция получения всех постов из файла JSON
    :param post_path:
    """
    with open(post_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_posts_by_user(user_name):
    """
       Поиск поста по имени
    """
    posts = []
    searched_name = False
    for d in get_posts_all("data/posts.json"):
        if user_name.lower() == d['poster_name'].lower():
            posts.append(d)
            searched_name = True
    if searched_name:
        return posts
    raise ValueError('Нет такого пользователя')


def get_comments_by_post_id(post_id):
    """
       Поиск комментария к посту по его номеру
    """
    if get_post_by_pk(post_id) is None:
        raise ValueError('Нет поста с таким номером')
    else:
        with open(POST_PATH1, 'r', encoding='utf-8') as f:
            data = json.load(f)
            comments = []
            for d in data:
                if post_id == d['post_id']:
                    comments.append(d)
    return comments


def search_for_posts(query):
    """
    Фунуция поиска постов по фразе
    """
    posts = []
    for d in get_posts_all("data/posts.json"):
        if query.lower() in d['content'].lower():
            posts.append(d)
    return posts


def get_post_by_pk(pk):
    """
    Функция поиска поста по его номеру
    """
    for d in get_posts_all("data/posts.json"):
        if pk == d['pk']:
            for word in d["content"].split():
                if word[0] == '#':
                    link = f'<a href="/tag/{word[1:]}">{word}</a>'
                    d["content"] = d["content"].replace(word, link, 1)
            return d
