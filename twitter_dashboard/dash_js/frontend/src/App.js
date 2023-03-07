import { Space } from "antd";
import { Router, BrowserRouter } from "react-router-dom";
import "./App.css";
import AppFooter from "./Components/AppFooter";
import AppHeader from "./Components/AppHeader";
import PageContent from "./Components/PageContent";
import SideMenu from "./Components/SideMenu";

function App() {
  return (
    <div className="App">
      <AppHeader />
      <div className="SideMenuAndPageContent">
        <BrowserRouter>
          <SideMenu></SideMenu>
          <PageContent></PageContent>
        </BrowserRouter>
      </div>
      <AppFooter />
    </div>
  );
}
export default App;