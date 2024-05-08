msg = "hello world!"
print(msg)

# create a function that sums two numbers
def add(a, b):
    return a + b

# q: explain what the following code does
# a: it creates a variable called msg and assigns it the value "hello world!"
# create a function that used request to get a response from a website
def get_response(url):
    import requests
    response = requests.get(url)
    return response

