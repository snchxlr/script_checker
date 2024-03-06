import requests
from bs4 import BeautifulSoup

# List of websites to check
websites = ['https://jasonthechiu.com/lr-ats-examples/sso-examples', 'https://anaispirson.github.io', 'https://example.net', 'https://www.gumtree.com.au', 'https://www.news.com.au']

# Scripts you want to check for
scripts_to_check = ['https://ats.rlcdn.com/ats.js', 'https://ats-wrapper.privacymanager.io', 'https://launchpad-wrapper.privacymanager.io']

for website in websites:
    try:
        # Fetch the webpage
        response = requests.get(website)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check if each script is present
        script_tags = soup.find_all('script', src=True)
        present_scripts = [script for script in scripts_to_check if any(script in tag['src'] for tag in script_tags)]

        # Print results
        if present_scripts:
            print(f"The following scripts are present on {website}: {', '.join(present_scripts)}")
        else:
            print(f"None of the scripts are present on {website}")

    except Exception as e:
        print(f"Error checking {website}: {e}")
