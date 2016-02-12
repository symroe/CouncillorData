import sys
import csv

import base_parser

class StandingDownParser(base_parser.BaseParser):

    def parse(self):
        all_data = []
        for date in self.soup.findAll('enddate'):
            councillor = date.findParent('councillor')
            councillor_name = councillor.find('fullusername').text
            councillor_id = councillor.find('councillorid').text
            councillor_party = councillor.find('politicalpartytitle').text
            councillor_representing = councillor.find('representing').text
            councillor_email = councillor.find('email')
            if councillor_email:
                councillor_email = councillor_email.text
            else:
                councillor_email = ""
            if date.text.strip() != "unspecified":
                all_data.append([
                    date.text.strip(),
                    councillor_name.strip(),
                    councillor_id.strip(),
                    councillor_party.strip(),
                    councillor_representing.strip(),
                    councillor_email.strip(),
                ])
        return all_data




if __name__ == "__main__":

    import fnmatch
    import os

    matches = []
    for root, dirnames, filenames in os.walk('data'):
        for filename in fnmatch.filter(filenames, 'CouncillorsByWard.xml'):
            matches.append(os.path.join(root, filename))

    all_urls = []
    out_file = csv.writer(sys.stdout)
    for match in matches:
        data = StandingDownParser(match).parse()
        if data:
            out_file.writerows(data)
            # print(data)

