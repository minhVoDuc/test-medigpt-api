# test-medigpt-api
## ⭐ **Introduction**
 Test making api for medigpt (using gpt4free lib)  
 App running on 127.0.0.1:8001 
## 🧩 **Prerequisites**
* Having installed **python3** or **docker**
## 📘 **Guide**
### 📖 Starting tool
* Using directly **python**
    1. Create virtual env  
`$ python -m venv .venv`
    2. Activate virtual env
`$ source .venv/bin/activate` (linux)  
or `$ .venv/Scripts/activate` (windows)  
    3. Install required modules  
`(.venv) $ pip install --no-cache-dir --upgrade -r requirements.txt`    
    4. Run app.py   
`(.venv) $ python app.py`   
    ***Note***: After running tool from **python**, deactivate virtual env  
        `(.venv) $ deactivate`
* Using **docker**
    1. Build image  
`$ docker build -t {image-name} .`
    2. Run tool  
`$ docker run -d --name {container-name} -p 8001:8001 {image-name}`  
or `$ docker run -d --name {container-name} -p 127.0.0.1:8001:8001 {image-name}` 
    ***Note***: After running tool from **docker**, remove current container before running tool again  
        `$ docker container rm {container-name}`
### 📖 Running tool
Go to `172.0.0.1:8001/docs` or `127.0.0.1:8001/redoc` to test API directly 