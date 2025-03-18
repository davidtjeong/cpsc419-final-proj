import React from "react";
import './App.css';
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Home from "./components/Home";
import ListItem from "./components/ListItem";
// import UserSignIn from "./components/UserSignIn";
import CreatePost from "./components/CreatePost";

function App() {
	return (
	<BrowserRouter>
		<Router>
			<div className="App">
			<header className="App-header">
			</header>
			<nav>
				<ul>
				<li>
					<a href="/">Home</a>
				</li>
				<li>
					<a href="/create-post">Create Post</a>
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
	</BrowserRouter>
	);
  }
  
export default App;
