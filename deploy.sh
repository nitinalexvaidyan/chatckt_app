#!/bin/bash

# Deployment script for a full-stack application (React front-end and Flask back-end)

# ----------------- Configuration ----------------- #
APP_NAME_REACT="chatckt_ui"        # PM2 process name for React app
APP_NAME_FLASK="chatckt_api"       # PM2 process name for Flask app
APP_DIR="/home/ubuntu/chatckt_app" # Deployment directory
REPO_URL="https://github.com/nitinalexvaidyan/chatckt_app.git" # Git repository URL
BRANCH="main"                      # Branch to deploy
BUILD_DIR="build"                  # React build directory
FLASK_DIR="$APP_DIR/chat_api"      # Flask application directory
VENV_DIR="$FLASK_DIR/venv/bin" # Path to Python virtual environment

# ----------------- Functions ----------------- #

# Log a message with a timestamp
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1"
}

# Update or clone the repository
update_repository() {
    if [ -d "$APP_DIR" ]; then
        log "Pulling latest changes from repository..."
        cd "$APP_DIR"
        git reset --hard
        git pull origin "$BRANCH"
    else
        log "Cloning repository..."
        git clone -b "$BRANCH" "$REPO_URL" "$APP_DIR"
        cd "$APP_DIR"
    fi
    git pull
}

# Update environment variables for React app
update_env_file() {
    PUBLIC_IP=$(curl -s ifconfig.me)
    log "Setting backend API URL with public IP: $PUBLIC_IP"
    echo "REACT_APP_BACKEND_API_URL=http://$PUBLIC_IP:5000/query" > .env
}

# Activate Python virtual environment
activate_venv() {
    if [ -f "$VENV_DIR" ]; then
        log "Activating Python virtual environment..."
        source "$VENV_DIR/activate"
        export OPENAI_API_KEY='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'
    else
        log "Virtual environment not found. Please ensure it exists at $VENV_DIR."
        exit 1
    fi
}

# Deploy Flask app with PM2
deploy_flask() {
    log "Deploying Flask application..."
    cd "$FLASK_DIR"
    if pm2 list | grep -q "$APP_NAME_FLASK"; then
        log "Restarting Flask application..."
        pm2 restart "$APP_NAME_FLASK"
    else
        log "Starting Flask application..."
        pm2 start python3 --name "$APP_NAME_FLASK" -- app.py
    fi
}

# Install React dependencies and build the app
deploy_react() {
    log "Installing React dependencies..."
    cd "$APP_DIR/chat_ui"
    npm install

    log "Building React application..."
    npm run build

    log "Serving React application with PM2..."
    if pm2 list | grep -q "$APP_NAME_REACT"; then
        log "Restarting React application..."
        pm2 restart "$APP_NAME_REACT"
    else
        log "Starting React application..."
        pm2 serve "$BUILD_DIR" 3000 --name "$APP_NAME_REACT" --spa
    fi
}

# Configure PM2 for process management
configure_pm2() {
    log "Saving PM2 process list..."
    pm2 save

    log "Setting up PM2 to start on boot..."
    pm2 startup
    sudo env PATH=$PATH:/usr/bin pm2 startup systemd -u "$USER" --hp "$HOME"
    pm2 save
}

# ----------------- Execution ----------------- #

log "Starting deployment process..."

update_repository
update_env_file
activate_venv
deploy_flask
deploy_react
configure_pm2

log "Deployment complete!"
log "React application is running at http://localhost:3000"
log "Flask API is running at the configured endpoint."
