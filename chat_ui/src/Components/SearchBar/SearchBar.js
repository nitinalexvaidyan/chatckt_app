import React, { useState } from "react";
import "./SearchBar.css";

const SearchBar = ({ onSearch, disabled }) => {
  const [query, setQuery] = useState("");

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault(); // Prevents adding a new line
      if (onSearch) {
        onSearch(query); // Send the text to the parent component
      }
      setQuery(""); // Clear the textarea
    }
  };

  const handleChange = (e) => {
    setQuery(e.target.value);
  };

  return (
    <div className="search-bar-container">
      <form className="search-bar-form" onSubmit={(e) => e.preventDefault()}>
        <textarea
          className="search-bar-input"
          placeholder="Message ChatCKT"
          value={query}
          onChange={handleChange}
          onKeyDown={handleKeyDown} // Handle Enter and Shift+Enter
          rows={3} // Adjust rows for the default height
          style={{
            width: "100%",
          }} // Optional: Adjust width
          disabled={disabled} 
        />
        <button
          type="button" // Prevent default form submission behavior
          className="search-bar-button"
          disabled={disabled} 
          onClick={() => {
            if (onSearch) onSearch(query);
            setQuery(""); // Clear the textarea
          }}
        >
          ➤
        </button>
      </form>
    </div>
  );
};

export default SearchBar;
