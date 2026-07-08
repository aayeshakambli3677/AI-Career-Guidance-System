import "./login.css";

function Login() {
  return (
    <div className="login-page">
      <div className="login-container">

        <h1 className="logo">CareerGPT</h1>

        <p className="tagline">
          AI Powered Career Guidance System
        </p>

        <h2>Login</h2>

        <input placeholder="Email" />
        <input placeholder="Password" />

        <button>Login</button>

      </div>
    </div>
  );
}

export default Login;