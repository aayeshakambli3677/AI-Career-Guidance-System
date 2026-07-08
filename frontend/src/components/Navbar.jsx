function Navbar() {
    return (
        <nav>
            <h2>AI Career Guidance System</h2>

            <ul style={{ listStyle: "none", display: "flex", gap: "20px" }}>
                <li>Dashboard</li>
                <li>Profile</li>
                <li>Career</li>
                <li>Resume</li>
                <li>Interview</li>
                <li>Roadmap</li>
                <li>Logout</li>
            </ul>
        </nav>
    );
}

export default Navbar;