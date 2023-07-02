import requests
import base64

# Elasticsearch server details
elasticsearch_url = 'http://localhost:9200'
index_name = 'logstash-p-test-0001'

# Authentication credentials
username = 'elastic'
password = 'changeme'

# Base64 encode the username and password
credentials = base64.b64encode('{}:{}'.format(username, password).encode('utf-8')).decode('utf-8')

# Headers with basic authentication
headers = {
    'Authorization': 'Basic {}'.format(credentials),
    'Content-Type': 'application/json'
}

# Create index
create_index_url = '{}/{}'.format(elasticsearch_url, index_name)
requests.put(create_index_url, headers=headers)

# Define a document to insert
document = {
  "id": "1",
  "title": "Document Example",
  "content": "This is an example document for Elasticsearch.",
  "timestamp": "2023-07-02T10:00:00"
}

# Insert the document into the index
insert_document_url = '{}/{}/_doc'.format(elasticsearch_url, index_name)
requests.post(insert_document_url, headers=headers, json=document)

# Refresh the index
refresh_url = '{}/{}/_refresh'.format(elasticsearch_url, index_name)
requests.post(refresh_url, headers=headers)

# Perform a search to verify that the document has been indexed
search_url = '{}/{}/_search'.format(elasticsearch_url, index_name)
search_response = requests.get(search_url, headers=headers).json()

# Display search results
for hit in search_response['hits']['hits']:
    print(hit['_source'])
