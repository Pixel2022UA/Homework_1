def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    my_dict = {}
    if query:
        for elem in query.split(';'):
            key_value = elem.split('=', maxsplit=1)
            if len(key_value) == 2:
                key, value = key_value
                value_parts = value.split('=')
                if len(value_parts) > 1:
                    value = '='.join(value_parts)
                my_dict[key] = value
    return my_dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima;name=Vasya;') == {'name': 'Vasya'}
    assert parse_cookie('name=Dima;name=Vasya;name=Kolya;') == {'name': 'Kolya'}
    assert parse_cookie('name=Dima;age=28;city=Odessa') == {'name': 'Dima', 'age': '28', 'city': 'Odessa'}
    assert parse_cookie('name=Dima=User=Test;age=28;') == {'name': 'Dima=User=Test', 'age': '28'}
    assert parse_cookie('name=Dima;age=28;city=Kyiv;') == {'name': 'Dima', 'age': '28', 'city': 'Kyiv'}
    assert parse_cookie('name=Dima;age=15;city=Paris;city=Berlin;') == {'name': 'Dima', 'age': '15', 'city': 'Berlin'}