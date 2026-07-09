import { useState } from "react";
import { registerUser } from "../services/authServices";
import { Link } from "react-router-dom";
import "./login.css";

function Register() {

  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async () => {

    try {

      const result = await registerUser({
        full_name: fullName,
        email: email,
        password: password
      });

      console.log(result);

      alert("Registration Successful");

    } catch(error) {

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