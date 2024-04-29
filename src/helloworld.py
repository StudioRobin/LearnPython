msg = "hello world!"
print(msg)

# create a function that sums two numbers
def add(a, b):
    return a + b

# create a function that used request to get a response from a website
def get_response(url):
    import requests
    response = requests.get(url)
    return response

