import frontmatter

def main():
    filename = 'test.md'
    with open('DEMO-README.txt', 'w') as readme:
        faq = frontmatter.load(filename)
        owners = '|'.join([str(x) for x in faq.get('owners')])
        published = faq.get('datetime').get('published')
        # print(published)
        readme.write('''
        |owners|published|filename|
        |----|----|----|
        ''')
        readme.write('|{}|{}|{}|'.format(owners,published, filename))
        readme.close()


if __name__ == "__main__":
    main()