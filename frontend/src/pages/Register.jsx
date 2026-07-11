import { useState } from "react";
import { registerUser } from "../services/authServices";
import { Link, useNavigate } from "react-router-dom";
import "./login.css";

function Register() {

  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleRegister = async () => {

  if (!fullName.trim()) {
    alert("Please enter your full name");
    return;
  }

  if (!email.trim()) {
    alert("Please enter your email");
    return;
  }

  if (!password.trim()) {
    alert("Please enter your password");
    return;
  }

  try {

    await registerUser({
      full_name: fullName,
      email,
      password
    });

    navigate("/");

  } catch (error) {
    console.error(error);
    alert("Registration Failed");
  }
};

  return (

    <div className="login-page">

      <div className="login-container">

        <h1 className="logo">
          CareerGPT
        </h1>

        <h2>Register</h2>

        <input
          placeholder="Full Name"
          value={fullName}
          onChange={(e)=>setFullName(e.target.value)}
        />

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

        <button onClick={handleRegister}>
          Register
        </button>

        <p style={{marginTop:"15px"}}>
          Already have an account?
          <Link to="/">
            Login
          </Link>
        </p>

      </div>

    </div>

  );
}

export default Register;