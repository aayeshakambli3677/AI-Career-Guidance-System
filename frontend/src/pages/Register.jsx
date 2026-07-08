import "../pages/login.css";

function Register() {
  return (
    <div className="login-page">
      <div className="login-container">

        <h1 className="logo">CareerGPT</h1>

        <h2>Register</h2>

        <input placeholder="Full Name" />
        <input placeholder="Email" />
        <input placeholder="Password" />

        <button>Register</button>

      </div>
    </div>
  );
}

export default Register;