from logging import DEBUG, debug, CRITICAL, basicConfig, disable
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(CRITICAL)

def parse_args():
    pass

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