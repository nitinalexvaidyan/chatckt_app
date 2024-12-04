#!/bin/bash

# ----------------- Configuration ----------------- #
APP_NAME_REACT="chatckt_ui"        # PM2 process name for React app
APP_NAME_FLASK="chatckt_api"       # PM2 process name for Flask app
APP_DIR="/home/ubuntu/chatckt_app" # Deployment directory
BUILD_DIR="build"                  # React build directory
FLASK_DIR="$APP_DIR/chat_api"      # Flask application directory
VENV_DIR="$APP_DIR/venv/bin"       # Path to Python virtual environment

# ----------------- Script Execution ----------------- #
cd "$APP_DIR"
git pull

# Activate virtual environment
source "$VENV_DIR/activate"
export OPENAI_API_KEY='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'

# Get public IP for setting up the backend API URL
PUBLIC_IP=$(curl -s ifconfig.me)
echo "Setting backend API URL with public IP: $PUBLIC_IP"
echo "REACT_APP_BACKEND_API_URL=http://$PUBLIC_IP:5000/query" > .env

# ----------------- Flask Application Setup ----------------- #
cd "$FLASK_DIR"
if pm2 list | grep -q "$APP_NAME_FLASK"; then
    echo "Restarting Flask application..."
    pm2 restart "$APP_NAME_FLASK"
else
    echo "Starting Flask application..."
    pm2 start python3 --name "$APP_NAME_FLASK" -- app.py
#    pm2 start python3 --name "chatckt_api" -- app.py
fi

# ----------------- React Application Setup ----------------- #
echo "Installing React dependencies..."
cd "$APP_DIR/chat_ui"
npm install

echo "Building React application..."
npm run build

echo "Serving React application with PM2..."
if pm2 list | grep -q "$APP_NAME_REACT"; then
    echo "Restarting React application..."
    pm2 restart "$APP_NAME_REACT"
else
    echo "Starting React application..."
    pm2 serve "$BUILD_DIR" 3000 --name "$APP_NAME_REACT" --spa
fi

# ----------------- PM2 Process Management ----------------- #
echo "Saving PM2 process list..."
pm2 save

echo "Setting up PM2 to start on boot..."
pm2 startup
sudo env PATH=$PATH:/usr/bin pm2 startup systemd -u "$USER" --hp "$HOME"
pm2 save
