import requests
from bs4 import BeautifulSoup

URL = 'https://results.elections.gov.lk/index.php'
URL_DISTRICT = 'https://results.elections.gov.lk/district_results.php?district={district}'
URL_DIVISION_RESULTS = 'https://results.elections.gov.lk/division_results.php?district={district}&pd_division={division}'


def fetch_overall_results():
    response = requests.get(URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        results_section = soup.find('div', class_='col-lg-4 d-flex flex-column')
        if results_section:
            title_element = results_section.find('h4', class_='card-title card-title-dash')
            title = title_element.get_text(strip=True) if title_element else 'Overall Results'

            result_divs = results_section.select('div.wrapper.d-flex.align-items-center.justify-content-between.py-2.border-bottom')[:5]
            overall_results = []

            for div in result_divs:
                party_abbreviation = div.select_one('div.d-flex.flex-column.align-items-center small').get_text(strip=True)
                candidate_name = div.select_one('div.wrapper.ms-3.w-100 p').get_text(strip=True)
                votes_received = div.select_one('div.d-flex.justify-content-between.align-items-center.mt-1 small.text-muted:nth-of-type(1)').get_text(strip=True)
                percentage = div.select_one('div.d-flex.justify-content-between.align-items-center.mt-1 small.text-muted:nth-of-type(2)').get_text(strip=True)

                overall_results.append({
                    'candidate_name': candidate_name,
                    'party_abbreviation': party_abbreviation,
                    'votes_received': votes_received,
                    'percentage': percentage
                })

            return {'message': title, 'results': overall_results}
        else:
            return {'message': 'Results section not found.'}
    else:
        return {'message': f'Failed to fetch overall results. Status code: {response.status_code}'}

def fetch_election_results():
    response = requests.get(URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title_element = soup.find('h4', class_='card-title card-title-dash')
        title = title_element.get_text(strip=True) if title_element else 'Title not found'

        table_rows = soup.select('table.select-table tbody tr')
        results = []
        for row in table_rows:
            candidate_name = row.select_one('td:nth-child(1) h6').get_text(strip=True)
            party_abbreviation = row.select_one('td:nth-child(2) h6').get_text(strip=True)
            votes_received = row.select_one('td:nth-child(3) p').get_text(strip=True)
            percentage = row.select_one('td:nth-child(4) p').get_text(strip=True)
            results.append({
                'candidate_name': candidate_name,
                'party_abbreviation': party_abbreviation,
                'votes_received': votes_received,
                'percentage': percentage
            })
        return {'message': title, 'results': results}
    else:
        return {'message': 'Failed to fetch the result.'}


def fetch_district_results(district):
    response = requests.get(URL_DISTRICT.format(district=district))
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title_element = soup.find('h4', class_='card-title card-title-dash')
        title = title_element.get_text(strip=True) if title_element else 'Title not found'

        table_rows = soup.select('table.select-table tbody tr')
        results = []
        for row in table_rows:
            candidate_name = row.select_one('td:nth-child(1) h6').get_text(strip=True)
            party_abbreviation = row.select_one('td:nth-child(2) h6').get_text(strip=True)
            votes_received = row.select_one('td:nth-child(3) p').get_text(strip=True)
            percentage = row.select_one('td:nth-child(4) p').get_text(strip=True)
            results.append({
                'candidate_name': candidate_name,
                'party_abbreviation': party_abbreviation,
                'votes_received': votes_received,
                'percentage': percentage
            })
        return {'message': title, 'results': results}
    else:
        return {'message': 'Failed to fetch the result.'}


def fetch_division_results(district, division):
    response = requests.get(URL_DIVISION_RESULTS.format(district=district, division=division))
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title_element = soup.find('h4', class_='card-title card-title-dash')
        title = title_element.get_text(strip=True) if title_element else 'Title not found'

        table_rows = soup.select('table.select-table tbody tr')
        results = []
        for row in table_rows:
            candidate_name = row.select_one('td:nth-child(1) h6').get_text(strip=True)
            party_abbreviation = row.select_one('td:nth-child(2) h6').get_text(strip=True)
            votes_received = row.select_one('td:nth-child(3) p').get_text(strip=True)
            percentage = row.select_one('td:nth-child(4) p').get_text(strip=True)
            results.append({
                'candidate_name': candidate_name,
                'party_abbreviation': party_abbreviation,
                'votes_received': votes_received,
                'percentage': percentage
            })
        return {'message': title, 'results': results}
    else:
        return {'message': 'Failed to fetch the result.'}