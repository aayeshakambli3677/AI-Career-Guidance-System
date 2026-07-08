import { Outlet } from "react-router-dom";

function AuthLayout() {
    return (
        <div className="auth-layout">
            <div className="auth-left">
                <h1>CareerGPT</h1>
                <p>
                    AI Powered Career Guidance System
                </p>
                <p>
                    Explore careers, improve skills, and prepare for your future.
                </p>
            </div>

            <div className="auth-right">
                <Outlet />
            </div>
        </div>
    );
}

export default AuthLayout;