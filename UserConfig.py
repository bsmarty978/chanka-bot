import os

# Set environment variables
os.environ['API_USER'] = 'username'
os.environ['API_PASSWORD'] = 'secret'
os.environ['HELP_MSG'] ='$help - to get help.\n$quote - to get random quote.\n$noods - to get random nood.\n$menu - to get menu.\n\nchevi sensei is lub'
os.environ['PREFIX'] = '$'

# Get environment variables
USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')