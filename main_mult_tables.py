import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os

URL = 'https://www.nba.com/stats/'

# XPATH obtained by inspecting each required element
XPATH_SEASON = '//*[@id="__next"]/div[2]/div[2]/div[3]/div/div[1]/section[1]/div/div[2]/button[2]'
XPATH_POINTS = '//*[@id="__next"]/div[2]/div[2]/div[3]/div/div[1]/section[1]/div/div[4]/div[1]/div/table/tbody/tr'
XPATH_REBOUNDS = '//*[@id="__next"]/div[2]/div[2]/div[3]/div/div[1]/section[1]/div/div[4]/div[2]/div/table/tbody/tr'
XPATH_STEALS = '//*[@id="__next"]/div[2]/div[2]/div[3]/div/div[1]/section[1]/div/div[4]/div[5]/div/table/tbody/tr'
XPATH_BLOCKS = '//*[@id="__next"]/div[2]/div[2]/div[3]/div/div[1]/section[1]/div/div[4]/div[4]/div/table/tbody/tr'

# Set up WebDriver (e.g., chromedriver for Chrome) and open the webpage
driver = webdriver.Chrome()
driver.get(URL)

# Decline the prompt 'Additional tracking preference'
try:
    decline_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "I Decline")]'))
    )
    decline_button.click()
    print("Declined the pop-up.")
except Exception as e:
    print("Pop-up not found or error occurred:", e)

# Click tab 'Season Leaders'
button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, XPATH_SEASON))
)
ActionChains(driver).move_to_element(button).perform() # Scroll to the button if it's out of view
button.click()

# Delay for the relevant table to load
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//table"))
    )
    print("Table found and page loaded.")
except Exception as e:
    print("Error:", e)

# Extract top players by points
nba_top_scorers = []
try:
    rows = driver.find_elements(By.XPATH, XPATH_POINTS)

    for row in rows:
        player_name = row.find_element(By.XPATH, "./td[2]/a").text.strip()  # Get player name
        avg_points = row.find_element(By.XPATH, "./td[3]").text.strip()  # Get average points

        nba_top_scorers.append([player_name, avg_points])  # Append the extracted data
except Exception as e:
    print("No more players found or error occurred:", e)

# Extract top players by rebounds
nba_top_rebounders = []
try:
    rows = driver.find_elements(By.XPATH, XPATH_REBOUNDS)

    for row in rows:
        player_name = row.find_element(By.XPATH, "./td[2]/a").text.strip()
        avg_rebounds = row.find_element(By.XPATH, "./td[3]").text.strip()

        nba_top_rebounders.append([player_name, avg_rebounds])
except Exception as e:
    print("No more players found or error occurred:", e)

# Extract top players by steals
nba_top_steals = []
try:
    rows = driver.find_elements(By.XPATH, XPATH_STEALS)

    for row in rows:
        player_name = row.find_element(By.XPATH, "./td[2]/a").text.strip()
        avg_steals = row.find_element(By.XPATH, "./td[3]").text.strip()

        nba_top_steals.append([player_name, avg_steals])
except Exception as e:
    print("No more players found or error occurred:", e)

# Extract top players by blocks
nba_top_blockers = []
try:
    rows = driver.find_elements(By.XPATH, XPATH_BLOCKS)

    for row in rows:
        player_name = row.find_element(By.XPATH, "./td[2]/a").text.strip()
        avg_blocks = row.find_element(By.XPATH, "./td[3]").text.strip()

        nba_top_blockers.append([player_name, avg_blocks])
except Exception as e:
    print("No more players found or error occurred:", e)

# Save CSV file in the working file folder
script_folder = os.path.dirname(os.path.realpath(__file__))
csv_file_path = os.path.join(script_folder, "top_nba_player_data_alt.csv")

# Save data to a CSV file with separate sections for each stat
try:
    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Write Points per game table
        writer.writerow(["Rank", "Player Name", "Points per game"])
        for i, scorer in enumerate(nba_top_scorers, start=1):
            writer.writerow([i, scorer[0], scorer[1]])
        writer.writerow([])  # Adds a blank row for spacing with the next table

        # Write Rebounds per game table
        writer.writerow(["Rank", "Player Name", "Rebounds per game"])
        for i, rebounder in enumerate(nba_top_rebounders, start=1):
            writer.writerow([i, rebounder[0], rebounder[1]])
        writer.writerow([])

        # Write Steals per game table
        writer.writerow(["Rank", "Player Name", "Steals per game"])
        for i, stealer in enumerate(nba_top_steals, start=1):
            writer.writerow([i, stealer[0], stealer[1]])
        writer.writerow([])

        # Write Blocks per game table
        writer.writerow(["Rank", "Player Name", "Blocks per game"])
        for i, blocker in enumerate(nba_top_blockers, start=1):
            writer.writerow([i, blocker[0], blocker[1]])

    print("Players' data has been saved to top_nba_player_data_alt.csv.")

except Exception as e:
    print("Error occurred while saving to CSV:", e)

input("Press Enter to close the browser...")
