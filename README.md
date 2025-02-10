# lead_scraper

```markdown
# Real Estate Lead Scraper

This Python script automates the process of generating real estate leads by:
1. Searching for relevant websites using Bing.
2. Scraping essential information like company names, emails, and project details.
3. Saving the data into a CSV file.
4. Sending a test email with the scraped data.

## Features
- **Search Bing**: Automatically queries Bing with a specified search phrase and retrieves a list of URLs.
- **Data Scraping**: Extracts company names, emails, project names, and URLs from the retrieved websites.
- **CSV Export**: Saves the scraped data in a structured CSV format.
- **Email Integration**: Sends a test email showcasing the scraped data.

## Requirements
- Python 3.x
- `requests` library
- `BeautifulSoup` from `bs4`
- `csv` (built-in)
- `smtplib` (built-in)

## Installation
1. Clone or download this repository.
2. Install dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage
### 1. Run the Script
- Update the `search_query` variable with your search term (e.g., `"Real estate developers Germany new construction projects"`).
- Execute the script:
  ```bash
  python real_estate_scraper.py
  ```

### 2. Steps Performed:
- **Search Bing**: Searches Bing with the query and retrieves the top URLs.
- **Scrape Data**: Extracts relevant details from each website.
- **Save Data**: Saves the scraped data into `scraped_real_estate_data.csv`.

### 3. Load Data
The function `load_scraped_data()` can load previously scraped data from the CSV file:
```python
data = load_scraped_data()
```

### 4. Send Test Email
The `send_test_email()` function sends an email with the first result:
```python
send_test_email(data)
```

## SMTP Configuration
Update the following parameters in the `send_test_email` function:
- `smtp_server`: Your email provider's SMTP server (e.g., `smtp.gmail.com`).
- `smtp_port`: Port number for the SMTP server (e.g., `587`).
- `sender_email`: Your email address.
- `sender_password`: Your email password or app-specific password.
- `recipient_email`: The recipient's email address.

## CSV Output Format
The CSV file (`scraped_real_estate_data.csv`) contains:
- `Company Name`: The title of the webpage or "N/A" if not available.
- `Email`: The first email found on the page or "N/A" if not found.
- `Project Name`: The main `<h1>` text or "N/A" if not available.
- `URL`: The scraped URL.

## Notes
- Ensure your email provider allows SMTP connections.
- Handle errors gracefully, such as failed connections or missing data.

## Example
### Sample Search Query
```python
search_query = "Real estate developers Germany new construction projects"
```

### Sample Output
CSV File:
```csv
Company Name,Email,Project Name,URL
"Developer ABC","info@developerabc.com","Luxury Apartments","https://www.developerabc.com"
...
```

### Sample Email Body
```plaintext
Hallo Team,

Dies ist ein Test-E-Mail für den Cold Outreach. Hier sind einige der gescrapten Daten:

Developer ABC - info@developerabc.com
Projekt: Luxury Apartments
URL: https://www.developerabc.com

Vielen Dank,
Ihr Testsystem
```

## Disclaimer
This script is intended for educational purposes only. Ensure compliance with data privacy regulations (e.g., GDPR) and website terms of service when scraping data.

## License
MIT License
```
