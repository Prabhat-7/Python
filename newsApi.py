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
            'pageSize': 15  # Fetch 5 articles per topic
             }
        
        response = requests.get(base_url, headers=headers, params=params)
        
        if response.status_code == 200:
            # Safely extract articles from the response JSON
            articles = response.json().get('articles', [])#returns article from the JSON if present
            news_data[topic] = articles                   # but if absent returns an empty list
        else:
            print(f"Failed to fetch news for topic {topic}: {response.status_code}")

    return news_data

def display_news(news_data):
    for topic, articles in news_data.items():
        print(f"\nNews in category: {topic.capitalize()}")
        for article in articles:
            title = article.get('title', 'No title')
            description = article.get('description', 'No description')
            url = article.get('url', 'No URL')
            print(f"\nTitle: {title}\nDescription: {description}\nURL: {url}\n{'-'*40}")

if __name__ == "__main__":
    api_key = "22cf104f25b34bb5a878011298f5239d" 
    topics = [ 'sports']

    news_data = fetch_news(api_key, topics)
    display_news(news_data)
