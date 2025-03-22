import React from "react";
import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./components/Home";
import ListItem from "./components/ListItem";
// import UserSignIn from "./components/UserSignIn";
import CreatePost from "./components/CreatePost";

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
        </header>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/create-post">Create Post</Link>
            </li>
          </ul>
        </nav>
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/item/:id" element={<ListItem />} />
            <Route path="/create-post" element={<CreatePost />} /> {/* New route */}
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;

