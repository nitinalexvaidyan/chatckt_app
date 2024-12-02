import React, { useEffect, useRef } from "react";
import ReactMarkdown from "react-markdown";
import "./ChatMessages.css";

// Utility function to render formatted text
const renderFormattedText = (text) => {
  return <ReactMarkdown>{text}</ReactMarkdown>;
};

// Functional component to display chat messages
const ChatMessages = ({ messages }) => {
  const containerRef = useRef(null);

  useEffect(() => {
    // Scroll to the bottom of the chat messages container
    if (containerRef.current) {
      containerRef.current.scrollTop = containerRef.current.scrollHeight;
    }
  }, [messages]);

  return (
    <div className="chat-messages-container" ref={containerRef}>
      {messages.map((message, index) => (
        <div
          key={index}
          className={`message ${message.sender}`}
          style={{
            textAlign: message.sender === "user" ? "right" : "left",
            marginBottom: "10px",
          }}
        >
          {message.text === "loading" ? (
            <span className="loading-dots"></span> // Show loading dots
          ) : (
            <span>{renderFormattedText(message.text)}</span>
          )}
        </div>
      ))}
    </div>
  );
};

export default ChatMessages;
