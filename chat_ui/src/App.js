import { useState, useEffect } from "react";
import axios from "axios";
import { SearchBar, ChatMessages } from "./Components";
import "./App.css";

// const BACKEND_API_URL = process.env.REACT_APP_BACKEND_API_URL;
const BACKEND_API_URL = "http://3.80.153.168:5000/query";

function App() {
  const [messages, setMessages] = useState([]); // State to store chat messages
  const [loading, setLoading] = useState(false); // State to track loading status

  // Load messages from sessionStorage when the component mounts
  useEffect(() => {
    const storedMessages = sessionStorage.getItem("messages");
    if (storedMessages) {
      setMessages(JSON.parse(storedMessages));
    }
  }, []);

  // Update sessionStorage whenever the messages array changes
  useEffect(() => {
    if (messages.length > 0) {
      sessionStorage.setItem("messages", JSON.stringify(messages));
    }
  }, [messages]);

  // Function to handle user query and response from the bot
  const handleSearch = async (query) => {
    if (query.trim()) {
      const userMessage = { text: query, sender: "user" };
      setMessages((prevMessages) => [...prevMessages, userMessage]);

      // Add loading message
      const loadingMessage = { text: "loading", sender: "bot", loading: true };
      setMessages((prevMessages) => [...prevMessages, loadingMessage]);

      setLoading(true); // Set loading state to true

      try {
        const response = await axios.post(BACKEND_API_URL, { query });

        const botMessage = response?.data?.response
          ? { text: response.data.response, sender: "bot" }
          : { text: "Sorry, I couldn't understand that.", sender: "bot" };

        // Remove loading message and add the bot's response
        setMessages((prevMessages) => {
          const updatedMessages = prevMessages.filter((msg) => !msg.loading);
          return [...updatedMessages, botMessage];
        });
      } catch (error) {
        const botMessage = {
          text: "Sorry, something went wrong. Please try again later.",
          sender: "bot",
        };

        // Remove loading message and add the error message
        setMessages((prevMessages) => {
          const updatedMessages = prevMessages.filter((msg) => !msg.loading);
          return [...updatedMessages, botMessage];
        });
        console.error("API error:", error);
      } finally {
        setLoading(false); // Set loading state to false after the response
      }
    }
  };

  // Function to clear the chat and session storage
  const clearChat = () => {
    setMessages([]);
    sessionStorage.removeItem("messages");
  };

  return (
    <div className="App">
      <ChatMessages messages={messages} />
      <div className="fixed-buttons-container">
        <SearchBar onSearch={handleSearch} disabled={loading} />{" "}
        {/* Disable search when loading */}
        {/* Clear chat button */}
        <button className="clear-chat-button" onClick={clearChat}>
          Clear Chat
        </button>
      </div>
    </div>
  );
}

export default App;
