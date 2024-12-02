
## Setup Instructions

### EC2 Instance Setup

1. **Launch EC2 Instance**:
    - Log in to AWS Console.
    - Go to the EC2 Dashboard and click `Launch Instances`.
    - Choose `Ubuntu Server 22.04 LTS` (or the latest LTS version).
    - Select an instance type (e.g., `t2.micro` for the free tier).
    - Configure security group: Add rules to allow HTTP (port 80) and custom TCP (port 5000) from `Anywhere (0.0.0.0/0)`.
    - Launch the instance and connect to it using SSH:
    
    ```bash
    ssh -i "path/to/your-key.pem" ubuntu@<your-ec2-public-ip>
    ```

2. **Install Dependencies**:
    ```bash
    sudo apt update && sudo apt upgrade -y
    sudo apt install python3 python3-pip python3-venv git -y
    git clone https://github.com/<your-username>/chatckt_app.git
    cd chatckt_app
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Run the Flask Server**:
    ```bash
    python3 app.py
    ```

4. **Access the App**:
    Visit `http://<your-ec2-public-ip>:5000` in your browser to access the Flask application.

### Setup for Flask Application

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/<your-username>/chatckt_app.git
    cd chatckt_app
    ```

2. **Create and Activate Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask Server**:
    ```bash
    python3 app.py
    ```

### Git Setup

1. **Create a GitHub Repository**:
    - Go to [GitHub](https://github.com) and create a new repository called `chatckt_app`.

2. **Set Remote Origin**:
    ```bash
    cd /path/to/chatckt_app
    git remote add origin https://github.com/<your-username>/chatckt_app.git
    ```

3. **Push Code to GitHub**:
    ```bash
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    ```

### Elasticsearch Setup

1. **Check Elasticsearch Service Status**:
    ```bash
    sudo service elasticsearch status
    sudo systemctl status elasticsearch
    sudo journalctl -u elasticsearch.service -f
    ```

2. **Start Elasticsearch**:
    ```bash
    sudo systemctl start elasticsearch
    sudo systemctl enable elasticsearch
    sudo systemctl restart elasticsearch
    ```

3. **Check Elasticsearch**:
    ```bash
    curl -X GET "http://<your-elasticsearch-ip>:9200/chat_messages/_search?pretty"
    ```

4. **Modify JVM Options for Heap Memory**:
    Edit the JVM options file for memory tuning:
    ```bash
    sudo vi /etc/elasticsearch/jvm.options
    ```

### Kibana Setup

1. **Access Kibana**:
    Visit `http://<your-kibana-ip>:5601` in your browser.

2. **Configure Kibana**:
    Edit the `kibana.yml` file to allow external access:
    ```bash
    sudo vi /etc/kibana/kibana.yml
    ```

    Modify the following settings:
    ```yaml
    server.port: 5601
    server.host: "0.0.0.0"  # Allows external access
    elasticsearch.hosts: ["http://localhost:9200"]  # Replace with your ES URL if different
    ```

### SCP File Transfer

To transfer files to the EC2 instance:

```bash
scp -i "/path/to/your-key.pem" -r /path/to/your/local/folder ubuntu@<your-ec2-ip>:/path/to/destination/folder
