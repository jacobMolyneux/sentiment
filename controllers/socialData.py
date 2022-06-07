import requests

def getSocialData(term):
    data = requests.get(
        f"https://api.twitter.com/2/tweets/search/recent?query={term}", 
        headers = {
            'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAGiKMwEAAAAA9IOJaFNMvj3x6FaqJQnoJyZ81Rs%3D8MVGwbqXMkCedrCMgSSlCguvPXqKBKQovKm8ZjaEqMe1N1sbs2'
            })
    return data.text

