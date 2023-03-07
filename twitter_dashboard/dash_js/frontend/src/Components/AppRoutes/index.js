import { BrowserRouter, Route, Routes } from "react-router-dom";
import Dashboard from "../../Pages/Dashboard";

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Dashboard />}></Route>\
    </Routes>
  );
}
export default AppRoutes;