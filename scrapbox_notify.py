import json
import requests
import datetime
import schedule
import time
import argparse
import slackweb

parser = argparse.ArgumentParser()
parser.add_argument('--url',help='url')
parser.add_argument('--slack',help='slack_url')
args = parser.parse_args()
url = args.url
slack_url = args.slack

url_id = url.split('/')[-2] if url.split('/')[-1] == '' else url.split('/')[-1]
api_url = 'https://scrapbox.io/api/pages/' + url_id
params = {'limit':10000}

def job():
    res = requests.get(api_url,params=params)
    list_pages = json.loads(res.text)['pages']
    week_ago = datetime.datetime.now() - datetime.timedelta(weeks = 1)
    week_ago_unix = week_ago.timestamp()
    new_page = 0
    re_page = 0
    for page in list_pages:
        if page['created'] > week_ago_unix:
            new_page += 1
        elif page['updated'] > week_ago_unix:
            re_page += 1
    text = 'この1週間で新しく作成されたページは，' + str(new_page) + '件，更新されたページは，' + str(re_page) + '件です．: ' + str(url)
    slack = slackweb.Slack(url=slack_url)
    slack.notify(attachments=[{'text':text}])



schedule.every().monday.at("12:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(10)
