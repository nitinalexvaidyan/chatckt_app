import {SearchBar} from "./Components";
import './App.css';

function App() {

  const handleSearch = (query) => {
    console.log("Received query from child:", query);
    // Perform any actions with the received query, like making an API call
  };

  return (
    <div className="App">
       <SearchBar onSearch={handleSearch}/>
    </div>
  );
}

export default App;
