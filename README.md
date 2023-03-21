# Simple Blockchain Python 

# Requirements
* **Python:** `3.9.8`
* **PostgreSQL:**  `15.2`
* **Flask:** `2.2.3`
---

## Build / Run

```shell
git clone https://github.com/QuitM6n/Blockchain.git
cd Blockchain

docker build -t blockchain .
docker run -d -p 8080:8080 --name blockchain-python blockchain 
```

## Endpoints

### - NewTransaction `/new/transaction`

### - GetBlock  `/get/block`

