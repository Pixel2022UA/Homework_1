def parse(query: str) -> dict:
    query = query.split('?')[1] if '?' in query else ''
    params = query.split('&')
    result = {}
    for param in params:
        if param:
            key, value = param.split('=')
            result[key] = value
    return result


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page?name=John&age=30') == {'name': 'John', 'age': '30'}
    assert parse('https://example.com/path/to/page?color=blue&size=large') == {'color': 'blue', 'size': 'large'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&age=2') == {'name': 'ferret',
                                                                                        'color': 'purple', 'age': '2'}
    assert parse('https://example.com/path/to/page?name=Jane&age=25&city=New+York') == {'name': 'Jane', 'age': '25',
                                                                                        'city': 'New+York'}
    assert parse('http://example.com/?name=Tolik&height=190') == {'name': 'Tolik', 'height': '190'}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}