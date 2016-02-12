import base_parser

class CouncillorPhotoParser(BaseParser):
    def parse(self):
        urls = []
        for url in self.soup.findAll('photobigurl'):
            person_name = url.findPrevious('fullusername').text
            person_name = person_name.lower().replace(' ', '-')
            urls.append("{0} {1}.jpg".format(url.text, person_name))
        return urls

if __name__ == "__main__":

    import fnmatch
    import os

    matches = []
    for root, dirnames, filenames in os.walk('data'):
        for filename in fnmatch.filter(filenames, 'CouncillorsByWard.xml'):
            matches.append(os.path.join(root, filename))

    all_urls = []
    for match in matches:
        all_urls.extend(CouncillorPhotoParser(match).parse())
    print('\n'.join(all_urls))
