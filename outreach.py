# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 08:51:18 2025

@author: CSO-II
"""
import requests
from bs4 import BeautifulSoup
import csv
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def search_bing(query, num_results=20):
    """Search Bing for the given query and return a list of URLs."""
    print(f"Searching Bing for: {query}")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    search_url = f"https://www.bing.com/search?q={query.replace(' ', '+')}&count={num_results}"
    response = requests.get(search_url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch search results. Status Code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    links = []

    # Extract links from Bing search results
    for link in soup.select("li.b_algo h2 a"):
        href = link.get("href")
        if href and href.startswith("http"):
            links.append(href)

    print(f"Found {len(links)} links.")
    return links


def scrape_real_estate_data(urls):
    """Scrape company names, emails, and project names from the given URLs."""
    scraped_data = []

    for i, url in enumerate(urls, 1):
        print(f"Scraping URL {i}/{len(urls)}: {url}")
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            if response.status_code != 200:
                print(f"Failed to access {url}. Status code: {response.status_code}")
                continue

            soup = BeautifulSoup(response.content, "html.parser")

            # Extract data from the website
            company_name = soup.title.string.strip() if soup.title else "N/A"
            email = None
            for a_tag in soup.find_all("a", href=True):
                if "mailto:" in a_tag["href"]:
                    email = a_tag["href"].replace("mailto:", "").strip()
                    break
            email = email or "N/A"
            project_name = soup.find("h1").text.strip() if soup.find("h1") else "N/A"

            # Save the scraped data
            scraped_data.append({
                "Company Name": company_name,
                "Email": email,
                "Project Name": project_name,
                "URL": url
            })
        except Exception as e:
            print(f"Error scraping {url}: {e}")
        
        time.sleep(1)  # Delay for politeness

    return scraped_data


def save_to_csv(data, filename="scraped_real_estate_data.csv"):
    """Save the scraped data to a CSV file."""
    if not data:
        print("No data to save.")
        return

    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}")


if __name__ == "__main__":
    # Define the search query and number of leads
    search_query = "Real estate developers Germany new construction projects"
    num_leads = 20

    # Step 1: Search Bing for leads
    urls = search_bing(search_query, num_results=num_leads)

    # Step 2: Scrape data from the returned URLs
    scraped_data = scrape_real_estate_data(urls)

    # Step 3: Save the scraped data to a CSV file
    save_to_csv(scraped_data)


# Load scraped data from CSV
def load_scraped_data(filename="scraped_real_estate_data.csv"):
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

# Send test email
def send_test_email(scraped_data):
    # SMTP configuration
    smtp_server = "smtp.gmail.com"  # Change this to your SMTP server
    smtp_port = 587
    sender_email = "itsmishesbone@gmail.com"  # Replace with your email
    sender_password = "ezdz gmyf ldms jxwd"        # Replace with your email password
    recipient_email = "team@propertyvisualizer.com"

    # Create the email
    subject = "Test Email: AI-Powered Cold Outreach"
    body = f"""
    Hallo Team,

    Dies ist ein Test-E-Mail für den Cold Outreach. Hier sind einige der gescrapten Daten:

    {scraped_data[0]["Company Name"]} - {scraped_data[0]["Email"]}
    Projekt: {scraped_data[0]["Project Name"]}
    URL: {scraped_data[0]["URL"]}

    Vielen Dank,
    Ihr Testsystem
    """

    # Set up MIME
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("Test email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Step 1: Load scraped data
    data = load_scraped_data()

    # Step 2: Send test email
    send_test_email(data)
