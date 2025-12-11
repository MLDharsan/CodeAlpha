#Task 01

import os
import shutil


def move_jpg_files(source_folder, destination_folder):

    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created folder: {destination_folder}")

    # Counter for moved files
    moved_count = 0

    # Iterate through files in source folder
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.jpg'):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            # Move the file
            shutil.move(source_path, destination_path)
            print(f"Moved: {filename}")
            moved_count += 1

    print(f"\nTotal files moved: {moved_count}")

#Task 02
import re


def extract_emails(input_file, output_file):
    """
    Extract all email addresses from a text file and save to another file.
    """
    # Email regex pattern
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    try:
        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all email addresses
        emails = re.findall(email_pattern, content)

        # Remove duplicates and sort
        unique_emails = sorted(set(emails))

        # Write to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            for email in unique_emails:
                f.write(email + '\n')

        print(f"Extracted {len(unique_emails)} unique email(s)")
        print(f"Saved to: {output_file}")

        return unique_emails

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found!")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

#Task 03
import requests
from re import search


def scrape_webpage_title(url, output_file):
    """
    Scrape the title from a webpage and save it to a file.
    Works best with static websites. For dynamic sites, use scrape_webpage_title_advanced().
    """
    try:
        # Check if output_file is a directory
        if os.path.isdir(output_file):
            output_file = os.path.join(output_file, 'webpage_title.txt')
            print(f"Directory detected. Saving to: {output_file}")

        # Send GET request with headers to avoid blocking
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()

        # Extract title using regex
        title_match = search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)

        if title_match:
            title = title_match.group(1).strip()

            # Check if title is empty or just whitespace
            if not title:
                title = "No title found (page may be JavaScript-rendered)"
                print("\n⚠️  WARNING: This appears to be a dynamic website.")
                print("The title is loaded by JavaScript, which requests library cannot handle.")
                print("For dynamic sites like Booking.com, you need Selenium or Playwright.")

            # Save to file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"URL: {url}\n")
                f.write(f"Title: {title}\n")

            print(f"Title scraped: {title}")
            print(f"Saved to: {output_file}")
            return title
        else:
            print("No <title> tag found on the webpage")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def scrape_webpage_title_advanced(url, output_file):

    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        # Check if output_file is a directory
        if os.path.isdir(output_file):
            output_file = os.path.join(output_file, 'webpage_title.txt')

        # Setup headless Chrome
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        print("Opening browser...")
        driver = webdriver.Chrome(options=chrome_options)

        # Load the page
        driver.get(url)

        # Wait for title to load (max 10 seconds)
        WebDriverWait(driver, 10).until(
            lambda d: d.title and d.title.strip() != ""
        )

        title = driver.title
        driver.quit()

        # Save to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"URL: {url}\n")
            f.write(f"Title: {title}\n")

        print(f"Title scraped: {title}")
        print(f"Saved to: {output_file}")
        return title

    except ImportError:
        print("\nSelenium not installed!")
        print("Install it with: pip install selenium")
        print("Also install ChromeDriver from: https://chromedriver.chromium.org/")
        return None
    except Exception as e:
        print(f"Error: {e}")
        try:
            driver.quit()
        except:
            pass
        return None


def main():

    print("\n=== TASK AUTOMATION MENU ===")
    print("1. Move .jpg files to a new folder")
    print("2. Extract email addresses from text file")
    print("3. Scrape webpage title")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == '1':
        source = input("Enter source folder path: ")
        destination = input("Enter destination folder path: ")
        move_jpg_files(source, destination)

    elif choice == '2':
        input_file = input("Enter input file path: ")
        output_file = input("Enter output file path: ")
        extract_emails(input_file, output_file)

    elif choice == '3':
        url = input("Enter webpage URL: ")
        output_file = input("Enter output file path: ")
        scrape_webpage_title(url, output_file)

    elif choice == '4':
        print("Exiting...")
        return

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()