

def main():
    args = parse_args()
    if args['product']:
        response = get_search_response(args['product'])
        links = get_links(response)
        debug(links)
        for link in links:
            open(f'https://amazon.in{link}')

if __name__ == '__main__':
    main()