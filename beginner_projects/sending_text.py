import requests
# one per day free
resp = requests.post('https://textbelt.com/text', {
  'phone': input("Input your number: "),
  'message': input("Input your text: "),
  'key': 'textbelt',
})
print(resp.json())
