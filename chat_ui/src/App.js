import { useState, useEffect } from "react";
import axios from "axios";
import { SearchBar, ChatMessages } from "./Components";
import './App.css';
const BACKENDAPI = "http://3.80.153.168:5000/query"
function App() {
  const [messages, setMessages] = useState([]); // State to store chat messages

  // Load messages from sessionStorage on initial load
  useEffect(() => {
    const storedMessages = sessionStorage.getItem("messages");
    if (storedMessages) {
      setMessages(JSON.parse(storedMessages));
    }
  }, []);

  // Update sessionStorage whenever messages change
  useEffect(() => {
    if (messages.length > 0) {
      sessionStorage.setItem("messages", JSON.stringify(messages));
    }
  }, [messages]);

  const handleSearch = async (query) => {
    // Add user's message to the state
    const userMessage = { text: query, sender: "user" };
    setMessages((prevMessages) => [...prevMessages, userMessage]);

    try {
      // Make the API call to send the user's message
      const response = await axios.post(BACKENDAPI, {
        "query": query, // Sending the message to the API
      });

      // Assuming the API returns a JSON response with a 'message' field
      let botMessage
      if (response?.data?.response){
        botMessage = { text: response.data.response, sender: "bot" };
      }
      console.log(botMessage)

      // Add bot's message to the state
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      let botMessage = { text: "....", sender: "bot" };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
      console.error("Error:", error);
    }
  };

  const clearChat = () => {
    setMessages([]);
    sessionStorage.removeItem("messages");
  };

  return (
    <div className="App">
      <ChatMessages messages={messages} />
      <SearchBar onSearch={handleSearch} />
      
      {/* Clear chat button */}
      <button className="clear-chat-button" onClick={clearChat}>
        Clear Chat
      </button>
    </div>
  );
}

export default App;
