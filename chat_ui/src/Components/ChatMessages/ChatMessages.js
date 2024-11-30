import React from "react";
import "./ChatMessages.css";

// Functional component to display chat messages
const ChatMessages = ({ messages }) => {
  return (
    <div className="chat-messages-container">
      {messages.map((message, index) => (
        <div
          key={index}
          className={`message ${message.sender}`}
          style={{
            textAlign: message.sender === "user" ? "right" : "left",
            marginBottom: "10px",
          }}
        >
          <span>{message.text}</span>
        </div>
      ))}
    </div>
  );
};

export default ChatMessages;
