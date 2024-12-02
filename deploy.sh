#!/bin/bash

# Set variables
APP_NAME="chatckt_ui" # Name for the PM2 process
APP_DIR="/home/ubuntu/chatckt_app" # Deployment directory
REPO_URL="https://github.com/nitinalexvaidyan/chatckt_app.git" # Replace with your repository URL
BRANCH="main" # Branch to deploy
BUILD_DIR="build" # React build directory

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

# Install dependencies
echo "Installing dependencies..."
cd "chat_ui"
npm install

# Build the React app
echo "Building the React app..."
npm run build

# Serve the app with PM2
echo "Deploying the application with PM2..."
if pm2 list | grep -q $APP_NAME; then
    echo "Restarting existing PM2 process..."
    pm2 restart $APP_NAME
else
    echo "Starting a new PM2 process..."
    pm2 serve $BUILD_DIR 3000 --name $APP_NAME --spa
fi

# Save PM2 process list
echo "Saving PM2 process list..."
pm2 save

# Set PM2 to start on boot
echo "Configuring PM2 to start on boot..."
pm2 startup
sudo env PATH=$PATH:/usr/bin pm2 startup systemd -u $USER --hp $HOME
pm2 save

echo "Deployment complete! The application is running at http://localhost:3000"
