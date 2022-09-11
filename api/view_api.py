import logging
from flask import Blueprint, jsonify
from myutils import get_post_by_pk, get_posts_all


api_blueprint = Blueprint('api_blueprint', __name__)
logging.basicConfig(filename='logs/api.log', format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO,
                    encoding='utf-8')

@api_blueprint.route('/api/posts', methods=['GET'])
def get_posts_json():
    """
    вывод всех постов в формате JSON
    """
    posts = get_posts_all("data/posts.json")
    logging.info('Запрос /api/posts')
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>')
def get_post_json(post_id):
    """
    вывод одного поста в формате JSON
    """
    one_post = get_post_by_pk(post_id)
    if one_post is None:
        logging.error(f'Запрос /api/posts/{post_id} - нет поста с таким номером')
        return "<h1>Нет поста с таким номером</h1>"
    logging.info(f'Запрос /api/posts/{post_id}')
    return jsonify(one_post)
