import argparse

MURZIK = '=^._.^=_____/'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Вежливый скрипт')
    # Добавление позиционного аргумента для имени.
    parser.add_argument('name', help='Имя')
    # Добавление именованного аргумента для фамилии.
    parser.add_argument('-s', '--surname', help='Фамилия')
    # Добавление именованного аргумента с параметром выбора choices.
    parser.add_argument(
        '-c', '--city', help='Город',
        choices=['Chekhov', 'Dublin', 'Minsk', 'Simbirsk']
    )
    # Добавление именованного аргумента с параметром действия action.
    parser.add_argument(
        '-m', '--murzik', action='store_true',
        help=f'Отправить кота Мурзика {MURZIK}'
    )

    args = parser.parse_args()
    parts = []
    parts.append(f'Hello, {args.name}')
    if args.surname is not None:
        parts.append(args.surname)
    if args.city is not None:
        parts.append(f'from {args.city}')
    if args.murzik:
        parts.append(MURZIK)
    print(*parts)
