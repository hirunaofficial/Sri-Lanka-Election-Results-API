import requests
from bs4 import BeautifulSoup

URL = 'https://results.elections.gov.lk/index.php'
URL_DISTRICT = 'https://results.elections.gov.lk/district_results.php?district=Colombo'
URL_DIVISION_RESULTS = 'https://results.elections.gov.lk/division_results.php?district=Anuradhapura&pd_division=Medawachchiya'

def fetch_election_results():
    response = requests.get(URL)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title_element = soup.find('h4', class_='card-title card-title-dash')
        title = title_element.get_text(strip=True) if title_element else 'Title not found'
        
        print(f"Polling Division Title: {title}\n")
        
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
        
        for result in results:
            print(f"Candidate: {result['candidate_name']}")
            print(f"Party: {result['party_abbreviation']}")
            print(f"Votes: {result['votes_received']}")
            print(f"Percentage: {result['percentage']}\n")
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        
def fetch_division_results():
    response = requests.get(URL_DISTRICT)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title_element = soup.find('h4', class_='card-title card-title-dash')
        title = title_element.get_text(strip=True) if title_element else 'Title not found'
        
        print(f"Polling Division Title: {title}\n")
        
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
        
        for result in results:
            print(f"Candidate: {result['candidate_name']}")
            print(f"Party: {result['party_abbreviation']}")
            print(f"Votes: {result['votes_received']}")
            print(f"Percentage: {result['percentage']}\n")
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        
def fetch_division_results():
    response = requests.get(URL_DIVISION_RESULTS)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extracting title of the division
        title_element = soup.find('h4', class_='card-title card-title-dash')
        title = title_element.get_text(strip=True) if title_element else 'Title not found'
        
        print(f"Division Results Title: {title}\n")
        
        # Extracting the table rows for the division results
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
        
        # Print or return the results
        for result in results:
            print(f"Candidate: {result['candidate_name']}")
            print(f"Party: {result['party_abbreviation']}")
            print(f"Votes: {result['votes_received']}")
            print(f"Percentage: {result['percentage']}\n")
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")

fetch_election_results()
fetch_division_results()
fetch_division_results()