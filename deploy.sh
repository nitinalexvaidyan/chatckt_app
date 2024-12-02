#!/bin/bash

# Set variables
APP_NAME_REACT="chatckt_ui" # PM2 process name for React app
APP_NAME_FLASK="chatckt_api" # PM2 process name for Flask app
APP_DIR="/home/ubuntu/chatckt_app" # Deployment directory
REPO_URL="https://github.com/nitinalexvaidyan/chatckt_app.git" # Repository URL
BRANCH="main" # Branch to deploy
BUILD_DIR="build" # React build directory
FLASK_DIR="$APP_DIR/chat_api" # Flask app directory
VENV_DIR="venv/bin/activate" # Virtual environment path

# Clone or update the repository
if [ -d "$APP_DIR" ]; then
    echo "Pulling latest changes..."
    cd $APP_DIR
    git reset --hard
    git pull origin $BRANCH
else
    echo "Cloning repository..."
    git clone -b $BRANCH $REPO_URL $APP_DIR
    cd $APP_DIR
fi

git pull
# Fetch the public IP
PUBLIC_IP=$(curl -s ifconfig.me)

# Update the .env file
echo "REACT_APP_BACKEND_API_URL=http://$PUBLIC_IP:5000/query" > .env


# Activate Python virtual environment
echo "Activating Python virtual environment..."
source $VENV_DIR
export OPENAI_API_KEY='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'


# Deploy Flask application
echo "Deploying Flask application with PM2..."
cd $FLASK_DIR
if pm2 list | grep -q $APP_NAME_FLASK; then
    echo "Restarting existing PM2 process for Flask..."
    pm2 restart $APP_NAME_FLASK
else
    echo "Starting a new PM2 process for Flask..."
    pm2 start python3 --name $APP_NAME_FLASK -- app.py
fi

# Install React dependencies
echo "Installing React dependencies..."
cd "$APP_DIR/chat_ui"
npm install

# Build the React app
echo "Building the React app..."
npm run build

# Serve the React app with PM2
echo "Deploying the React application with PM2..."
if pm2 list | grep -q $APP_NAME_REACT; then
    echo "Restarting existing PM2 process for React..."
    pm2 restart $APP_NAME_REACT
else
    echo "Starting a new PM2 process for React..."
    pm2 serve $BUILD_DIR 3000 --name $APP_NAME_REACT --spa
fi

# Save PM2 process list
echo "Saving PM2 process list..."
pm2 save

# Set PM2 to start on boot
echo "Configuring PM2 to start on boot..."
pm2 startup
sudo env PATH=$PATH:/usr/bin pm2 startup systemd -u $USER --hp $HOME
pm2 save

echo "Deployment complete!"
echo "React application is running at http://localhost:3000"
echo "Flask API is running at the configured endpoint."
