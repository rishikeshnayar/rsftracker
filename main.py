import time
import send_sms
import webscraper

# Main function.  Uses condition functions to check if RSF is below or above threshold, sends appropriate SMS, and switches condition
def main(threshold=40):
    conditions = [original_cond, secondary_cond]
    texts = [f"The RSF is less than {threshold}% full!  You should consider going :D", f"The RSF has exceeded the {threshold}% threshold - perhaps wait until it's less busy."]
    i = 0

    while True:
        if conditions[i % 2](threshold, webscraper.scrape(webscraper.driver)):
            send_sms.text(texts[i % 2])
            i += 1 # Change condition to new condition
        time.sleep(600) # Check crowdmeter again after 10 minutes

# Function to check if RSF is below threshold
def original_cond(threshold, curr_percent):
    if curr_percent < threshold:
        return True

# Function to check if RSF is above threshold + 5
def secondary_cond(threshold, curr_percent):
    if curr_percent >= threshold + 5:
        return True

main()