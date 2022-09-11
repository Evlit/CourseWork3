from run import app

keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_api_posts():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200, "Ошибка при обращении к эндпоинту"
    assert type(response.json) == list, "возвращается не список"
    assert set(response.json[0].keys()) == keys_should_be, "неверный список ключей"


def test_api_one_post():
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200, "Ошибка при обращении к эндпоинту"
    assert type(response.json) == dict, "возвращается не словарь"
    assert set(response.json.keys()) == keys_should_be, "неверный список ключей"

