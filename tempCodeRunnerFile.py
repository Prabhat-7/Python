import requests

def fetch_news(api_key, topics, country='us'):
    base_url = 'https://newsapi.org/v2/top-headlines'
    headers = {
        'Authorization': f'Bearer {api_key}'#convention for an authorized api request
    }
    
    news_data = {}

    for topic in topics:
        params = {
            'category': topic,
            'country': country,
            'pageSize': 5  # Fetch 5 articles