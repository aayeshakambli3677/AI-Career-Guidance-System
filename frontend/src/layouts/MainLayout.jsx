import { Outlet } from "react-router-dom";
import Sidebar from "../components/Sidebar";

function MainLayout() {
    return (
        <div>
            <Sidebar />

            <main style={{ marginLeft: "270px", padding: "20px" }}>
                <Outlet />
            </main>

        </div>
    );
}

export default MainLayout;