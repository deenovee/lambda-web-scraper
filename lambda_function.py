import requests
from tabulate import tabulate
from bs4 import BeautifulSoup
import csv
import os
import boto3

ses = boto3.client('sns')

def lambda_handler(event, context):
    url = 'https://www.forexfactory.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
    response = requests.get(url, headers=headers)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the table with the class "calendar__table"
    table = soup.find('table', {'class': 'calendar__table'})
    # Find the first 10 rows
    rows = []
    for class_string in ['calendar__row calendar_row', 'calendar__row calendar_row calendar__row--no-grid nogrid', 'calendar__row calendar_row calendar__row--grey', 'calendar__row calendar_row calendar__row--grey calendar__row--new-day newday', 'calendar__row calendar_row calendar__row--grey calendar__row--no-grid nogrid']:
        rows += table.find_all('tr', {'class': class_string})

    # Create a list to store the data
    data = []

    # Iterate over the rows
    for row in rows:
        # Find the cells
        cells = row.find_all('td')
        # Find the time
        time = cells[1].text
        impact_icon = cells[4].find('span', {'class': 'high'})
        if impact_icon:
            color = impact_icon['class'][0]
        else:
            color = "not found"
        # Find the event title
        event_title = cells[5].find('div').find('span', {'class': 'calendar__event-title'}).text
    
        currency = cells[3].text
        # Append the data to the list
        if color == 'high':
            data.append({"time":time, "color":color, "event-title":event_title, "currency":currency})
        else:
            pass

    if len(data) < 1:
        message = "No high impact stories for today"
    else:
        message = tabulate(data, headers="keys", tablefmt="html")

    # Publish message to SNS
    sns.publish(
        TopicArn=os.environ['SNS_TOPIC_ARN'],
        Message=message,
        Subject="Your Daily Report"
    )
    
    
    
    
    
    
    
    
    
    