if __name__ == '__main__':
    obj = NinetyNineBottles2()
    obj.display_intro()
    try:
        obj.main()
    except KeyboardInterrupt:
        exit()