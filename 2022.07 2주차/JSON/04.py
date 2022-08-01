import json
from pprint import pprint

with open('./data/movie.json', 'r', encoding='utf-8') as f:
    cho_movie = json.load(f)


def movie_info(movie):
    pass
    # 여기에 코드를 작성합니다.
    movie_dict = {}
    movie_dict['genre_ids'] = cho_movie['genre_ids']
    movie_dict['id'] = cho_movie['id']
    movie_dict['overview'] = cho_movie['overview']
    movie_dict['title'] = cho_movie['title']
    movie_dict['vote_average'] = cho_movie['vote_average']
    return movie_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    pprint(movie_info(movie))
