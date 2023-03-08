import { BrowserRouter, Route, Routes } from "react-router-dom";
import Dashboard from "../../Pages/Dashboard";
import DataTable from "../../Pages/DataTable";

function AppRoutes() {
    return (
        <Routes>
            <Route path="/" element={<Dashboard />}></Route>\
            <Route path="/data" element={<DataTable />}></Route>\
        </Routes>
    );
}
export default AppRoutes;