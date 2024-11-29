import requests

server_url="https://jsonplaceholder.typicode.com"

def get_request():
    res=requests.get(f"{server_url}/posts")
    if res.status_code==200:
        print("Get: ")
        posts = res.json()
        
        filtered_titles = [post for post in posts if len(post['title'].split()) <= 6]
        
        filtered_bodies = [post for post in filtered_titles if post['body'].count('\n') <= 3]
        
        for post in filtered_titles[:3] and filtered_bodies[:3]: 
            print(post)
        
        
    else:
        print(f"Failded:\n status code: {res.status_code}")
    
def post_request():
    new={
        "title":"Anna's post",
        "body":"Just for fun",
        "userId":1
        }
    res=requests.post(f"{server_url}/posts",json=new)
    if res.status_code==201:
        print("Post: ")
        print(res.json())
     
    else:
        print(f"Failded:\n status code: {res.status_code}")
        
    
def put_request():
    post_id=1
    update={
        "title":"Anna's NEW post",
        "body": "New version",
        "userID": 1
        }
    res=requests.put(f"{server_url}/posts/{post_id}",json=update)
    if res.status_code==200:
        print("Put: ")
        print(res.json())
     
    else:
        print(f"Failded:\n status code: {res.status_code}")
 
def delete_requests():
    post_id=1
    res=requests.delete(f"{server_url}/posts/{post_id}")
    if res.status_code==200:
        print("Delete:  ")
        print(res.json())
     
    else:
        print(f"Failded:\n status code: {res.status_code}")
    


get_request()
post=post_request()
if post:
    print(post)
    
put_request()
delete_requests()
