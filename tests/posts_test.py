import pytest
from myutils import get_posts_all, get_posts_by_user, get_post_by_pk, search_for_posts

keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


class TestPosts:
    def test_get_posts_all(self):
        """ Проверяем, верный ли список постов возвращается """
        posts = get_posts_all("data/posts.json")
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_posts_by_user(self):
        """ Проверяем, верные ли данные возвращаются при запросе по имени """
        posts = get_posts_by_user('leo')
        assert type(posts) == list, "возвращается не список"
        assert (posts[0]["poster_name"] == 'leo'), "возвращается неправильный кандидат"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_post_by_pk(self):
        """ Проверяем, верный ли кандидат возвращается при запросе одного """
        post = get_post_by_pk(1)
        assert type(post) == dict, "возвращается не словарь"
        assert (post["pk"] == 1), "возвращается неправильный пост"

    def test_get_posts_by_text(self):
        """ Проверяем, верные ли данные возвращаются при запросе по имени """
        posts = search_for_posts('кот')
        assert type(posts) == list, "возвращается не список"
        assert (posts[0]["poster_name"] == 'johnny'), "возвращается неправильный кандидат"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"
