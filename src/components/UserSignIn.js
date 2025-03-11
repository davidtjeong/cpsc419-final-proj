import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function SignIn() {
  const [userId, setUserId] = useState("");
  const navigate = useNavigate();

  const handleSignIn = () => {
    if (userId.trim() !== "") {
      localStorage.setItem("user_id", userId);
      navigate("/home");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h2 className="text-2xl font-bold mb-4">Sign In</h2>
      <input
        type="text"
        placeholder="Enter User ID"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
        className="border p-2 rounded mb-2"
      />
      <button onClick={handleSignIn} className="bg-blue-500 text-white px-4 py-2 rounded">
        Sign In
      </button>
    </div>
  );
}

export default SignIn;
