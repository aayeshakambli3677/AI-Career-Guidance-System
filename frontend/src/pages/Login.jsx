import { useState } from "react";
import { loginUser } from "../services/authServices";
import { useNavigate, Link } from "react-router-dom";
import "./login.css";

function Login() {

  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {

    try {

      const result = await loginUser({
        email,
        password
      });

      console.log(result);

      localStorage.setItem(
        "token",
        result.access_token
      );

      alert("Login Successful");

      navigate("/dashboard");

    } catch (error) {

      console.error(error);
      alert("Login Failed");

    }
  };

  return (
    <div className="login-page">
      <div className="login-container">

        <h1 className="logo">CareerGPT</h1>

        <p className="tagline">
          AI Powered Career Guidance System
        </p>

        <h2>Login</h2>

        <input
          placeholder="Email"
          value={email}
          onChange={(e)=>setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e)=>setPassword(e.target.value)}
        />

        <button onClick={handleLogin}>
          Login
        </button>

        <p style={{marginTop:"15px"}}>
          Don't have an account?
          <Link to="/register">
            Register
          </Link>
        </p>

      </div>
    </div>
  );
}

export default Login;