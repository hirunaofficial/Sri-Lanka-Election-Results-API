import requests
from bs4 import BeautifulSoup

URL = 'https://results.elections.gov.lk/index.php'
URL_DISTRICT = 'https://results.elections.gov.lk/district_results.php?district={district}'
URL_DIVISION_RESULTS = 'https://results.elections.gov.lk/division_results.php?district={district}&pd_division={division}'


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
        return {'title': title, 'results': results}
    else:
        return {'error': 'Failed to fetch the page.'}


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
        return {'title': title, 'results': results}
    else:
        return {'error': 'Failed to fetch the page.'}


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
        return {'title': title, 'results': results}
    else:
        return {'error': 'Failed to fetch the page.'}