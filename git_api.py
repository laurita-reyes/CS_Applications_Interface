import base64
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import config


def git_api():
    owner = "SimplifyJobs"
    repo = "New-Grad-Positions"
    file = "README.md"
    username = 'laurita-reyes'

    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file}"
    r = requests.get(url, auth=(username, config.token))

    response = r.json()
    text = response.get('content')

    # decode text
    decoded_text = base64.b64decode(text).decode('utf-8')
    # print(decoded_text)
    soup = BeautifulSoup(decoded_text, 'html.parser')
    # Parse td's styles
    rows = soup.find_all('tr')
    job_data = []
    for row in rows:
        cols = row.find_all('td')

        if len(cols) >= 5:

            # first <td> is company name
            company = cols[0].get_text(strip=True)
            role = cols[1].get_text(strip=True)  # job title
            location = cols[2].get_text(separator=', ')  # location
            # job link is in td, but within the <a> tag
            link = cols[3].find("a")["href"] if cols[3].find("a") else None
            age = cols[4].get_text(strip=True)  # last <td> is posted date
            job = [company, role, location, link, age]
            print(
                f'company: {company}, role: {role} ,location: {location}, application: {link}, age: {age}\n')
            job_data.append(job)

    df = pd.DataFrame(job_data, columns=[
                      'company', 'role', 'location', 'link', 'age'])
    file_name = 'jobs' + datetime.today().strftime('%Y-%m-%d') + '.csv'
    df.to_csv(file_name, index=False)

    return file_name
